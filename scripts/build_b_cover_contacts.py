"""Validate local B ground/first-Wood interfaces and selected top differences."""
import csv,json,math
from pathlib import Path


def sections(ref):
    spec=json.loads((ref/'B_COVER_CONTACT_REVIEW.json').read_text());reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']};tops={r['id']:r for r in json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text())['reports']};rows=[];padding=spec['numerical_allowance_native'];assert padding==.01
    for selection in spec['selections']:
        r=reports[selection['report']];assert r['source_build']==spec['source_build'] and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01
        c=r['config'];assert c['normal_axis']==0 and c['tangent_axis']==2 and c['maximum_bracket_native']<=.1
        assert len(r['brackets'])==2 and r['brackets'][0]['tangent_interval_native']==r['brackets'][1]['tangent_interval_native'] and len({o['normal_coordinate'] for o in c['origins']})==2
        interface=r['brackets'][0]['tangent_interval_native'];assert interface[1]-interface[0]<=.1;on_points=[];off_points=[]
        for bracket in r['brackets']:
            origin=next(o for o in c['origins'] if o['id']==bracket['origin_id'])
            for role,target,material,shape in [('on',on_points,'Wood_Plank','Hull'),('off',off_points,'concrete','Mesh')]:
                assert bracket[role]['on_component']==(role=='on');index=bracket[role]['observation_index'];a,b=r['observations'][index-1:index+1];assert a['repeat']==1 and b['repeat']==2 and a['hit']==b['hit'] and a['surface']==b['surface']
                assert 'surfaceprop '+material+',' in str(b['surface']) and 'shape type: '+shape+',' in str(b['surface'])
                assert abs(float(b['rangefinder_reply'].split()[1])-math.dist(b['eye_origin'],b['hit']))<=.02
                if role=='on':assert origin['on_normal_band'][0]<=b['hit'][0]<=origin['on_normal_band'][1]
                else:assert b['hit'][0]>origin['on_normal_band'][1]
                target.append(b['hit'])
        assert on_points[0]==on_points[1] and off_points[0]==off_points[1]
        top=tops[selection['top_report']];samples=[o for o in top['observations'] if o['feature']=='floor'][-2:];point=top['endpoints']['floor'];assert top['source_build']==spec['source_build'] and top['status'].startswith('complete;') and len(samples)==2 and all(o['xy_error']<=.02 for o in samples)
        assert math.dist(point[:2],top['target_xy'])<=.02 and samples[0]['hit']==samples[1]['hit']==point and 'surfaceprop Wood_Plank,' in str(samples[1]['hit_description']) and 'shape type: Hull,' in str(samples[1]['hit_description'])
        assert point[1]==on_points[0][1]==off_points[0][1] and abs(point[0]-on_points[0][0])<25
        bounds=[(point[2]-interface[1]-2*padding)*2.54,(point[2]-interface[0]+2*padding)*2.54]
        rows.append(dict(**selection,native_y=point[1],selected_top=point,ground_first=off_points[0],wood_first=on_points[0],interface_native_z=interface,height_interval_cm=bounds,value_cm=sum(bounds)/2,scope=spec['scope']))
    return rows


def measurement_rows(ref):
    return [dict(id=r['id'],area='B Site',feature=r['feature'],value=round(r['value_cm'],4),unit='cm',method='two independent outside origins, repeated concrete-ground/first-Wood height brackets plus selected repeated covered top; SCALE_CALIBRATION',source_id='B_COVER_CONTACT_SECTIONS/'+r['id'],confidence='confirmed bounded local different-X height comparison',tolerance=f"Numerical interval[{r['height_interval_cm'][0]:.4f},{r['height_interval_cm'][1]:.4f}]cm; .01native printed-endpoint allowance each end; full body/render limits separate",notes=r['scope']) for r in sections(ref)]


def build(root):
    ref=root/'reference';rows=sections(ref);(ref/'B_COVER_CONTACT_SECTIONS.json').write_text(json.dumps(dict(source_build='25640462',sections=rows,gate1='FAIL'),indent=2)+'\n')
    with (ref/'B_COVER_CONTACT_SECTIONS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['id','native_y','interface_low_native_z','interface_high_native_z','selected_top_native_z','height_low_cm','height_high_cm','scope'])
        for r in rows:w.writerow([r['id'],r['native_y'],*r['interface_native_z'],r['selected_top'][2],*r['height_interval_cm'],r['scope']])
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="890" viewBox="0 0 1400 890">','<rect width="1400" height="890" fill="#14202e"/><g font-family="Arial" fill="white">','<text x="30" y="40" font-size="25">B covered mass / two local top-to-visible-ground sections</text>','<text x="30" y="75" font-size="17">Independent source origins agree. Graded ground contacts differ byY; no uniform cover or hidden base. Gate1 FAIL.</text>']
    for n,r in enumerate(rows):
        left=40+n*690;sx=lambda x:left+100+(x+1790)*10;sy=lambda z:660-z*4.4
        svg.append(f'<text x="{left}" y="140" font-size="22">NativeY{r["native_y"]:.0f}</text><text x="{left}" y="174" font-size="17">Bounded local difference{r["height_interval_cm"][0]:.3f}..{r["height_interval_cm"][1]:.3f}cm</text>')
        for z in [0,25,50,75,100]:svg.append(f'<path d="M{left+75},{sy(z)}h450" stroke="#506477"/><text x="{left}" y="{sy(z)+5}" font-size="14">Z{z}</text>')
        for key,color in [('selected_top','#60e4cb'),('ground_first','#bb9cff'),('wood_first','#ffbf69')]:
            p=r[key];svg.append(f'<circle cx="{sx(p[0])}" cy="{sy(p[2])}" r="5" fill="{color}"/><text x="{sx(p[0])-100}" y="{sy(p[2])-15 if key != "ground_first" else sy(p[2])+25}" font-size="14" fill="{color}">{key} X{p[0]:.2f}/Z{p[2]:.2f}</text>')
        svg.append(f'<text x="{left}" y="724" font-size="16">Visibility intervalZ[{r["interface_native_z"][0]},{r["interface_native_z"][1]}]</text>')
    svg.extend(['<text x="30" y="778" font-size="16">NativeXZ point sections. Top samples are within25native X of contact, at the sameY; no connecting body surface fitted.</text>','<text x="30" y="812" font-size="16">Purple: nearer concrete ground. Amber: covered Wood_Plank Hull first hit. Green: selected covered top.</text>','<text x="30" y="846" font-size="16">Ground hides lower timber. These bounds do not measure hidden underside, full roof/cover envelope or rendered cloth seam.</text></g></svg>'])
    (ref/'B_COVER_CONTACT_SECTIONS.svg').write_text('\n'.join(svg)+'\n');print([(r['id'],r['height_interval_cm']) for r in rows])


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
