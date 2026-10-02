"""Draw calibrated layered local architectural sections, not full wall outlines.

Run: py -3.11 scripts/build_architectural_survey_plan.py. Uses explicit reviewed
ARCHITECTURAL_ENDPOINTS accepted_sections/accepted_columns, floor datums and
SCALE_CALIBRATION. Writes ARCHITECTURAL_SURVEY_PLAN.svg and section index CSV.
Source X right/Y up; separation by ray height makes lower/upper evidence visible.
Every line is a measured chord through space, never a wall or polygon edge.
"""
import csv,json,math
from html import escape
from pathlib import Path


def build(root):
    ref=root/'reference'
    calibration=json.loads((ref/'SCALE_CALIBRATION.json').read_text())
    assert calibration['status'].startswith('ACCEPTED')
    factor=calibration['cm_per_source_unit'];assert factor==2.54
    reports=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']
    rows=[]
    for report in reports:
        for section in report.get('accepted_sections',[]):
            axis=section.get('axis',0);positive=0 if axis==0 else 90;negative=180 if axis==0 else -90
            obs=[o for o in report['observations'] if o['station_id']==section['station_id']]
            a=[o['hit'] for o in obs if o['yaw']==negative]
            b=[o['hit'] for o in obs if o['yaw']==positive]
            assert len(a)==len(b)==2 and a[0]==a[1] and b[0]==b[1]
            assert all(a[0][i]==b[0][i] for i in range(3) if i!=axis)
            rows.append(dict(id=section['id'],area=report['area'],feature=section['feature'],
                report=report['id'],axis='XY'[axis],x1_cm=round(a[0][0]*factor,4),
                y1_cm=round(a[0][1]*factor,4),x2_cm=round(b[0][0]*factor,4),
                y2_cm=round(b[0][1]*factor,4),z_cm=round(a[0][2]*factor,4),
                length_cm=round(math.dist(a[0],b[0])*factor,4),limits=section['notes']))
    assert rows and len({r['id'] for r in rows})==len(rows)
    with (ref/'ARCHITECTURAL_SECTIONS.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    floors=list(csv.DictReader((ref/'FLOOR_DATUMS.csv').open()))
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1320" viewBox="0 0 1600 1320">',
      '<rect width="1600" height="1320" fill="#101923"/>',
      '<g fill="#edf3f8" font-family="Arial"><text x="45" y="38" font-size="25">Dust II — calibrated architectural section survey</text>',
      '<text x="45" y="67" font-size="16">Build25640462 · 2.54cm/native unit · source X right / Y up · measured chords and elevation points</text>',
      '<text x="45" y="92" font-size="16">Gate1 FAIL: these are local sections through space; no continuous wall outline or complete footprint is certified.</text></g>']
    scale=.125
    def xy(x_cm,y_cm,layer):
        return 55+layer*790+(x_cm/factor+2300)*scale,170+(3300-y_cm/factor)*scale
    for layer,title,color in [(0,'LOWER: sampled ray Z below source datum0','#49c6e7'),(1,'UPPER: sampled ray Z at/above source datum0','#eeb458')]:
        left=55+layer*790
        parts.append(f'<text x="{left}" y="137" fill="{color}" font-family="Arial" font-size="19">{title}</text>')
        for x in range(-2000,2001,500):
            a=xy(x*factor,-1400*factor,layer);b=xy(x*factor,3300*factor,layer)
            parts.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="#40515c" stroke-width="1"/><text x="{a[0]-14}" y="{a[1]+18}" fill="#a5b8c6" font-family="Arial" font-size="11">{x*factor/100:.1f}m</text>')
        for y in range(-1000,3001,500):
            a=xy(-2300*factor,y*factor,layer);b=xy(1900*factor,y*factor,layer)
            parts.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="#40515c" stroke-width="1"/><text x="{b[0]+8}" y="{b[1]+4}" fill="#a5b8c6" font-family="Arial" font-size="11">Y {y*factor/100:.1f}m</text>')
        for r in rows:
            if (r['z_cm']>=0)!=bool(layer):continue
            a=xy(r['x1_cm'],r['y1_cm'],layer);b=xy(r['x2_cm'],r['y2_cm'],layer)
            label=escape(f"{r['id']}: {r['length_cm']}cm at Z{r['z_cm']}cm; {r['feature']}; {r['limits']}")
            parts.append(f'<g><title>{label}</title><path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="{color}" stroke-width="2.3" opacity=".8"/><circle cx="{a[0]}" cy="{a[1]}" r="2.5" fill="#fff"/><circle cx="{b[0]}" cy="{b[1]}" r="2.5" fill="#fff"/></g>')
        for i,floor in enumerate(floors,1):
            x,y,z=[float(floor[k]) for k in ['source_x','source_y','source_z']]
            if (z>=0)!=bool(layer):continue
            u,v=xy(x*factor,y*factor,layer)
            label=escape(f"{floor['area']}: floor Z{z*factor:.4f}cm; point only")
            parts.append(f'<g><title>{label}</title><circle cx="{u}" cy="{v}" r="5" fill="#d8ebf0" stroke="#111"/><text x="{u+7}" y="{v-5}" fill="#fff" stroke="#101923" stroke-width="3" paint-order="stroke" font-family="Arial" font-size="13">{i}</text></g>')
        # Floor/overhead columns remain single XY locations with separate Z values.
        for report in reports:
            if not report.get('accepted_columns'):continue
            lo,hi=[report['endpoints'][k] for k in ['floor','ceiling']]
            if (lo[2]>=0)!=bool(layer):continue
            u,v=xy(lo[0]*factor,lo[1]*factor,layer)
            label=escape(f"{report['id']}: floor Z{lo[2]*factor:.4f}cm / first overhead Z{hi[2]*factor:.4f}cm; local column only")
            parts.append(f'<g><title>{label}</title><rect x="{u-2.5}" y="{v-2.5}" width="5" height="5" fill="#8cdaaa" stroke="#101923"/></g>')
    parts.append('<g fill="#edf3f8" font-family="Arial" font-size="15">')
    for i,floor in enumerate(floors):
        col=i//7;y=840+(i%7)*25;x=55+col*790
        parts.append(f'<text x="{x}" y="{y}">{i+1}. {escape(floor["area"])} · floorZ {float(floor["source_z"])*factor/100:+.3f}m</text>')
    parts.extend([f'<text x="55" y="1040">{len(rows)} explicit reviewed horizontal sections; dots are collision endpoints. Hover for ID, height, feature and limitations.</text>',
      '<text x="55" y="1068">Cyan/gold lines are chords through open space, including reviewed local cover gaps. They are NOT boundary walls.</text>',
      '<text x="55" y="1096">Green squares: repeated floor/first-overhead columns. Numbered white circles:13 native floor datums.</text>',
      '<text x="55" y="1124">Panels separate evidence by ray height, not complete floor stories. Source datum0 is a coordinate convention.</text>',
      '<text x="55" y="1152">Grid spacing12.7m. CSV stores calibrated endpoint XYZ and measured length; no hidden geometry is interpolated.</text>',
      '<text x="55" y="1180">Source repeatability and centimeter conversion do not bound render/collision offsets or minimum body clearance.</text>',
      '<text x="55" y="1208">Remaining: full apertures, cover masses, ramp endpoints, continuous architectural outlines and overlapping elevation layers.</text>',
      '</g></svg>'])
    (ref/'ARCHITECTURAL_SURVEY_PLAN.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
    print(f'{len(rows)} calibrated local section chords;13 floor datums; full footprint pending')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
