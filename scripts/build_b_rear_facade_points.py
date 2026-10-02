"""Rebuild selected repeated B rear facade/return point diagnostics.

Input: ARCHITECTURAL_ENDPOINTS completed and explicitly selected failed reports;
checked B_REAR_FRONTAL_001 camera. Output: B_REAR_FACADE_POINTS JSON/CSV/SVG.
Run, render and inspect. Includes safe complete pairs from preserved failed
preflights, without accepting their failures or silently creating wall edges.
Projected points may be behind rendered surfaces; no automatic correspondence,
full facade endpoint, unseen continuity or closed footprint is granted.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path
from build_local_camera import project


def build(root):
    ref=root/'reference';data=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    reports={r['id']:r for r in data['reports']+data['rejected_attempts']}
    selections=[('B_REAR_WALL_JOIN_PREFLIGHT_001','front/recess diagnostic'),('B_REAR_EAST_JOIN_PREFLIGHT_002','east return'),('B_REAR_EAST_JOIN_PREFLIGHT_004','east return'),('B_REAR_WEST_MESH_HULL_TRANSITION_003','west wrapped Mesh'),('B_REAR_WEST_COMPONENT_TRANSITION_005','west wrapped Mesh'),('B_REAR_CORNER_SIDE_PREFLIGHT_006','west side-normal return')]
    rows=[];excluded=[]
    for id,group in selections:
        report=reports[id];assert max(report['restore_numeric_errors'])<=.01
        assert report['status'].startswith(('complete;','failed;'))
        obs=report['observations']
        for i in range(0,len(obs),2):
            pair=obs[i:i+2]
            if len(pair)!=2:
                excluded.append(dict(report=id,observation_index=i,reason='Unpaired own-origin failure preserved, never selected'));continue
            a,b=pair;assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface']
            if 'surfaceprop concrete,' not in str(b['surface']) or 'shape type: Mesh,' not in str(b['surface']):
                excluded.append(dict(report=id,observation_index=i,reason='Concrete Hull/recess or Dirt origin is not selected exposed facade Mesh'));continue
            if group=='west side-normal return' and b['eye_origin'][1]<2885:
                excluded.append(dict(report=id,observation_index=i,reason='Remote eastern hit or grazing front facade; not west return point'));continue
            for o in pair:
                assert math.dist(o['eye_origin'],o['hit'])>.1
                distance=float(re.search(r'DISTANCE:\s+([0-9.]+) inches',o['rangefinder_reply']).group(1));assert abs(math.dist(o['eye_origin'],o['hit'])-distance)<.02
                assert o['hit'][2]==104
            rows.append(dict(report=id,observation_index=i,group=group,source_x=b['hit'][0],source_y=b['hit'][1],source_z=b['hit'][2],x_cm=b['hit'][0]*2.54,y_cm=b['hit'][1]*2.54,z_cm=b['hit'][2]*2.54,surface='; '.join(b['surface']),source_status=report['status'],confidence='confirmed repeated local first-hit Mesh point; boundary interpretation unaccepted'))
    assert len(rows)==43
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='B_REAR_FRONTAL_001');assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    assert all(camera['tested_marker_y_range'][0]<=r['source_y']<=camera['tested_marker_y_range'][1] for r in rows)
    capture=next(c for c in camera['captures'] if c['id']=='QA_B_REAR_CAMERA_FIT_001_CLEAN');image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    visibility=reports['B_REAR_CAMERA_FIRST_HIT_VISIBILITY_007']
    assert max(visibility['restore_numeric_errors'])<=.01 and visibility['status'].startswith('complete;')
    assert len(visibility['architectural_review']['rows'])==5
    result=dict(source_build='25640462',camera_id=camera['id'],points=rows,explicitly_excluded_observations=excluded,camera_origin_visibility=visibility['architectural_review'],selected_failed_reports=[id for id,_ in selections if reports[id]['status'].startswith('failed;')],gate1='FAIL',scope=__doc__)
    (ref/'B_REAR_FACADE_POINTS.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ref/'B_REAR_FACADE_POINTS.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    encoded=base64.b64encode(image.read_bytes()).decode();colors={'front/recess diagnostic':'#39e5cd','east return':'#ffb45e','west wrapped Mesh':'#eac5ff','west side-normal return':'#70df77'}
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1170">','<rect width="1280" height="1170" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{encoded}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">B rear facade /43 repeated front and return point observations</text>','<text x="25" y="65" font-size="17">Cyan=front / orange=east angled return / purple=west wrap / green=west side rays. Point projections only.</text>']
    for r in rows:
        u,v=project(camera['projection_matrix'],[r['source_x'],r['source_y'],r['source_z']]);assert 4<u<1276 and 4<v<716
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="3" fill="{colors[r["group"]]}" stroke="#14202e"/>')
    # Numeric plan inset shows discrete actual XY at one measured ray height;
    # never connect into an invented facade polygon or flat corner.
    svg.append('<text x="25" y="858" font-size="17">Local native XY point plan atZ104 (264.16cm). Dots only; x right, y up. Full wall/floor boundary unaccepted.</text>')
    for r in rows:
        x=40+(r['source_x']+1900)*1.8;y=1025-(r['source_y']-2840)*1.5
        svg.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{colors[r["group"]]}"/>')
    svg.extend(['<text x="940" y="916" font-size="16">SourceX-1900..-1440</text>','<text x="940" y="947" font-size="16">SourceY2840..2911</text>','<text x="25" y="1075" font-size="16">Old guard failures and own-origin Dirt hit remain excluded/preserved. Remote/grazing side rays are not west corners.</text>','<text x="25" y="1110" font-size="16">Checked camera max.6502px at exact pose; deeper return withinY2800..2950 marker range. Projected points may be occluded.</text>','<text x="25" y="1145" font-size="16">No rendered corner agreement, complete wall ends, unseen plane continuation or closed architectural footprint accepted. Gate1 FAIL.</text></g></svg>'])
    (ref/'B_REAR_FACADE_POINTS.svg').write_text('\n'.join(svg)+'\n');print(len(rows),'reviewed selected repeated Mesh points;',len(excluded),'excluded selections retained')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
