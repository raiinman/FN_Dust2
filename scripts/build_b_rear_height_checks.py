"""Validate unchanged B rear height predictions and derive diagnostic artifacts.

Inputs: ARCHITECTURAL_ENDPOINTS reports008/009/011/013 and checked B_REAR_FRONTAL_001 camera.
Outputs: B_REAR_HEIGHT_CHECKS JSON/CSV/SVG. Rebuild, render and inspect. Retain
failed prospective predictions, remote first hits and exact restoration. A
passing sampled prediction never certifies unseen wall extrusion or full body.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path
from build_local_camera import project


def upper_rows(ref):
    data=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    rows=[]
    for report in data['reports']:
        selections=report.get('accepted_local_upper_interfaces',[])
        if not selections:continue
        assert report['status'].startswith('complete;') and max(report['restore_numeric_errors'])<=.01
        config=report['config'];assert config['normal_axis']==1 and config['tangent_axis']==2
        obs=report['observations']
        for i in range(0,len(obs),2):
            a,b=obs[i:i+2];assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface']
            for o in (a,b):
                native=float(re.search(r'DISTANCE:\s+([0-9.]+) inches',o['rangefinder_reply']).group(1))
                assert native>.1 and abs(math.dist(o['eye_origin'],o['hit'])-native)<.02
        for selection in selections:
            brackets=[b for b in report['brackets'] if b['origin_id'] in selection['origin_ids']]
            assert len(brackets)==2 and brackets[0]['tangent_interval_native']==brackets[1]['tangent_interval_native']
            lo,hi=brackets[0]['tangent_interval_native'];assert hi-lo<=.1
            for bracket in brackets:
                on,off=[obs[bracket[k]['observation_index']] for k in ('on','off')]
                assert on['hit'][0]==off['hit'][0]==selection['x_native']
                assert abs(on['hit'][1]-selection['y_native'])<=.02 and off['hit'][1]-on['hit'][1]>selection.get('minimum_recessed_depth_native',100)
                for o,role in ((on,'on'),(off,'off')):
                    assert 'surfaceprop '+config[role+'_material']+',' in str(o['surface']) and 'shape type: '+config[role+'_shape']+',' in str(o['surface'])
            rows.append(dict(id=selection['id'],source_x=selection['x_native'],source_y=selection['y_native'],elevation_interval_native=[lo-.01,hi+.01],elevation_interval_cm=[(lo-.01)*2.54,(hi+.01)*2.54],native_point=[selection['x_native'],selection['y_native'],(lo+hi)/2],render_review=selection['render_review'],source_report=report['id'],limits='Local first-hit concrete face upper termination only; absolute sourceZ0 elevation, not floor-to-roof height, full wall or hidden body. Independent source origins agree; numerical bound includes.01native allowance.'))
    return rows


def measurement_rows(ref):
    rows=[]
    for r in upper_rows(ref):
        lo,hi=r['elevation_interval_cm']
        rows.append(dict(id=r['id'],area='B Site',feature=f'Local B rear concrete face upper termination at sourceX{r["source_x"]}',value=(lo+hi)/2,unit='cm',method='two agreeing independent-origin repeated first-face upper-interface brackets; SCALE_CALIBRATION',source_id='ARCHITECTURAL_ENDPOINTS/'+r['source_report']+'/'+r['id'],confidence='confirmed bounded local collision-face termination',tolerance=f'Native numerical elevation interval [{lo:.7f},{hi:.7f}]cm; rendered correspondence '+r['render_review']['status'],notes=r['limits']))
    return rows


def build(root):
    ref=root/'reference';data=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    report=next(r for r in data['reports'] if r['id']=='B_REAR_HEIGHT_CHECKS_008')
    assert report['status'].startswith('complete;') and max(report['restore_numeric_errors'])<=.01
    predictions={q['station_id']:q for q in report['config']['predeclared_predictions']}
    rows=[]
    for i in range(0,len(report['observations']),2):
        a,b=report['observations'][i:i+2]
        assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface']
        assert 'surfaceprop concrete,' in str(a['surface']) and 'shape type: Mesh,' in str(a['surface'])
        for o in (a,b):
            native=float(re.search(r'DISTANCE:\s+([0-9.]+) inches',o['rangefinder_reply']).group(1))
            assert native>.1 and abs(math.dist(o['eye_origin'],o['hit'])-native)<.02
        q=predictions[a['station_id']];error=math.dist(q['predicted_endpoint'],a['hit'])
        rows.append(dict(station_id=a['station_id'],observation_index=i,source_x=a['hit'][0],source_y=a['hit'][1],source_z=a['hit'][2],predicted_x=q['predicted_endpoint'][0],predicted_y=q['predicted_endpoint'][1],predicted_z=q['predicted_endpoint'][2],error_native=error,error_cm=error*2.54,threshold_native=q['predeclared_maximum_error_native'],prediction_result='PASS' if error<=q['predeclared_maximum_error_native'] else 'REJECT',interpretation='local first-hit sample; unseen extrusion unaccepted'))
    assert len(rows)==16 and sum(r['prediction_result']=='PASS' for r in rows)==12
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='B_REAR_FRONTAL_001')
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_B_REAR_CAMERA_FIT_001_CLEAN')
    image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    for row in rows:
        row['inside_camera_checked_depth']=camera['tested_marker_y_range'][0]<=row['source_y']<=camera['tested_marker_y_range'][1]
    upper=upper_rows(ref)
    for r in upper:
        assert camera['tested_marker_z_range'][0]<=r['native_point'][2]<=camera['tested_marker_z_range'][1]
        review=r['render_review']
        if review['status'].startswith('PASS'):
            assert review['camera_id']==camera['id'] and review['image_path']==capture['repository_image_path']
            assert math.dist(project(camera['projection_matrix'],r['native_point']),review['pixel'])<=review['pixel_radius']
    result=dict(source_build='25640462',report_id=report['id'],camera_id=camera['id'],checked_points=rows,local_upper_interfaces=upper,passed=12,rejected=4,gate1='FAIL',scope=__doc__)
    (ref/'B_REAR_HEIGHT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ref/'B_REAR_HEIGHT_CHECKS.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    encoded=base64.b64encode(image.read_bytes()).decode()
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1600">','<rect width="1280" height="1600" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{encoded}"/>','<g fill="white" font-family="sans-serif"><text x="25" y="32" font-size="24">B rear height checks / unchanged prospective models</text>','<text x="25" y="65" font-size="17">12 PASS /4 REJECT against predeclared1native tolerance. Green=pass; red=reject; hollow=prediction.</text>']
    for row in rows:
        color='#48e0bc' if row['prediction_result']=='PASS' else '#ff978b'
        u,v=project(camera['projection_matrix'],[row[k] for k in ('predicted_x','predicted_y','predicted_z')])
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="7" fill="none" stroke="{color}" stroke-width="2"/>')
        if row['inside_camera_checked_depth']:
            u,v=project(camera['projection_matrix'],[row[k] for k in ('source_x','source_y','source_z')])
            svg.append(f'<circle cx="{u}" cy="{v+100}" r="3" fill="{color}"/>')
    for i,r in enumerate(upper):
        u,v=project(camera['projection_matrix'],r['native_point']);color='#ffe080'
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="6" fill="none" stroke="{color}" stroke-width="2"/>')
        lo,hi=r['elevation_interval_cm']
        label='local cap-band only; exact seam unresolved' if 'cap-band' in r['render_review']['status'] else r['render_review']['status']
        svg.append(f'<text x="25" y="{1245+i*40}" font-size="18" fill="{color}">X{r["source_x"]} upper first-face elevation [{lo:.5f},{hi:.5f}]cm; {label}.</text>')
    svg.extend(['<text x="25" y="865" font-size="19">Two easternZ220 rays pass above local return and hit distantY3088.01. Remote hits listed numerically.</text>','<text x="25" y="905" font-size="18">WestY2890: Z80 differs1.26native (3.2004cm); Z160 differs1.39native (3.5306cm) from oldZ104 relief.</text>','<text x="25" y="945" font-size="18">WestY2910: .64/.63native differences pass original1native threshold; no exact common vertical plane.</text>','<text x="25" y="985" font-size="18">Central front samples remain nearY2880 atZ80/160/220; east lower samples agree atZ80/160.</text>','<text x="25" y="1025" font-size="18">FartherZ220 hits lie outside camera checkedY2800..2950, so their actual projections are omitted.</text>','<text x="25" y="1065" font-size="18">All32 native observations repeated; rangefinder crosschecks pass; exact B-mouth restoration verified.</text>','<text x="25" y="1105" font-size="18">Observed collision points and hollow model predictions are diagnostic, not rendered corner selections.</text>','<text x="25" y="1145" font-size="18">Full roof/wall extent, hidden body, floor polygon and continuous footprint remain unaccepted.</text>','<text x="25" y="1195" font-size="18">Yellow:160 additional repeated observations bracket four local upper interfaces; independent origins agree.</text>','<text x="25" y="1470" font-size="18">Elevations relative nativeZ0; no inferred floor-to-top heights. Palm overlap remains unresolved atX-1496.</text>','<text x="25" y="1540" font-size="18">No production geometry. Gate1 FAIL.</text></g></svg>'])
    (ref/'B_REAR_HEIGHT_CHECKS.svg').write_text('\n'.join(svg)+'\n')
    print('16 unchanged-model height checks /12 PASS /4 REJECT')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
