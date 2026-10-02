"""Project repeated B ground, cover and timber samples into checked overhead.

Rebuild, render and inspect B_PLATFORM_OVERHEAD_POINTS JSON/SVG. No connecting
surface, full retaining body or continuous architectural perimeter is inferred.
"""
import base64,hashlib,json,math,re
from pathlib import Path
from build_local_camera import project

def build(root):
    ref=root/'reference'
    profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text())
    reports={r['id']:r for r in profile['reports']}
    rows=[]
    for key in ['b_platform_column_review','b_covered_top_review']:
        spec=profile[key];assert max(spec['driver_recovery']['restore_numeric_errors'])<=.01
        for case in spec['plan']['cases']:
            r=reports[case['id']];assert r['status'].startswith('complete;') and r['source_build']=='25640462'
            pair=[o for o in r['observations'] if o['feature']=='floor'][-2:]
            assert len(pair)==2 and pair[0]['hit']==pair[1]['hit']==r['endpoints']['floor'] and all(o['xy_error']<=.02 for o in pair)
            cover='surfaceprop Wood_Plank,' in str(pair[1]['hit_description'])
            rows.append(dict(id=r['id'],point=r['endpoints']['floor'],kind='cover top' if cover else 'ground',scope=r['surface_semantics']))
    data=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    front=next(r for r in data['reports'] if r['id']=='B_PLATFORM_FRONT_COMPONENT_RESUME_008')
    assert front['status'].startswith('complete;') and front['source_build']=='25640462' and max(front['restore_numeric_errors'])<=.01
    obs=front['observations'];assert len(obs)==12
    for n in range(0,len(obs),2):
        a,b=obs[n:n+2]
        assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface']
        assert 'surfaceprop Wood_Plank,' in str(b['surface']) and 'shape type: Hull,' in str(b['surface'])
        for o in [a,b]:
            distance=float(re.search(r'DISTANCE:\s+([0-9.]+) inches',o['rangefinder_reply']).group(1))
            assert abs(math.dist(o['eye_origin'],o['hit'])-distance)<.02 and distance>.1
        rows.append(dict(id=b['station_id'],point=b['hit'],kind='timber front',scope='Repeated first-Wood Hull atZ20/40/60; independent low origin agrees with preserved safe pairs in failed007. No masonry, timber ends or complete platform boundary accepted.'))
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='B_PLATFORM_OVERHEAD_009')
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_B_PLATFORM_CAMERA_FIT_009_CLEAN')
    image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    colors={'ground':'#49f6e0','cover top':'#ffc75d','timber front':'#ec87ff'}
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1050">','<rect width="1280" height="1050" fill="#14202e"/>',f'<image y="100" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(image.read_bytes()).decode()}"/>','<g font-family="Arial" fill="white"><text x="25" y="35" font-size="23">B central courtyard / calibrated point and elevation context</text><text x="25" y="70" font-size="17">Cyan ground / amber covered top / pink timber first-hit face. NativeZ labels; multiply by2.54 forcm.</text>']
    for row in rows:
        p=row['point'];assert camera['tested_marker_z_range'][0]<=p[2]<=camera['tested_marker_z_range'][1] or row['kind']=='ground' and 1<=p[2]<5
        u,v=project(camera['projection_matrix'],p);assert 8<u<1272 and 8<v<712
        row['projected_pixel']=[u,v];row['z_cm']=p[2]*2.54
        color=colors[row['kind']]
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="{color}" stroke="#14202e"><title>{row["id"]} {p}</title></circle>')
        if row['kind']=='ground' and not (p[1]<2450 and p[0]>-1950):svg.append(f'<text x="{u+8}" y="{v+91}" font-size="13" fill="{color}" stroke="#14202e" stroke-width=".4">Z{p[2]:.2f}</text>')
    svg.extend(['<text x="25" y="850" font-size="17">Six pink points: timber first-hitZ20/40/60 at twoY. Amber covered-topZ102.35..102.98; numeric detail in paired JSON.</text>','<text x="25" y="883" font-size="17">Overlapping pink points are differentZ observations, not additional corners. Covered ground and unseen body limits remain open.</text>','<text x="25" y="916" font-size="17">Held camera maximum0.532px. GroundZ1.33..4.71 extrapolates up to3.67native below the lowestZ5 marker.</text>','<text x="25" y="949" font-size="17">Projected points alone do not prove renderer/collision correspondence. No connecting outline, uniform floor or full site acceptance.</text>','<text x="25" y="1000" font-size="19">Gate1 FAIL. Complete structural bounds and layered whole-map footprint still required.</text></g></svg>'])
    (ref/'B_PLATFORM_OVERHEAD_POINTS.svg').write_text('\n'.join(svg)+'\n')
    (ref/'B_PLATFORM_OVERHEAD_POINTS.json').write_text(json.dumps(dict(source_build='25640462',camera_id=camera['id'],capture=capture,points=rows,gate1='FAIL',scope=__doc__),indent=2)+'\n')
    print(len(rows),'repeated ground/cover/timber point projections; no full boundaries')

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
