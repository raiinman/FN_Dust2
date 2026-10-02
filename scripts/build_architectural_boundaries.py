"""Validate explicitly reviewed exposed local collision-face sections.

Two independent source origins, Mesh/Hull component-aware transition rays and
a separately calibrated clean rendered view are mandatory. Output intervals
describe only the declared section height, never hidden/full-height bodies,
ground perimeter or polygon closure. Retain plane-only failed interpretations.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path
from build_local_camera import inverse_plane,project


def section_rows(ref):
    register=json.loads((ref/'ARCHITECTURAL_BOUNDARIES.json').read_text())
    reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']}
    cameras={c['id']:c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras']}
    rows=[]
    for section in register['sections']:
        assert section['scope']=='exposed local collision-face section only'
        axis=section['normal_axis'];assert axis in [0,1]
        plane=section['plane_native'];height=section['height_native']
        evidence=[reports[id] for id in section['transition_reports']]
        assert len(evidence)>=2 and len({tuple(r['config']['pose']) for r in evidence})==len(evidence)
        ends=[]
        for end in section['ends']:
            intervals=[];padding=[]
            for report in evidence:
                config=report['config']
                assert report['source_build']==register['source_build'] and report['status'].startswith('complete;')
                assert max(report['restore_numeric_errors'])<=.01 and not report.get('restore_error')
                assert config['axis']==axis and config['plane_native']==plane and config['required_shape_type']=='Mesh'
                bracket=next(b for b in report['brackets'] if b['id']==end['bracket_id'])
                assert bracket['on']['on_plane'] and not bracket['off']['on_plane']
                assert bracket['bracket_width_native']<=.02
                for role in ['on','off']:
                    index=bracket[role]['observation_index'];a,b=report['observations'][index-1:index+1]
                    assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface']
                    assert a['yaw']==b['yaw']==bracket[role]['yaw'] and a['eye_origin'][2]==height
                    assert 'surfaceprop concrete,' in str(b['surface'])
                    if role=='on':
                        assert 'shape type: Mesh,' in str(b['surface'])
                        assert abs(b['hit'][axis]-plane)<=config['on_plane_tolerance_native']
                    else:
                        assert end['off_surface_required'] in str(b['surface'])
                        if end.get('off_plane_required'):
                            assert abs(b['hit'][axis]-plane)>config['on_plane_tolerance_native']
                    values=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',b['pose'])]
                    direction=[math.cos(math.radians(values[4])),math.sin(math.radians(values[4]))]
                    projected=values[1-axis]+(plane-values[axis])*direction[1-axis]/direction[axis]
                    # Derive numeric padding from actual-vs-requested pose,
                    # declared printed-plane rounding and printed endpoint resolution.
                    padding.append(abs(projected-bracket[role]['projected_plane_coordinate_native'])+section['plane_rounding_native']*abs(direction[1-axis]/direction[axis])+.005)
                intervals.append(bracket['projected_coordinate_interval_native'])
            assert max(i[0] for i in intervals)<=min(i[1] for i in intervals), 'Independent origins disagree'
            guard=max(padding)
            interval=[min(i[0] for i in intervals)-guard,max(i[1] for i in intervals)+guard]
            ends.append(dict(id=end['id'],native_interval=interval,numeric_padding_native=guard,independent_raw_intervals=intervals))
        assert ends[0]['native_interval'][1]<ends[1]['native_interval'][0]
        length=[(ends[1]['native_interval'][0]-ends[0]['native_interval'][1])*2.54,
                (ends[1]['native_interval'][1]-ends[0]['native_interval'][0])*2.54]
        camera=cameras[section['camera_id']];assert camera['normal_axis']==axis
        assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
        image=ref.parent/section['clean_image_path']
        assert hashlib.sha256(image.read_bytes()).hexdigest()==section['clean_jpeg_sha256']
        render=[]
        for end,review in zip(ends,section['rendered_corner_reviews']):
            assert review['end_id']==end['id'] and review['pixel_radius']==1.5
            center=inverse_plane(camera['projection_matrix'],*review['pixel'],plane,axis)
            points=[inverse_plane(camera['projection_matrix'],review['pixel'][0]+du,review['pixel'][1]+dv,plane,axis) for du,dv in [(-1.5,-1.5),(-1.5,1.5),(1.5,-1.5),(1.5,1.5)]]
            bounds=[min(p[1-axis] for p in points),max(p[1-axis] for p in points)]
            assert bounds[0]<=end['native_interval'][0]<=end['native_interval'][1]<=bounds[1], 'Rendered/native correspondence outside reviewed pixel bounds'
            render.append(dict(end_id=end['id'],pixel=review['pixel'],native_tangent_interval=bounds,native_point=center,review=review['review']))
        rows.append(dict(id=section['id'],area=section['area'],normal_axis=axis,plane_native=plane,height_native=height,ends=ends,length_interval_cm=length,length_midpoint_cm=sum(length)/2,rendered_correspondence=render,scope=section['scope'],clean_image_path=section['clean_image_path'],clean_jpeg_sha256=section['clean_jpeg_sha256'],camera_id=section['camera_id'],transition_reports=section['transition_reports']))
    return rows


def measurement_rows(ref):
    return [dict(id=r['id']+'_LENGTH',area=r['area'],feature='Exposed west plaster collision-face section length at nativeZ104',value=round(r['length_midpoint_cm'],4),unit='cm',method='two independent origins with component-aware repeated transitions; calibrated rendered corner correspondence; SCALE_CALIBRATION',source_id='ARCHITECTURAL_BOUNDARIES/'+r['id'],confidence='triangulated bounded exposed local section',tolerance=f"Native section length interval[{r['length_interval_cm'][0]:.4f},{r['length_interval_cm'][1]:.4f}]cm; rendered corners within independently checked1.5px selection boxes",notes='Declared Z section only. South recess/north Hull join delimit exposed Mesh; no hidden continuation, full-height wall, floor perimeter, playerclip or whole-map footprint inference.') for r in section_rows(ref)]


def build(root):
    ref=root/'reference';rows=section_rows(ref)
    (ref/'ARCHITECTURAL_BOUNDARY_SECTIONS.json').write_text(json.dumps(dict(source_build='25640462',sections=rows,gate1='FAIL',limits=__doc__),indent=2)+'\n')
    with (ref/'ARCHITECTURAL_BOUNDARY_SECTIONS.csv').open('w',newline='') as f:
        fields=['id','area','height_native','plane_native','length_low_cm','length_high_cm','scope'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r in rows:w.writerow({**{k:r[k] for k in ['id','area','height_native','plane_native','scope']},'length_low_cm':r['length_interval_cm'][0],'length_high_cm':r['length_interval_cm'][1]})
    r=rows[0];cameras={c['id']:c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras']};camera=cameras[r['camera_id']]
    data=base64.b64encode((root/r['clean_image_path']).read_bytes()).decode()
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="900" viewBox="0 0 1280 900">','<rect width="1280" height="900" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">B-west exposed plaster section / native Z104 (264.16cm)</text>',f'<text x="25" y="65" font-size="18">Bounded collision section: {r["length_interval_cm"][0]:.3f}..{r["length_interval_cm"][1]:.3f}cm / ten independent camera checks</text>']
    pixels=[]
    for end in r['ends']:
        p=[0,0,r['height_native']];p[r['normal_axis']]=r['plane_native'];p[1-r['normal_axis']]=sum(end['native_interval'])/2
        u,v=project(camera['projection_matrix'],p);pixels.append((u,v+100));svg.append(f'<circle cx="{u}" cy="{v+100}" r="6" fill="#39e5cd"/><text x="{u+8}" y="{v+89}" font-size="16">{end["id"]}</text>')
    svg.append(f'<line x1="{pixels[0][0]}" y1="{pixels[0][1]}" x2="{pixels[1][0]}" y2="{pixels[1][1]}" stroke="#39e5cd" stroke-width="3"/>')
    svg.extend(['<text x="25" y="850" font-size="17">South recess / north Mesh-to-Hull joint. Exposed section only; hidden wall and ground footprint remain unresolved.</text>','<text x="25" y="880" font-size="17">Ray intervals include pose/plane rounding. Rendered corner boxes are separate pixel-selection bounds. Gate1 FAIL.</text></g></svg>'])
    (ref/'ARCHITECTURAL_BOUNDARIES.svg').write_text('\n'.join(svg)+'\n')
    print([(r['id'],r['length_interval_cm']) for r in rows])


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
