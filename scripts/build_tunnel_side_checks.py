"""Rebuild independently checked tunnel winder side-point diagnostics.

Input: reviewed ARCHITECTURAL_ENDPOINTS fresh angle/height reports and their
fixed-before-capture circle predictions; TUNNEL_STAIR_PROFILE radial baseline;
checked TUNNEL_STAIR_OVERHEAD_001 camera. Output: TUNNEL_WINDER_SIDE_CHECKS
JSON/CSV/SVG. Run this script, then render/inspect the SVG. Sample residuals
do not certify unseen cylindrical walls, full sides/ends or a closed footprint.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path
from build_local_camera import project


def build(root):
    ref=root/'reference'
    data=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    reports={r['id']:r for r in data['reports']}
    baseline=json.loads((ref/'TUNNEL_STAIR_PROFILE.json').read_text())['radial_widths']
    rows=[];models=None
    for id in ('TUNNEL_WINDER_FRESH_ANGLE_SIDE_CHECKS_002','TUNNEL_WINDER_FIXED_HEIGHT_SIDE_CHECKS_003'):
        report=reports[id]
        assert report['status'].startswith('complete;') and max(report['restore_numeric_errors'])<=.01
        predictions=report['predictions_fixed_before_capture']
        if models is None:models=predictions['models']
        assert predictions['models']==models
        for check in predictions['predictions']:
            samples=[o for o in report['observations'] if o['station_id']==check['station_id'] and o['yaw']==check['yaw']]
            assert len(samples)==2 and samples[0]['hit']==samples[1]['hit'] and samples[0]['surface']==samples[1]['surface']
            o=samples[0];model=next(m for m in models if m['side']==check['side'])
            eye=o['eye_origin'];angle=math.radians(check['yaw']);direction=[math.cos(angle),math.sin(angle)]
            offset=[eye[i]-model['center_xy'][i] for i in range(2)]
            b=sum(offset[i]*direction[i] for i in range(2));c=sum(x*x for x in offset)-model['radius_native']**2
            disc=b*b-c;assert disc>0
            distance=min(t for t in (-b-math.sqrt(disc),-b+math.sqrt(disc)) if t>.1)
            predicted=[eye[i]+distance*direction[i] for i in range(2)]+[eye[2]]
            assert math.dist(predicted,check['predicted_endpoint'])<.00001
            measured=float(re.search(r'DISTANCE:\s+([0-9.]+) inches',o['rangefinder_reply']).group(1))
            assert abs(math.dist(eye,o['hit'])-measured)<.02
            error=math.dist(o['hit'],predicted)
            component=('surfaceprop '+check['expected_material']+',') in str(o['surface']) and ('shape type: '+check['expected_shape']+',') in str(o['surface'])
            stored=next(x for x in report['independent_curve_check_review']['checks'] if x['station_id']==check['station_id'] and x['yaw']==check['yaw'])
            assert abs(error-stored['model_error_native'])<.00001 and component==stored['component_match']
            rows.append(dict(report=id,station=check['station_id'],side=check['side'],sector=check['sector'],source_x=o['hit'][0],source_y=o['hit'][1],source_z=o['hit'][2],predicted_x=predicted[0],predicted_y=predicted[1],prediction_error_cm=error*2.54,predeclared_threshold_cm=check['maximum_predeclared_model_error_native']*2.54,component_match=component,status='point pass' if component and error<=check['maximum_predeclared_model_error_native'] else 'rejected'))
    assert len(rows)==72
    # Retain original three-point fit links and nine baseline withheld points per
    # side. Baseline holds are retrospective; fresh72 remain prospective checks.
    fit_links=[]
    for model in models:
        assert model['fit_sectors']==[1,6,12]
        pts=[]
        for sector in model['fit_sectors']:
            station=baseline['config']['stations'][sector-1];yaw=station['yaws'][0 if model['side']=='outer' else 1]
            obs=[o for o in baseline['observations'] if o['station_id']==station['id'] and o['yaw']==yaw]
            assert len(obs)==2 and obs[0]['hit']==obs[1]['hit']
            p=obs[0]['hit'];assert abs(math.dist(p[:2],model['center_xy'])-model['radius_native'])<.00001
            pts.append(dict(sector=sector,point=p))
        fit_links.append(dict(side=model['side'],fit=pts))
    result=dict(source_build=baseline['source_build'],models=models,original_fit_links=fit_links,fresh_checks=rows,maximum_fresh_error_cm=max(r['prediction_error_cm'] for r in rows),gate1='FAIL',scope=__doc__)
    (ref/'TUNNEL_WINDER_SIDE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ref/'TUNNEL_WINDER_SIDE_CHECKS.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='TUNNEL_STAIR_OVERHEAD_001')
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_TUNSTAIR_CAMERA_FIT_001_CLEAN')
    image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    encoded=base64.b64encode(image.read_bytes()).decode()
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="960">','<rect width="1280" height="960" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{encoded}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">Tunnel winder /72 independent curved-side point checks</text>','<text x="25" y="66" font-size="17">Orange=outer Mesh / cyan=inner Hull. Circles=floor+4; squares=common eyeZ10. No fitted wall outline.</text>']
    outside=0
    for r in rows:
        u,v=project(camera['projection_matrix'],[r['source_x'],r['source_y'],r['source_z']]);color='#ffb45e' if r['side']=='outer' else '#39e5cd'
        if not (4<=u<=1276 and 4<=v<=716):
            outside+=1
            continue
        if 'FIXED_HEIGHT' in r['report']:svg.append(f'<rect x="{u-3}" y="{v+97}" width="6" height="6" fill="{color}" stroke="#14202e"/>')
        else:svg.append(f'<circle cx="{u}" cy="{v+100}" r="3.5" fill="{color}" stroke="#14202e"/>')
    svg.extend([f'<text x="25" y="856" font-size="17">72/72 fresh component checks pass; max {result["maximum_fresh_error_cm"]:.4f}cm. {outside} off-frame points retained in CSV/JSON.</text>','<text x="25" y="889" font-size="16">Original circles fit only sectors1/6/12;9 other original points per side withheld. Fresh predictions fixed before capture.</text>','<text x="25" y="923" font-size="16">No unseen vertical continuity, complete sides/ends, rendered offset or closed stair/map footprint accepted. Gate1 FAIL.</text></g></svg>'])
    (ref/'TUNNEL_WINDER_SIDE_CHECKS.svg').write_text('\n'.join(svg)+'\n')
    print('72 fresh checks;',sum(r['status']=='rejected' for r in rows),'rejected; max',result['maximum_fresh_error_cm'],'cm')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
