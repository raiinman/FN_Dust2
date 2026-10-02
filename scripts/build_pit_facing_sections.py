"""Derive bounded Pit native first-Mesh facing intervals at source Z0.

Southern rendered correspondence is checked at Z-80/-40, below the separate
roof; Z0 itself remains occluded. These are component extents, not complete
wall bodies, full-height sections or closed floor/map boundaries.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path
from build_local_camera import inverse_plane,project


def repeated(report,index):
    a,b=report['observations'][index-1:index+1]
    assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface'] and a['pose']==b['pose']
    values=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',b['pose'])]
    assert len(values)==6 and abs(values[3])<=.01 and abs(values[5])<=.01
    eye=values[:2]+[values[2]+64]
    assert math.dist(eye,b['eye_origin'])<=.01 and math.dist(eye,b['hit'])>.1
    assert abs(math.dist(eye,b['hit'])-float(b['rangefinder_reply'].split()[1]))<=.02
    assert abs(eye[1]-b['hit'][1])<=.02 and abs(eye[2]-b['hit'][2])<=.02
    return b


def sections(ref):
    register=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    reports={r['id']:r for r in register['reports']}
    cameras={c['id']:c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras']}
    review=json.loads((ref/'PIT_WALL_RENDER_REVIEW.json').read_text())
    fresh=reports['PIT_SOUTH_JOIN_INDEPENDENT_LOWER_BRACKETS_029']
    assert fresh['source_build']=='25640462' and fresh['status'].startswith('complete;') and max(fresh['restore_numeric_errors'])<=.01
    assert len(fresh['observations'])==32
    result=[]
    for side,plane,camnum,northnum,southnum,offmaterial,offshape in [('WEST',1272,26,12,24,'sand','Mesh'),('EAST',1592,27,13,25,'concrete','Hull')]:
        intervals=[];source_ids=[]
        for end,num in [('south',southnum),('north',northnum)]:
            id=f'PIT_{side}_Z0_SOUTH_MESH_HULL_JOIN_{num:03}' if end=='south' else f'PIT_{side}_Z0_FIRST_MESH_LIMIT_{num:03}'
            r=reports[id];c=r['config'];source_ids.append(id)
            assert r['status'].startswith('complete;') and r['source_build']=='25640462' and max(r['restore_numeric_errors'])<=.01 and not r.get('restore_error')
            assert c['normal_axis']==0 and c['height_native']==0
            assert len(r['brackets'])==2 and len({b['origin_id'] for b in r['brackets']})==2
            observed=[]
            for b in r['brackets']:
                assert b['on']['on_component'] and not b['off']['on_component']
                for role in ['on','off']:
                    o=repeated(r,b[role]['observation_index'])
                    assert o['eye_origin'][2]==0
                    if role=='on':
                        assert abs(o['hit'][0]-plane)<=.02 and 'surfaceprop concrete,' in str(o['surface']) and 'shape type: Mesh,' in str(o['surface'])
                    else:
                        material='concrete' if end=='south' else offmaterial
                        shape='Hull' if end=='south' else offshape
                        assert f'surfaceprop {material},' in str(o['surface']) and f'shape type: {shape},' in str(o['surface'])
                raw=b['tangent_interval_native'];assert raw[1]-raw[0]<=c['maximum_bracket_native']
                observed.append(raw)
            assert observed[0]==observed[1]
            # Printed source pose/endpoint resolution is included separately
            # from the native search bracket; no render offset is absorbed.
            intervals.append([observed[0][0]-.01,observed[0][1]+.01])
        for i in range(0,len(fresh['observations']),2):
            o=repeated(fresh,i+1)
            if not o['station_id'].startswith(side+'_'):continue
            station=next(s for s in fresh['config']['stations'] if s['id']==o['station_id'])
            assert o['eye_origin'][2] in [-80,-40] and o['eye_origin'][0] in [1400,1424]
            assert intervals[0][0]<=station['pose'][1]<=intervals[0][1]
            assert 'surfaceprop concrete,' in str(o['surface'])
            if '_ON_' in o['station_id']:
                assert 'shape type: Mesh,' in str(o['surface']) and abs(o['hit'][0]-plane)<=.02
            else:assert 'shape type: Hull,' in str(o['surface'])
        camera=cameras[f'PIT_{side}_WALL_FRONTAL_{camnum:03}']
        assert camera['normal_axis']==0 and max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
        north=next(r for r in review['rows'] if r['side']==side and r['end']=='north')
        selected=[north]+[r for r in review['lower_join_reviews'] if r['side']==side]
        assert len(selected)==3
        for r in selected:
            assert r['status'].startswith('CORROBORATED') and r['pixel_radius']==1.5
            image=ref.parent/north['clean_image_path']
            assert hashlib.sha256(image.read_bytes()).hexdigest()==north['clean_jpeg_sha256']
            u,v=r['observed_vertical_break_pixel'];m=camera['projection_matrix']
            ys=[inverse_plane(m,u+du,v,plane,0)[1] for du in [-1.5,1.5]]
            bound=intervals[1] if r is north else intervals[0]
            assert min(ys)<=bound[0]<=bound[1]<=max(ys), 'Selected rendered seam does not bound native component interval'
        length=[(intervals[1][0]-intervals[0][1])*2.54,(intervals[1][1]-intervals[0][0])*2.54]
        result.append(dict(id=f'PIT_{side}_Z0_FIRST_MESH_FACING_LENGTH',side=side,plane_native=plane,height_native=0,south_interval_native=intervals[0],north_interval_native=intervals[1],length_interval_cm=length,length_midpoint_cm=sum(length)/2,transition_reports=source_ids,lower_check_report=fresh['id'],camera_id=camera['id'],clean_image_path=north['clean_image_path'],clean_jpeg_sha256=north['clean_jpeg_sha256'],limits='Native first-Mesh extent atZ0. Southern sameXY join independently checked/rendered atZ-80/-40; Z0 roof occlusion remains. North local facing break only. No full wall body, hidden base, uniform height, continuous ground outline or whole-map acceptance.'))
    return result


def measurement_rows(ref):
    return [dict(id=r['id'],area='Pit',feature=r['side'].title()+' native first-Mesh facing extent at sourceZ0',value=round(r['length_midpoint_cm'],4),unit='cm',method='two independent native transition origins; prospective lower-height checks; checked-camera component correspondence; SCALE_CALIBRATION',source_id='PIT_FACING_SECTIONS/'+r['id'],confidence='bounded native component extent; southern renderedZ0 remains occluded',tolerance=f"Native interval[{r['length_interval_cm'][0]:.5f},{r['length_interval_cm'][1]:.5f}]cm; printed resolution .01native perend; partial rendered correspondence separately scoped",notes=r['limits']) for r in sections(ref)]


def build(root):
    ref=root/'reference';rows=sections(ref)
    (ref/'PIT_FACING_SECTIONS.json').write_text(json.dumps(dict(source_build='25640462',sections=rows,gate1='FAIL',limits=__doc__),indent=2)+'\n')
    with (ref/'PIT_FACING_SECTIONS.csv').open('w',newline='') as f:
        fields=['id','plane_native','height_native','length_low_cm','length_high_cm','limits'];w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r in rows:w.writerow({**{k:r[k] for k in ['id','plane_native','height_native','limits']},'length_low_cm':r['length_interval_cm'][0],'length_high_cm':r['length_interval_cm'][1]})
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1110" viewBox="0 0 1280 1110">','<rect width="1280" height="1110" fill="#14202e"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">Pit native first-Mesh facing extents / source Z0</text><text x="25" y="62" font-size="17">Independent material brackets; southern rendered checks at Z-80/-40. Full bodies and ground boundaries open.</text>']
    cameras={c['id']:c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras']}
    for n,r in enumerate(rows):
        top=90+n*500;data=base64.b64encode((root/r['clean_image_path']).read_bytes()).decode()
        svg.append(f'<image x="180" y="{top}" width="880" height="495" href="data:image/jpeg;base64,{data}"/>')
        svg.append(f'<text x="25" y="{top+30}" font-size="17">{r["side"]}</text><text x="25" y="{top+60}" font-size="13">{r["length_interval_cm"][0]:.3f}..</text><text x="25" y="{top+80}" font-size="13">{r["length_interval_cm"][1]:.3f}cm</text>')
        m=cameras[r['camera_id']]['projection_matrix'];pixels=[]
        for interval in [r['south_interval_native'],r['north_interval_native']]:
            u,v=project(m,[r['plane_native'],sum(interval)/2,0]);pixels.append((180+u*880/1280,top+v*495/720))
        svg.append(f'<line x1="{pixels[0][0]}" y1="{pixels[0][1]}" x2="{pixels[1][0]}" y2="{pixels[1][1]}" stroke="#39e5cd" stroke-width="2" stroke-dasharray="7 4"/>')
    svg.append('<text x="25" y="1090" font-size="15">Dashed Z0 extent is native component evidence; south end is under a separate roof. Gate 1 remains FAIL.</text></g></svg>')
    (ref/'PIT_FACING_SECTIONS.svg').write_text('\n'.join(svg)+'\n')
    print([(r['id'],r['length_interval_cm']) for r in rows])


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
