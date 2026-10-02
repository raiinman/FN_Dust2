"""Rebuild close terminal floor point-pair rises, not exact contact/landing bounds.

Input: TUNNEL_STAIR_PROFILE terminal_floor_checks and accepted_terminal_pairs.
Outputs: TUNNEL_TERMINAL_CHECKS JSON/CSV/SVG. Physical register consumes six
explicit terminal_rows. Run, render and inspect. Sand crossfall and.20native
selection offsets each side of first/last faces remain explicit.
"""
import base64,csv,hashlib,json,math
from pathlib import Path
from build_tunnel_stair_profile import points
from build_local_camera import project


def terminal_rows(profile,factor):
    actual=points(profile);cases=profile['terminal_floor_checks']['cases'];reports={r['id']:r for r in profile['reports']}
    recovery=profile['terminal_floor_checks']['driver_recovery'];assert recovery['status'].startswith('completed') and max(recovery['restore_numeric_errors'])<=.01
    assert len(cases)==15
    for case in cases:
        pt=actual[case['id']];assert math.dist(pt[:2],case['xy'])<=.02
        o=reports[case['id']]['observations'][-1];ground=case['terminal']=='lower' and case['side']=='BEFORE'
        material='sand' if ground else 'concrete';shape='Mesh' if ground else 'Hull'
        assert ('surfaceprop '+material+',') in str(o['hit_description']) and ('shape type: '+shape+',') in str(o['hit_description'])
        if case['expected_floor_z_native'] is not None:assert abs(pt[2]-case['expected_floor_z_native'])<=.02
    rows=[]
    for pair in profile['accepted_terminal_pairs']:
        a,b=[actual[pair[k]] for k in ('before_report','after_report')];assert .38<=math.dist(a[:2],b[:2])<=.42 and b[2]>a[2]
        rows.append(dict(id=pair['id'],terminal=pair['terminal'],before_report=pair['before_report'],after_report=pair['after_report'],before_z_native=a[2],after_z_native=b[2],sampled_rise_cm=round((b[2]-a[2])*factor,4),xy_sample_separation_cm=round(math.dist(a[:2],b[:2])*factor,4),limits=pair['scope']))
    assert len(rows)==6
    return rows


def build(root):
    ref=root/'reference';profile=json.loads((ref/'TUNNEL_STAIR_PROFILE.json').read_text());scale=json.loads((ref/'SCALE_CALIBRATION.json').read_text());assert scale['status'].startswith('ACCEPTED') and scale['cm_per_source_unit']==2.54
    rows=terminal_rows(profile,2.54)
    (ref/'TUNNEL_TERMINAL_CHECKS.json').write_text(json.dumps(dict(source_build=profile['source_build'],rows=rows,scope=__doc__,gate1='FAIL'),indent=2)+'\n')
    with (ref/'TUNNEL_TERMINAL_CHECKS.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='TUNNEL_STAIR_OVERHEAD_002');assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_TUNSTAIR_CAMERA_FIT_002_CLEAN');image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256'];data=base64.b64encode(image.read_bytes()).decode();pts=points(profile)
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1090">','<rect width="1280" height="1090" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">Tunnel stair terminals /15 close independent floor points</text>','<text x="25" y="65" font-size="17">Orange=sloped sand lower landing / green=concrete tread or upper landing. Actual points only.</text>']
    for case in profile['terminal_floor_checks']['cases']:
        u,v=project(camera['projection_matrix'],pts[case['id']]);assert 4<u<1276 and 4<v<716
        color='#ffb45e' if case['terminal']=='lower' and case['side']=='BEFORE' else '#70df77'
        svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="{color}" stroke="#14202e"/>')
    for i,r in enumerate(rows):
        svg.append(f'<text x="{25+(i//3)*635}" y="{855+(i%3)*30}" font-size="16">{r["id"].replace("TUNNEL_CLOSE_","")} / {r["before_z_native"]:+.2f} to {r["after_z_native"]:+.2f} / {r["sampled_rise_cm"]:.4f}cm</text>')
    svg.extend(['<text x="25" y="978" font-size="16">Samples.20native each side of measured first/last face; sand entry crossfall varies the sampled first rise.</text>','<text x="25" y="1012" font-size="16">Wider camera max.3444px; lowest ground point extrapolates1.82native below synthetic marker range.</text>','<text x="25" y="1046" font-size="16">No exact coincident contact, full side/landing footprint or unseen continuous floor/rendered-offset acceptance. Gate1 FAIL.</text></g></svg>'])
    (ref/'TUNNEL_TERMINAL_CHECKS.svg').write_text('\n'.join(svg)+'\n');print('15 terminal points /6 sampled rises',[(r['id'],r['sampled_rise_cm']) for r in rows])


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
