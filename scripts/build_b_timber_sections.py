"""Derive two sampled B timber thicknesses and bounded local upper elevations.

Original failed component classifications remain in ARCHITECTURAL_ENDPOINTS.
Rebuild/render/inspect B_TIMBER_LOCAL_SECTIONS JSON/CSV/SVG; no full strip,
hidden base, uniform top, rendered seam or continuous platform outline inferred.
"""
import base64,csv,hashlib,json,math
from pathlib import Path
from build_b_frame_sections import repeated
from build_local_camera import project

def sections(ref):
    data=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    reports={r['id']:r for r in data['reports']}
    front=reports['B_PLATFORM_FRONT_COMPONENT_RESUME_008'];back=reports['B_PLATFORM_TIMBER_BACK_FACE_016']
    rows=[]
    for y,upper_id,off_material,off_shape in [(2500,'B_PLATFORM_TIMBER_UPPER_Y2500_RESUME_012','Wood_Panel','Hull'),(2600,'B_PLATFORM_TIMBER_UPPER_Y2600_GRAVEL_017','gravel','Mesh')]:
        upper=reports[upper_id]
        for r in [front,back,upper]:assert r['source_build']=='25640462' and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01 and not r.get('restore_error')
        def station(r,id):
            index=next(i for i,o in enumerate(r['observations']) if o['station_id']==id and o['repeat']==2)
            o=repeated(r,index);assert 'surfaceprop Wood_Plank,' in str(o['surface']) and 'shape type: Hull,' in str(o['surface']);return o
        east=station(front,f'X1700_Y{y}_Z40')
        west=[station(back,f'X{x}_Y{y}_Z40') for x in [1770,1790]]
        assert west[0]['hit']==west[1]['hit'] and west[0]['eye_origin']!=west[1]['eye_origin']
        assert west[0]['hit'][1:]==east['hit'][1:]==[y,40]
        thickness=math.dist(west[0]['hit'],east['hit'])*2.54
        assert upper['config']['normal_axis']==0 and upper['config']['tangent_axis']==2 and len(upper['brackets'])==2
        intervals=[];on_points=[];off_points=[]
        for b in upper['brackets']:
            on,off=[repeated(upper,b[k]['observation_index']) for k in ['on','off']]
            origin=next(o for o in upper['config']['origins'] if o['id']==b['origin_id'])
            assert 'surfaceprop Wood_Plank,' in str(on['surface']) and 'shape type: Hull,' in str(on['surface'])
            assert origin['on_normal_band'][0]<=on['hit'][0]<=origin['on_normal_band'][1]
            assert on['hit'][0]==east['hit'][0] and on['hit'][1]==y
            assert f'surfaceprop {off_material},' in str(off['surface']) and f'shape type: {off_shape},' in str(off['surface'])
            assert off['hit'][0]<on['hit'][0]-1
            interval=b['tangent_interval_native'];assert interval[1]-interval[0]<=.1
            intervals.append(interval);on_points.append(on['hit']);off_points.append(off['hit'])
        assert intervals[0]==intervals[1] and on_points[0]==on_points[1] and off_points[0]==off_points[1]
        z=intervals[0];bounds=[(z[0]-.01)*2.54,(z[1]+.01)*2.54]
        rows.append(dict(native_y=y,front_point=east['hit'],back_point=west[0]['hit'],thickness_cm=thickness,thickness_interval_cm=[thickness-.0508,thickness+.0508],upper_report=upper_id,upper_interval_native=z,upper_elevation_interval_cm=bounds,upper_on_point=on_points[0],upper_off_point=off_points[0],scope='Two local different-Y sections; upper elevation relative sourceZ0, not ground-to-top height. Off-hit is remoteWood_Panel atY2500 and nearer gravel atY2600. No interpolation/fulltop/hiddenbase/bodyends or renderer offset bounds.'))
    return rows

def measurement_rows(ref):
    result=[]
    for r in sections(ref):
        for kind,bounds,feature in [('THICKNESS',r['thickness_interval_cm'],'Sampled timber retaining strip thickness atnativeZ40'),('UPPER_ELEVATION',r['upper_elevation_interval_cm'],'Local first-Wood upper visibility elevation relative nativeZ0')]:
            result.append(dict(id=f'B_TIMBER_Y{r["native_y"]}_{kind}',area='B Site',feature=feature+f' /nativeY{r["native_y"]}',value=round(sum(bounds)/2,4),unit='cm',method='repeated outside-origin Wood_Plank Hull section / independent-origin upper material brackets; SCALE_CALIBRATION',source_id='B_TIMBER_LOCAL_SECTIONS/Y'+str(r['native_y']),confidence='confirmed bounded local collision section',tolerance=f'Native numeric interval[{bounds[0]:.5f},{bounds[1]:.5f}]cm; rendered correspondence separate',notes=r['scope']))
    return result

