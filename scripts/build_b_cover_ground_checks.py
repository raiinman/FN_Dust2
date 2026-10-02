"""Review fresh B exterior-ground predictions against the unchanged three-point fit."""
import csv,json,math
from pathlib import Path


def build(root):
    ref=root/'reference';profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());spec=profile['b_cover_ground_plane_checks'];plan=spec['plan'];reports={r['id']:r for r in profile['reports']}
    assert len(spec['checks'])==4 and plan['diagnostic_maximum_error_native']==1 and max(spec['driver_recovery']['restore_numeric_errors'])==0
    a,b,c=plan['unchanged_plane_coefficients_native'];assert len(plan['fit_reports'])==3
    for ident,point in zip(plan['fit_reports'],plan['original_fit_points_native']):
        assert reports[ident]['endpoints']['floor']==point and abs(a*point[0]+b*point[1]+c-point[2])<1e-10
    rows=[]
    for case in plan['cases']:
        r=reports[case['id']];samples=[o for o in r['observations'] if o['feature']=='floor'][-2:];point=r['endpoints']['floor'];assert len(samples)==2 and samples[0]['hit']==samples[1]['hit']==point and math.dist(point[:2],case['xy'])<=.02
        predicted=a*point[0]+b*point[1]+c;error=point[2]-predicted;result='PASS point check' if abs(error)<=1 else 'REJECT plane prediction';row=dict(id=case['id'],native_x=point[0],native_y=point[1],actual_native_z=point[2],predicted_native_z=predicted,signed_error_cm=error*2.54,result=result);rows.append(row)
        previous=next(v for v in spec['checks'] if v['report']==case['id']);assert previous['actual']==point and previous['result']==result and abs(previous['error_native']-abs(error))<1e-10
    assert sum(r['result'].startswith('REJECT') for r in rows)==3
    result=dict(source_build=profile['source_build'],original_fit_points_native=plan['original_fit_points_native'],unchanged_plane_coefficients_native=[a,b,c],declared_error_limit_cm=2.54,checks=rows,status='REJECT nearby flat-plane model: three of four independent checks exceed declared limit',scope=spec['scope'],gate1='FAIL')
    (ref/'B_COVER_GROUND_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ref/'B_COVER_GROUND_CHECKS.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="790" viewBox="0 0 1280 790">','<rect width="1280" height="790" fill="#14202e"/><g font-family="Arial" fill="white">','<text x="30" y="40" font-size="25">B covered mass / fresh neighboring-ground plane checks</text>','<text x="30" y="76" font-size="17">Original three-point plane unchanged.1 PASS /3 REJECT; measured ground points retained. Gate1 FAIL.</text>']
    sx=lambda value:780+value*30
    for value in [-5,0,5,10,15]:svg.append(f'<path d="M{sx(value)},140V550" stroke="#506477"/><text x="{sx(value)-15}" y="580" font-size="15">{value}cm</text>')
    for value in [-2.54,2.54]:svg.append(f'<path d="M{sx(value)},140V550" stroke="#ffbf69" stroke-dasharray="5 5"/>')
    for n,row in enumerate(rows):
        yy=190+n*100;color='#60e4cb' if row['result'].startswith('PASS') else '#ff877b';left=min(sx(0),sx(row['signed_error_cm']));width=abs(sx(row['signed_error_cm'])-sx(0));svg.append(f'<text x="30" y="{yy}" font-size="18">X{row["native_x"]:.2f}, Y{row["native_y"]:.0f} / actualZ{row["actual_native_z"]:.2f}</text><text x="30" y="{yy+28}" font-size="16" fill="{color}">{row["result"]}; signed error{row["signed_error_cm"]:+.4f}cm</text><rect x="{left}" y="{yy-14}" width="{width}" height="26" fill="{color}"/>')
    svg.extend(['<text x="30" y="645" font-size="17">Amber lines: predeclared +/-2.54cm threshold. Independent points excluded from original fitting.</text>','<text x="30" y="680" font-size="17">Actual elevations describe graded concrete Mesh outside cover; no uniform neighboring or hidden floor accepted.</text>','<text x="30" y="715" font-size="17">No retrospective refit, threshold widening, exact covered base/contact or whole-platform inference.</text></g></svg>'])
    (ref/'B_COVER_GROUND_CHECKS.svg').write_text('\n'.join(svg)+'\n');print(result['status'],max(abs(r['signed_error_cm']) for r in rows))


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
