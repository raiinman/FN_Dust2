"""Derive reviewed B/Lower stone sections without fitting unseen surfaces.

STONE_PORTAL_PROFILES selects existing repeated columns, opening chords and
outside-origin masonry depths. Dashed links show sample order only.
"""
import csv,json,math
from html import escape
from pathlib import Path

def build(root):
    ref=root/'reference';spec=json.loads((ref/'STONE_PORTAL_PROFILES.json').read_text())
    reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']}
    factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
    rows=[];panels=[]
    for portal in spec['portals']:
        axis=portal['transverse_axis'];normal=1-axis;columns=[];widths=[];depths=[]
        for ident in portal['columns']:
            r=reports[ident];assert r['source_build']==spec['source_build'] and r['status'].startswith('complete') and r.get('accepted_columns')
            floor,top=[r['endpoints'][k] for k in ['floor','ceiling']];assert math.dist(floor[:2],top[:2])<=.04 and top[2]>floor[2]
            assert abs(floor[normal]-portal['section_plane_native'])<=.02
            for feature,point in [('floor',floor),('ceiling',top)]:
                obs=[o for o in r['observations'] if o['feature']==feature];assert obs[-1]['hit']==obs[-2]['hit']==point and obs[-1]['xy_error']<=.02
                description=str(obs[-1]['hit_description']);assert 'surfaceprop concrete,' in description if feature=='ceiling' else 'surfaceprop sand,' in description
            columns.append((floor[axis],floor[2],top[2],ident))
            rows.append(dict(portal=portal['id'],kind='floor_to_intrados_column',source_report=ident,source_feature=r['accepted_columns'][0]['id'],low_native=str(floor),high_native=str(top),value_cm=round((top[2]-floor[2])*factor,4),confidence='confirmed repeated selected collision column',limits=spec['limits']))
        for selection in portal['widths']:
            r=reports[selection['report']];section=next(s for s in r['accepted_sections'] if s['id']==selection['section']);assert section['axis']==axis
            obs=[o for o in r['observations'] if o['station_id']==section['station_id']]
            pairs=[[o for o in obs if o['yaw']==yaw] for yaw in ([180,0] if axis==0 else [-90,90])]
            assert all(len(p)==2 and p[0]['hit']==p[1]['hit'] for p in pairs)
            lo,hi=[p[0]['hit'] for p in pairs];assert lo[axis]<hi[axis] and lo[2]==hi[2] and lo[normal]==hi[normal]==portal['section_plane_native']
            assert all('surfaceprop concrete,' in str(o['surface']) for o in obs)
            widths.append((lo[axis],hi[axis],lo[2],section['id']))
            rows.append(dict(portal=portal['id'],kind='local_opening_chord',source_report=r['id'],source_feature=section['id'],low_native=str(lo),high_native=str(hi),value_cm=round(math.dist(lo,hi)*factor,4),confidence=section['confidence'],limits=spec['limits']))
        for selection in portal['depths']:
            r=reports[selection['report']];span=next(s for s in r['accepted_endpoint_spans'] if s['id']==selection['span']);assert span['axis']==normal
            endpoints=[]
            for side in ['low','high']:
                selector=span[side];obs=[o for o in r['observations'] if o['station_id']==selector['station_id'] and o['yaw']==selector['yaw']]
                assert len(obs)==2 and obs[0]['hit']==obs[1]['hit'] and all('surfaceprop concrete,' in str(o['surface']) for o in obs);endpoints.append(obs[0]['hit'])
            lo,hi=endpoints;assert hi[normal]>lo[normal];value=round(math.dist(lo,hi)*factor,4);depths.append(value)
            rows.append(dict(portal=portal['id'],kind='local_masonry_depth',source_report=r['id'],source_feature=span['id'],low_native=str(lo),high_native=str(hi),value_cm=value,confidence=span['confidence'],limits=spec['limits']))
        panels.append((portal,sorted(columns),widths,depths))
    with (ref/'STONE_PORTAL_PROFILE_SAMPLES.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="960" viewBox="0 0 1400 960">','<rect width="1400" height="960" fill="#12202b"/>','<g fill="#edf4f8" font-family="Arial">','<text x="35" y="38" font-size="25">B and Lower stone mouths — measured local sections</text>','<text x="35" y="70" font-size="16">Build25640462 · 2.54cm/native · independent floor/intrados, widths and masonry depth</text>']
    for n,(portal,columns,widths,depths) in enumerate(panels):
        left=45+n*680;values=[v for c in columns for v in [c[0]]]+[v for w in widths for v in w[:2]];origin=min(values)-10;sx=lambda x:left+80+(x-origin)*3.4
        zmin=math.floor(min(c[1] for c in columns)/50)*50;zmax=math.ceil(max(c[2] for c in columns)/50)*50;scale=460/(zmax-zmin);sy=lambda z:650-(z-zmin)*scale
        parts.append(f'<text x="{left}" y="115" font-size="21">{escape(portal["label"])}</text>')
        parts.append(f'<text x="{left}" y="143" font-size="15">Plane {"YX"[n]}={portal["section_plane_native"]*factor/100:.3f}m</text>')
        for z in range(zmin,zmax+1,50):parts.append(f'<path d="M{left+75},{sy(z):.2f}h450" stroke="#415765"/><text x="{left}" y="{sy(z)+5:.2f}" font-size="13">Z{z*factor/100:+.2f}m</text>')
        for key,color in [(1,'#6bd4b2'),(2,'#e9ba73')]:
            pts=' '.join(f'{sx(c[0]):.2f},{sy(c[key]):.2f}' for c in columns);parts.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-dasharray="5 5"/>')
            for c in columns:parts.append(f'<circle cx="{sx(c[0]):.2f}" cy="{sy(c[key]):.2f}" r="4" fill="{color}"><title>{escape(c[3])}; native{c[0]},{c[key]}</title></circle>')
        for lo,hi,z,ident in widths:
            yy=sy(z);parts.append(f'<path d="M{sx(lo):.2f},{yy:.2f}H{sx(hi):.2f}" stroke="#b89bef" stroke-width="2"><title>{escape(ident)}</title></path><text x="{left+540}" y="{yy+4:.2f}" font-size="12" fill="#b89bef">{(hi-lo)*factor:.2f}cm</text>')
        parts.append(f'<text x="{left}" y="700" font-size="15">{len(columns)} columns; {len(widths)} width chords</text>')
        parts.append(f'<text x="{left}" y="730" font-size="15">Local masonry depths(cm): {", ".join(str(v) for v in depths)}</text>')
        parts.append(f'<text x="{left}" y="760" font-size="14">Transverse world axis {"XY"[portal["transverse_axis"]]}; hover points for native coordinates.</text>')
    parts+=['<text x="35" y="815" font-size="16">Gold: stone intrados. Green: sand floor. Purple: opening chords. Dashed connectors show sample order.</text>','<text x="35" y="846" font-size="16">Sections exclude separate timber roofs, external stair flight and intervening Wood cover.</text>','<text x="35" y="877" font-size="16">Full curve/apex/jamb extents, depth variation and rendered offsets require separate bounded evidence.</text>','<text x="35" y="918" font-size="16">Gate1 FAIL. These local sections do not certify continuous surfaces or the whole-map footprint.</text>','</g></svg>']
    (ref/'STONE_PORTAL_PROFILES.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
    print(len(rows),'reviewed stone portal measurements; sample-only profiles')

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
