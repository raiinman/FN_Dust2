"""Derive separate sampled Xbox cover top and adjacent rock-cap profiles."""
import csv,json
from pathlib import Path
from build_connector_profile import points

def build(root):
    ref=root/'reference';spec=json.loads((ref/'XBOX_UPPER_JOINT_PROFILE.json').read_text());data=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());p=points(data);reports={r['id']:r for r in data['reports']};assert spec['source_build']==data['source_build'];rows=[]
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="850" viewBox="0 0 1400 850">','<rect width="1400" height="850" fill="#12202b"/>','<g fill="#edf4f8" font-family="Arial">','<text x="35" y="38" font-size="24">Xbox eastern upper join — separate repeated first-surface supports</text>','<text x="35" y="70" font-size="16">Build25640462 · 2.54cm/native · plastic Mesh cover top and Rock Hull raised masonry</text>']
    for n,g in enumerate(spec['groups']):
        left=50+n*680;sx=lambda x:left+80+(x+282)*14;sy=lambda z:570-(z+40)*5
        parts.append(f'<text x="{left}" y="115" font-size="20">Y{g["source_y"]*2.54/100:.3f}m · local transverse samples</text>')
        for z in [-40,-20,0,20,40]:parts.append(f'<path d="M{left+75},{sy(z)}h500" stroke="#415765"/><text x="{left}" y="{sy(z)+5}" font-size="13">Z{z*2.54/100:+.3f}m</text>')
        for component,key,color in [('plastic_cover','cover_reports','#6bd4b2'),('rock_support','rock_reports','#e9ba73')]:
            selected=[]
            for ident in g[key]:
                point=p[ident];assert point[1]==g['source_y'];r=reports[ident];description=str([o for o in r['observations'] if o['feature']=='floor'][-1]['hit_description']);assert ('surfaceprop plastic,' in description and 'shape type: Mesh' in description) if component=='plastic_cover' else ('surfaceprop rock,' in description and 'shape type: Hull' in description)
                selected.append(point);rows.append(dict(group=g['id'],component=component,report=ident,x_native=point[0],y_native=point[1],z_native=point[2],x_cm=point[0]*2.54,y_cm=point[1]*2.54,z_cm=round(point[2]*2.54,4),confidence='confirmed repeated selected first support',limits=g['scope']))
                parts.append(f'<circle cx="{sx(point[0]):.2f}" cy="{sy(point[2]):.2f}" r="4" fill="{color}"><title>{ident}; native{point}</title></circle>')
            parts.append('<polyline points="'+' '.join(f'{sx(t[0]):.2f},{sy(t[2]):.2f}' for t in selected)+f'" fill="none" stroke="{color}" stroke-dasharray="4 4"/>')
        a,b=g['material_transition_x_interval_native'];assert 0<b-a<=2.02
        parts.append(f'<rect x="{sx(a):.2f}" y="{sy(40)}" width="{(b-a)*14:.2f}" height="{sy(-40)-sy(40)}" fill="#bd9bea" opacity=".2"/>')
        parts.append(f'<text x="{left}" y="620" font-size="15">First-hit transition bracket: {(b-a)*2.54:.4f}cm in X</text>')
        parts.append(f'<text x="{left}" y="649" font-size="14">Source X interval[{a},{b}]; neither hidden body nor constant cap.</text>')
    parts+=['<text x="35" y="705" font-size="16">Green: plastic top. Gold: rock support. Purple: bracket between nearest unlike first-hit samples.</text>','<text x="35" y="738" font-size="16">Dashed links connect same-component sample order only; no interpolation across the material/elevation break.</text>','<text x="35" y="771" font-size="16">Point-pair rise is adjacent support elevation difference, never exact vertical face height or unseen cover bbox.</text>','<text x="35" y="815" font-size="16">Gate1 FAIL. Complete cover envelope, footprint and bounded rendered offsets remain separate.</text>','</g></svg>']
    with (ref/'XBOX_UPPER_JOINT_SAMPLES.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    (ref/'XBOX_UPPER_JOINT_PROFILE.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8');print(len(rows),'reviewed separate cover/rock support points; two local transition brackets')

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
