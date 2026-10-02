"""Derive axis-flat native wall candidates with independent midpoint checks.

PLAN_SECTION_SWEEPS supplies repeated endpoints; PLAN_SECTION_CHECKS supplies
fresh independent directions. A local agreement never supplies unseen corners,
component identity, rendered offsets or complete footprint acceptance.
"""
import base64,csv,hashlib,json,math
from html import escape
from pathlib import Path

def build(root):
    ref=root/'reference';source=json.loads((ref/'PLAN_SECTION_SWEEPS.json').read_text());checks=json.loads((ref/'PLAN_SECTION_CHECKS.json').read_text());models={m['baseline_report']['id']:m for m in checks['models']}
    camera=json.loads((ref/'MAP_CAMERA_CALIBRATION.json').read_text());P=camera['projection_matrix'];clean=next(c for c in camera['captures'] if c['id']=='QA_MAP_CAMERA_002_CLEAN');image=root/clean['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==clean['jpeg_sha256']
    assert max(g['maximum_residual_px'] for g in camera['groups'])<1
    def project(point):
        assert -100<=point[2]<=1000
        values=[sum(t*v for t,v in zip(row,point+[1])) for row in P];assert values[2]>0
        return [40+values[0]/values[2],95+values[1]/values[2]]
    rows=[];candidates=[];areas={}
    for report in source['reports']:
        observations={o['yaw']:o for o in report['observations'] if o['repeat']==2};angles=sorted(observations);station=report['config']['stations'][0]
        for yaw,o in observations.items():
            repeats=[p for p in report['observations'] if p['yaw']==yaw];assert len(repeats)==2 and repeats[0]['hit']==repeats[1]['hit'] and repeats[0]['surface']==repeats[1]['surface']
        for i,yaw in enumerate(angles):
            next_yaw=angles[(i+1)%len(angles)]
            if abs((next_yaw-yaw)%360-11.25)>.001:continue
            a,b=observations[yaw],observations[next_yaw]
            if not all('surfaceprop concrete,' in str(o['surface']) for o in [a,b]):continue
            for axis in [0,1]:
                if abs(a['hit'][axis]-b['hit'][axis])>.02 or math.dist(a['hit'],b['hit'])<10:continue
                midpoint=(yaw+5.625)%360;model=models.get(report['id']);check=None
                if model:
                    assert model['baseline_report']==report
                    obs=[o for o in model['check_report']['observations'] if o['yaw']==midpoint]
                    if obs:
                        assert len(obs)==2 and obs[0]['hit']==obs[1]['hit'] and obs[0]['surface']==obs[1]['surface'];check=obs[1]
                error=abs(check['hit'][axis]-(a['hit'][axis]+b['hit'][axis])/2) if check else None
                result='unexecuted independent check' if check is None else ('agrees at checked point only' if error<=checks['local_agreement_threshold_native'] else 'candidate axis line rejected')
                ident=f'AXIS_CANDIDATE_{report["area"]}_{yaw}_{axis}'
                candidate=dict(id=ident,source_report=report['id'],area=report['area'],source_pose=station['pose'],axis=axis,from_yaw=yaw,to_yaw=next_yaw,from_point=a['hit'],to_point=b['hit'],midpoint_yaw=midpoint,check_report=model['check_report']['id'] if check else None,check=check,check_axis_error_native=error,result=result,architectural_component='unreviewed; concrete material alone does not establish wall/cover/graded-floor identity')
                candidates.append(candidate);areas.setdefault(report['area'],station['pose'])
                rows.append(dict(id=ident,area=report['area'],source_report=report['id'],axis='XY'[axis],ray_z_cm=a['hit'][2]*2.54,from_native=str(a['hit']),to_native=str(b['hit']),sampled_endpoint_chord_cm=round(math.dist(a['hit'],b['hit'])*2.54,4),check_report=candidate['check_report'] or '',check_yaw=midpoint,check_axis_error_cm=round(error*2.54,6) if error is not None else '',result=result,limits='Local candidate only; midpoint agreement does not locate exact ends, close angular gaps, identify component or certify continuous architectural footprint.'))
    assert candidates and len({c['id'] for c in candidates})==len(candidates)
    data=dict(source_build=source['source_build'],status='Native axis-line validation candidates; no architectural boundary acceptance',diagnostic_axis_agreement_threshold_native=checks['local_agreement_threshold_native'],accepted_boundaries=[],candidates=candidates)
    (ref/'WALL_BOUNDARY_CHECKS.json').write_text(json.dumps(data,indent=2)+'\n')
    with (ref/'WALL_BOUNDARY_CHECKS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1190" viewBox="0 0 1440 1190">','<rect width="1440" height="1190" fill="#101923"/>','<g fill="#edf3f8" font-family="Arial"><text x="40" y="40" font-size="25">Dust II — independent native wall-line checks</text><text x="40" y="68" font-size="16">Calibrated overhead camera · exact ray elevations · candidate segments, never accepted footprint boundaries</text></g>',f'<image x="40" y="95" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(image.read_bytes()).decode()}"/>']
    for c in candidates:
        a,b=[project(c[k]) for k in ['from_point','to_point']];color='#ff6677' if 'rejected' in c['result'] else ('#78ef9b' if c['check'] else '#c7d4e0')
        label=escape(c['id']+'; '+c['result']+'; '+c['architectural_component'])
        parts.append(f'<path d="M{a[0]:.3f},{a[1]:.3f}L{b[0]:.3f},{b[1]:.3f}" fill="none" stroke="#071018" stroke-width="4"/><path d="M{a[0]:.3f},{a[1]:.3f}L{b[0]:.3f},{b[1]:.3f}" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="4 3"><title>{label}</title></path>')
        if c['check']:
            u,v=project(c['check']['hit']);parts.append(f'<circle cx="{u:.3f}" cy="{v:.3f}" r="2.2" fill="{color}" stroke="#071018"/>')
    for i,(area,pose) in enumerate(areas.items(),1):
        u,v=project([pose[0],pose[1],pose[2]+64]);parts.append(f'<circle cx="{u}" cy="{v}" r="9" fill="#071018" stroke="#ffe48b"/><text x="{u}" y="{v+4}" text-anchor="middle" fill="#fff" font-family="Arial" font-size="12">{i}</text>')
        x=40+(i-1)//9*680;y=846+(i-1)%9*23;rr=[c for c in candidates if c['area']==area];checked=sum(c['check'] is not None for c in rr)
        parts.append(f'<text x="{x}" y="{y}" fill="#edf3f8" font-family="Arial" font-size="14">{i}. {escape(area)} · rayZ{(pose[2]+64)*2.54/100:+.3f}m · {checked}/{len(rr)} midpoint checks</text>')
    parts+=['<g fill="#edf3f8" font-family="Arial" font-size="16">','<text x="40" y="1080">Green: checked point agrees. Red: line rejected. Gray: check unexecuted. Hover for IDs; exact values are in CSV.</text>','<text x="40" y="1110">Roof/cover occlusion, portals, unseen corners and render/collision offsets remain separate from camera calibration.</text>','<text x="40" y="1140">No polygon closure or full wall extents inferred. Ray-height labels are not surveyed floor-story boundaries.</text>','<text x="40" y="1170">Gate1 FAIL: semantic boundary/end-point review and continuous layered footprint remain incomplete.</text>','</g></svg>']
    (ref/'WALL_BOUNDARY_CHECKS.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8');print(len(candidates),'candidate lines;',sum(c['check'] is not None for c in candidates),'independent checks; no boundaries accepted')

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
