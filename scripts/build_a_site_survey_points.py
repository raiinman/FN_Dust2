"""Overlay measured A/Under-A/Long points in the checked A Site camera.

First-hit source faces, cap and ground samples remain separate. Out-of-frame
and hidden/roof-covered points are retained explicitly. No connected boundary,
flat floor or closed courtyard polygon is inferred by point projection.
"""
import base64,hashlib,json,math,re
from pathlib import Path
from build_local_camera import project
from build_connector_profile import points


def build(root):
    ref=root/'reference';profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());allpoints=points(profile)
    floors=[r for r in profile['reports'] if r['id'].startswith('ELEVATOR_') or r['id'] in ['A_ENTRY_X1100_Y2760_001','A_ENTRY_FINE_X1100_Y2775_001','A_ENTRY_FINE_X1100_Y2790_001','A_ENTRY_FINE_X1100_Y2805_001','A_ENTRY_X1100_Y2840_001','LONG_A_CENTER_X1400_Y2450_001','LONG_A_CENTER_X1400_Y2650_001']]
    rows=[dict(id=r['id'],point=allpoints[r['id']],kind='parapet cap' if r['id']=='ELEVATOR_X1100_Y2320_001' else 'sampled ground/tread',scope=r.get('surface_semantics','Corrected repeated source point; source floor/tread/cap identities remain separate.'),report_id=r['id']) for r in floors]
    if 'asite_courtyard_ground_review' in profile:
        selected=profile['asite_courtyard_ground_review'];assert max(selected['driver_recovery']['restore_numeric_errors'])<=.01
        reports={r['id']:r for r in profile['reports']}
        for case in selected['plan']['cases']:
            r=reports[case['id']];pair=[o for o in r['observations'] if o['feature']=='floor'][-2:]
            assert pair[0]['hit']==pair[1]['hit']==allpoints[r['id']] and max(o['xy_error'] for o in pair)<=.02 and 'shape type: Mesh,' in str(pair[-1]['hit_description'])
            assert any('surfaceprop '+m+',' in str(pair[-1]['hit_description']) for m in ['sand','concrete'])
            rows.append(dict(id=r['id'],point=allpoints[r['id']],kind='sampled ground/tread',scope=r['surface_semantics'],report_id=r['id']))
    if 'asite_retaining_cap_review' in profile:
        selected=profile['asite_retaining_cap_review'];assert max(selected['driver_recovery']['restore_numeric_errors'])<=.01
        reports={r['id']:r for r in profile['reports']}
        for case in selected['plan']['cases']:
            r=reports[case['id']];pair=[o for o in r['observations'] if o['feature']=='floor'][-2:]
            assert pair[0]['hit']==pair[1]['hit']==allpoints[r['id']] and 'surfaceprop rock,' in str(pair[-1]['hit_description']) and 'shape type: Hull,' in str(pair[-1]['hit_description'])
            rows.append(dict(id=r['id'],point=allpoints[r['id']],kind='parapet cap',scope=r['surface_semantics'],report_id=r['id']))
    report=next(r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports'] if r['id']=='ASITE_COURTYARD_RETAINING_FACE_PREFLIGHT_032')
    assert report['source_build']=='25640462' and report['status'].startswith('complete;') and max(report['restore_numeric_errors'])<=.01 and len(report['observations'])==28
    for index in range(0,len(report['observations']),2):
        a,b=report['observations'][index:index+2];assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface'] and a['pose']==b['pose']
        station=next(s for s in report['config']['stations'] if s['id']==b['station_id'])
        values=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',b['pose'])];assert len(values)==6 and math.dist(values[:3],station['pose'])<=.01 and abs(values[3])<=.01 and abs(values[5])<=.01
        assert abs((values[4]-b['yaw']+180)%360-180)<=.01 and math.dist(values[:2]+[values[2]+64],b['eye_origin'])<=.01
        assert math.dist(b['eye_origin'],b['hit'])>.1 and abs(math.dist(b['eye_origin'],b['hit'])-float(b['rangefinder_reply'].split()[1]))<=.02
        existing=next((r for r in rows if r['kind']=='native first-hit face' and r['point']==b['hit'] and r['surface']==b['surface']),None)
        source=dict(station_id=b['station_id'],yaw=b['yaw'],eye_origin=b['eye_origin'])
        if existing:existing['source_rays'].append(source)
        else:rows.append(dict(id='FACE_'+str(len([r for r in rows if r['kind']=='native first-hit face'])+1),point=b['hit'],kind='native first-hit face',surface=b['surface'],source_rays=[source],report_id=report['id'],scope=report['review']))
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='ASITE_OVERHEAD_031')
    assert camera['normal_axis']==2 and max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_ASITE_CAMERA_FIT_031_CLEAN');image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    colors={'sampled ground/tread':'#49f6e0','parapet cap':'#ffc75d','native first-hit face':'#ec87ff'}
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1130">','<rect width="1280" height="1130" fill="#14202e"/>',f'<image y="100" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(image.read_bytes()).decode()}"/>','<g font-family="Arial" fill="white"><text x="25" y="35" font-size="23">A Site / Under-A and Long: calibrated point and elevation context</text><text x="25" y="70" font-size="16">Cyan sampled ground/treads / amber parapet cap / pink native first-hit faces. NativeZ; multiply by2.54 forcm.</text>']
    for row in rows:
        p=row['point'];assert camera['tested_marker_z_range'][0]<=p[2]<=camera['tested_marker_z_range'][1]
        uv=project(camera['projection_matrix'],p);row.update(projected_pixel=uv,z_cm=p[2]*2.54,in_frame=8<uv[0]<1272 and 8<uv[1]<712,rendered_correspondence='not accepted from projection alone; roof/cap/vegetation occlusion must be reviewed')
        if not row['in_frame']:continue
        u,v=uv;color=colors[row['kind']]
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="{color}" stroke="#14202e"><title>{row["id"]}: native{p}, Z{row["z_cm"]:.4f}cm</title></circle>')
        if row['kind']=='native first-hit face':
            label=row['id'].replace('FACE_','F')
            svg.append(f'<text x="{u+7}" y="{v+94}" fill="{color}" font-size="13" stroke="#14202e" stroke-width=".5">{label}</text>')
    labels=['Two westorigins: MeshX256/Y2450/Z160. Inside northfirstMeshY2784 atX900/950; southfirstMeshY2016.',
      'NorthX1050 seesY3080/Z180; X1000 reaches remoteY3845.33 (out of frame), rather than the same local wall.',
      'Two southoutsideYorigins agree MeshY2304/Z24. Pink projections under roof/cap do not validate rendered corners.',
      'Two eastoutsideXorigins agree MeshX1280/Y2450/Z60 versus HullX1319.9/Y2650/Z90; ground occlusion stays open.',
      'Fresh044 ground: lowerY2450Z95.34..97.63; upperY2900Z127.58..128.04 and northY3040Z129.04.',
      'All faces/materials/heights stay separate. No rectangular site, hidden floor or closed layered footprint inferred.',
      'Held camera maximum0.509377px. Source face values do not grant exact renderer/collision correspondence.',
      'Gate1 FAIL: complete critical extents and bounded continuous layered whole-map footprint still required.']
    svg.extend(f'<text x="25" y="{855+i*32}" font-size="15">{label}</text>' for i,label in enumerate(labels));svg.append('</g></svg>')
    (ref/'A_SITE_SURVEY_POINTS.svg').write_text('\n'.join(svg)+'\n');(ref/'A_SITE_SURVEY_POINTS.json').write_text(json.dumps(dict(source_build='25640462',camera_id=camera['id'],capture=capture,points=rows,gate1='FAIL',scope=__doc__),indent=2)+'\n')
    print(len(rows),'unique reviewed ground/cap/first-hit face projections;',sum(not r['in_frame'] for r in rows),'out of frame; no full boundaries')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
