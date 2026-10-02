"""Project reviewed eastern A retaining components without inventing body bounds.

Inputs: native reports033/038, corrected columns034/037 and checked camera036.
Outputs: reference/A_RETAINING_CONTEXT.json/.svg. Render and inspect after build.
Points identify measured first-hit components; connecting lines are not inferred.
Outsideground below marker range and occluded floor/cap remain explicit.
"""
import base64,hashlib,json,math,re
from pathlib import Path
from build_connector_profile import points
from build_local_camera import project


def build(root):
    ref=root/'reference';architecture=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text());profiles=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());samples=points(profiles)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='ASITE_EAST_RETAINING_FRONTAL_036')
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_ASITE_FRONTAL_FIT_036_CLEAN');image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    terminal=json.loads((ref/'A_RETAINING_TERMINAL_REVIEW.json').read_text())
    assert terminal['camera_id']==camera['id'] and terminal['source_build']=='25640462'
    checked_capture=next(c for c in camera['captures'] if c['id']==terminal['capture_id'])
    assert hashlib.sha256((root/checked_capture['repository_image_path']).read_bytes()).hexdigest()==checked_capture['jpeg_sha256']
    report=next(r for r in architecture['reports'] if r['id']==terminal['report_id'])
    assert report['status'].startswith('complete;') and max(report['restore_numeric_errors'])<=.01 and len(report['brackets'])==2
    intervals=[b['tangent_interval_native'] for b in report['brackets']];assert intervals[0]==intervals[1]==[2303.9921875,2304]
    for i in range(0,len(report['observations']),2):
        a,b=report['observations'][i:i+2];assert a['hit']==b['hit'] and a['surface']==b['surface'] and a['pose']==b['pose']
        assert abs(math.dist(b['eye_origin'],b['hit'])-float(b['rangefinder_reply'].split()[1]))<=.02
        origin=next(o for o in report['config']['origins'] if o['id']==b['origin_id'])
        xyz=[origin['normal_coordinate'],b['requested_tangent'],46]
        actual=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',b['pose'])]
        assert len(actual)==6 and math.dist(actual[:3],xyz)<=.01 and abs(actual[3])<=.01 and abs(actual[5])<=.01 and abs((actual[4]-180+180)%360-180)<=.01
        assert 'surfaceprop concrete,' in str(b['surface']) and 'shape type: Mesh,' in str(b['surface'])
    for bracket in report['brackets']:
        on,off=[report['observations'][bracket[key]['observation_index']] for key in ['on','off']]
        assert on['hit']==terminal['point'] and off['hit'][0]==544 and off['hit'][2]==110
    assert any(o['hit']==terminal['point'] for o in report['observations'])
    assert any(a['world']==terminal['point'] for g in camera['groups'][1:] for a in g['anchors'])
    uv=project(camera['projection_matrix'],terminal['point']);error=[abs(x-y) for x,y in zip(uv,terminal['observed_pixel'])]
    assert max(error)<=terminal['selection_radius_px']<=1.5
    terminal.update(projected_pixel=uv,pixel_difference=error,capture=checked_capture,native_y_interval_with_print_allowance=[intervals[0][0]-.01,intervals[0][1]+.01])
    terminal['calibrated_source_y_interval_cm']=[v*2.54 for v in terminal['native_y_interval_with_print_allowance']]
    rows=[]
    for report_id in ['ASITE_EAST_UPPER_RETAINING_PREFLIGHT_033','ASITE_EAST_TERMINAL_FIRST_FACE_CHECKS_038']:
        report=next(r for r in architecture['reports'] if r['id']==report_id)
        assert report['status'].startswith('complete;') and report['source_build']=='25640462' and max(report['restore_numeric_errors'])<=.01
        for i in range(0,len(report['observations']),2):
            a,b=report['observations'][i:i+2];assert a['hit']==b['hit'] and a['surface']==b['surface'] and a['pose']==b['pose']
            assert math.dist(b['eye_origin'],b['hit'])>.1 and abs(math.dist(b['eye_origin'],b['hit'])-float(b['rangefinder_reply'].split()[1]))<=.02
            # Remote concrete wall atX544 remains recorded in its source report.
            if not 1270<=b['hit'][0]<=1330:continue
            if any(row['point']==b['hit'] and row.get('surface')==b['surface'] for row in rows):continue
            rows.append(dict(id='F'+str(len(rows)+1),point=b['hit'],kind='native first-hit face',surface=b['surface'],report_id=report_id,scope=report['review']))
    for key in ['asite_retaining_cap_review','asite_retaining_terminal_review']:
        selection=profiles[key];assert max(selection['driver_recovery']['restore_numeric_errors'])<=.01
        for case in selection['plan']['cases']:
            report=next(r for r in profiles['reports'] if r['id']==case['id']);pair=[o for o in report['observations'] if o['feature']=='floor'][-2:]
            assert pair[0]['hit']==pair[1]['hit']==samples[case['id']] and max(o['xy_error'] for o in pair)<=.02
            rock='surfaceprop rock,' in str(pair[-1]['hit_description'])
            rows.append(dict(id=('C' if rock else 'G')+str(len(rows)+1),point=samples[case['id']],kind='Rock cap top' if rock else 'outside sand ground',report_id=case['id'],scope=report['surface_semantics']))
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1080">','<rect width="1280" height="1080" fill="#14202e"/>',f'<image y="100" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(image.read_bytes()).decode()}"/>','<g font-family="Arial" fill="white"><text x="25" y="35" font-size="23">A eastern retaining face: calibrated component and elevation context</text><text x="25" y="70" font-size="16">Pink first-hit faces / amber Rock cap tops / cyan outside ground. Unconnected measured points.</text>']
    for row in rows:
        p=row['point'];uv=project(camera['projection_matrix'],p);tested=all(camera['tested_marker_'+axis+'_range'][0]<=p[i]<=camera['tested_marker_'+axis+'_range'][1] for i,axis in enumerate('xyz'))
        row.update(projected_pixel=uv,z_cm=p[2]*2.54,inside_tested_marker_ranges=tested,rendered_correspondence='not accepted from projection alone; ground/cap/cover occlusion requires review')
        color={'native first-hit face':'#ec87ff','Rock cap top':'#ffc75d','outside sand ground':'#49f6e0'}[row['kind']];u,v=uv
        assert 0<u<1280 and 0<v<720
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="{color}" stroke="#14202e"><title>{row["id"]}: native{p}; Z{row["z_cm"]:.4f}cm; tested marker ranges={tested}</title></circle>')
    labels=['SouthZ110: distantMeshX544 atY2296/2300; localMeshX1278.51..1279.24 atY2304..2312.',
        'Cap columns: outsideSandY2296/Z13.44; RockY2304/Z123.51 andY2312/Z124.4.',
        'NorthernRock tops persist throughY2792/Z125.03; Z122 side rays hit RockX1282.81..1282.89.',
        'Rising Longroad hides lowerbody; this visibility join does not define a northern cap/body end.',
        'SouthZ110 corner corroborated within1.5px box; fresh040 holds max0.446016px. GroundZ13.44 extrapolated.',
        'Held camera maximum0.548522px; plane/depth/body selection uncertainty remains separate.',
        'Gate1 FAIL: no fullbody extrusion, hiddenbase or continuous architectural footprint accepted.']
    svg.extend(f'<text x="25" y="{855+i*31}" font-size="15">{label}</text>' for i,label in enumerate(labels));svg.append('</g></svg>')
    (ref/'A_RETAINING_CONTEXT.svg').write_text('\n'.join(svg)+'\n');(ref/'A_RETAINING_CONTEXT.json').write_text(json.dumps(dict(source_build='25640462',camera_id=camera['id'],capture=capture,points=rows,southern_terminal_review=terminal,gate1='FAIL',scope=__doc__),indent=2)+'\n')
    print(len(rows),'unconnected component projections; no full body bounds')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