def build(root):
    ref=root/'reference';rows=sections(ref)
    c=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='B_PLATFORM_OVERHEAD_009')
    assert max(g['maximum_residual_px'] for g in c['groups'][1:])<1
    image=next(x for x in c['captures'] if x['id']=='QA_B_PLATFORM_CAMERA_FIT_009_CLEAN');raw=(root/image['repository_image_path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==image['jpeg_sha256']
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1060">','<rect width="1280" height="1060" fill="#14202e"/>',f'<image y="100" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(raw).decode()}"/>','<g font-family="Arial" fill="white"><text x="25" y="35" font-size="23">B retaining timber / two measured local sections</text><text x="25" y="70" font-size="17">Pink opposed face points atZ40 / amber independently bracketed upper first-Wood points.</text>']
    for r in rows:
        p,q=[project(c['projection_matrix'],r[key]) for key in ['front_point','back_point']]
        svg.append(f'<path d="M{p[0]},{p[1]+100}L{q[0]},{q[1]+100}" stroke="#ec87ff" stroke-width="2"/>')
        for v in [p,q]:svg.append(f'<circle cx="{v[0]}" cy="{v[1]+100}" r="4" fill="#ec87ff" stroke="#14202e"/>')
        u,v=project(c['projection_matrix'],r['upper_on_point']);svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="#ffc75d" stroke="#14202e"/>')
    profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text())
    top_review=profile['b_timber_top_review'];assert max(top_review['driver_recovery']['restore_numeric_errors'])<=.01
    for case in top_review['plan']['cases']:
        report=next(r for r in profile['reports'] if r['id']==case['id'])
        pair=[o for o in report['observations'] if o['feature']=='floor'][-2:]
        assert pair[0]['hit']==pair[1]['hit']==report['endpoints']['floor'] and all(o['xy_error']<=.02 for o in pair)
        material,shape=('Wood_Plank','Hull') if case['xy'][1]==2500 else ('gravel','Mesh')
        assert f'surfaceprop {material},' in str(pair[1]['hit_description']) and f'shape type: {shape},' in str(pair[1]['hit_description'])
        row=next(r for r in rows if r['native_y']==case['xy'][1]);row['selected_upper_column']=dict(report=case['id'],point=report['endpoints']['floor'],material=material,shape=shape)
        u,v=project(c['projection_matrix'],report['endpoints']['floor']);svg.append(f'<circle cx="{u}" cy="{v+100}" r="3" fill="#49f6e0" stroke="#14202e"/>')
    for n,r in enumerate(rows):
        lo,hi=r['upper_elevation_interval_cm'];svg.append(f'<text x="25" y="{858+n*33}" font-size="17">NativeY{r["native_y"]}: thickness{r["thickness_cm"]:.4f}cm; upperZ{r["upper_interval_native"]} / absolute elevation[{lo:.4f},{hi:.4f}]cm.</text>')
    svg.extend(['<text x="25" y="925" font-size="17">Cyan direct top samples: WoodZ62.67 atY2500; gravelZ61.94 atY2600, slightly behind each front point.</text>','<text x="25" y="958" font-size="17">Pink chords cross the body at two stations only. Neither uniform thickness nor shared flat cap is accepted.</text>','<text x="25" y="991" font-size="17">Hidden base, full strip ends, entire platform/ground envelope and exact renderer/collision seams remain unresolved.</text>','<text x="25" y="1030" font-size="19">Gate1 FAIL. Camera max held error0.532px; projection is separate from structural correspondence.</text></g></svg>'])
    (ref/'B_TIMBER_LOCAL_SECTIONS.svg').write_text('\n'.join(svg)+'\n')
    (ref/'B_TIMBER_LOCAL_SECTIONS.json').write_text(json.dumps(dict(source_build='25640462',camera_id=c['id'],sections=rows,gate1='FAIL',scope=__doc__),indent=2)+'\n')
    with (ref/'B_TIMBER_LOCAL_SECTIONS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['native_y','thickness_cm','upper_native_z_low','upper_native_z_high','upper_elevation_cm_low','upper_elevation_cm_high','scope'])
        for r in rows:w.writerow([r['native_y'],r['thickness_cm'],*r['upper_interval_native'],*r['upper_elevation_interval_cm'],r['scope']])
    print([(r['native_y'],r['thickness_cm'],r['upper_elevation_interval_cm']) for r in rows])

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
