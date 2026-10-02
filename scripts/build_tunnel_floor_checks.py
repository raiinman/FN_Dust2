"""Rebuild fresh winder floor checks against predeclared tread heights.

Inputs: TUNNEL_STAIR_PROFILE fresh_winder_floor_holds and checked local camera.
Outputs: TUNNEL_WINDER_FLOOR_CHECKS.csv/JSON/SVG. Run and render/inspect the SVG.
Four local checked points per tread do not certify unseen floor interpolation,
complete tread side/terminal bounds or exact rendered/collision correspondence.
"""
import base64,csv,hashlib,json,math
from pathlib import Path
from build_tunnel_stair_profile import points
from build_local_camera import project


def build(root):
    ref=root/'reference';profile=json.loads((ref/'TUNNEL_STAIR_PROFILE.json').read_text())
    calibration=json.loads((ref/'SCALE_CALIBRATION.json').read_text())
    assert calibration['status'].startswith('ACCEPTED') and calibration['cm_per_source_unit']==2.54
    register=profile['fresh_winder_floor_holds'];actual=points(profile)
    assert register['driver_recovery']['status'].startswith('completed') and max(register['driver_recovery']['restore_numeric_errors'])<=.01
    cases=register['cases'];assert len(cases)==48
    reports={r['id']:r for r in profile['reports']};fresh={c['id'] for c in cases};rows=[]
    for case in cases:
        report=reports[case['id']];point=actual[case['id']]
        samples=[o for o in report['observations'] if o['feature']=='floor'][-2:]
        assert samples[0]['hit_description']==samples[1]['hit_description']
        assert 'surfaceprop concrete,' in str(samples[1]['hit_description']) and 'shape type: Hull,' in str(samples[1]['hit_description'])
        assert math.dist(point[:2],case['xy'])<=.02
        expected=case['expected_floor_z_native'];error=point[2]-expected
        assert abs(error)<=case['maximum_predicted_floor_residual_native']==.02
        # This link corroborates the predeclared scalar in the old register;
        # it does not retroactively select a new prediction from fresh checks.
        old=[r for id,r in reports.items() if id not in fresh and abs(actual[id][2]-expected)<.005]
        assert old
        basis=min(old,key=lambda r:math.dist(actual[r['id']][:2],case['xy']))
        rows.append(dict(id=case['id'],sector=case['sector'],selection_type=case['id'].split('_',3)[3].replace('_FLOOR_001',''),source_x=point[0],source_y=point[1],source_z=point[2],x_cm=round(point[0]*2.54,4),y_cm=round(point[1]*2.54,4),z_cm=round(point[2]*2.54,4),predicted_z_native=expected,observed_residual_native=error,old_scalar_basis_report=basis['id'],confidence='confirmed repeated local collision-floor point; prospective scalar-height check',limits=__doc__))
    assert max(abs(r['observed_residual_native']) for r in rows)==register['maximum_observed_floor_residual_native']
    (ref/'TUNNEL_WINDER_FLOOR_CHECKS.json').write_text(json.dumps(dict(source_build=profile['source_build'],plan_sha256=register['plan_sha256'],checks=rows,maximum_observed_residual_native=max(abs(r['observed_residual_native']) for r in rows),gate1='FAIL',limits=__doc__),indent=2)+'\n')
    with (ref/'TUNNEL_WINDER_FLOOR_CHECKS.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='TUNNEL_STAIR_OVERHEAD_002')
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_TUNSTAIR_CAMERA_FIT_002_CLEAN')
    image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    data=base64.b64encode(image.read_bytes()).decode()
    colors={'INNER':'#39e5cd','OUTER':'#ffb45e','ANGLE_LOW':'#eac5ff','ANGLE_HIGH':'#70df77'}
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1040">','<rect width="1280" height="1040" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">Tunnel winder /48 fresh lateral and angular floor checks</text>','<text x="25" y="65" font-size="17">Cyan=inner / orange=outer / purple=lower angle / green=higher angle. Native point projections only.</text>']
    for row in rows:
        u,v=project(camera['projection_matrix'],[row['source_x'],row['source_y'],row['source_z']]);color=colors[row['selection_type']]
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="{color}" stroke="#14202e" stroke-width="1"/>')
    for sector in range(1,13):
        group=[r for r in rows if r['sector']==sector];assert len(group)==4
        z=group[0]['predicted_z_native'];assert all(r['predicted_z_native']==z for r in group)
        col=(sector-1)//4;line=(sector-1)%4
        svg.append(f'<text x="{25+col*420}" y="{850+line*26}" font-size="16">S{sector:02} / nativeZ{z:+.2f} /4pts / max delta0.00</text>')
    svg.extend([f'<text x="25" y="985" font-size="16">{len(actual)} total stair floor points. Printed native heights repeat; no unseen flat-plane or complete side/terminal acceptance.</text>','<text x="25" y="1015" font-size="16">Wider checked camera max.3444px. Point projection does not grant rendered offsets or full footprint. Gate1 FAIL.</text></g></svg>'])
    (ref/'TUNNEL_WINDER_FLOOR_CHECKS.svg').write_text('\n'.join(svg)+'\n')
    print(f'48 prospective floor checks pass;{len(actual)} stair points; no continuous floor acceptance')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
