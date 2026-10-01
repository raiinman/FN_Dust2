"""Build a native-unit floor register and point plot from reviewed probe reports.

Usage: py -3.11 scripts/build_elevation_register.py
Reads reference/ELEVATION_PROBES.json. No inferred walls, routes or cm conversion.
"""
import csv
import html
import json
from pathlib import Path

def build(root):
    reports=json.loads((root/'reference/ELEVATION_PROBES.json').read_text(encoding='utf-8'))['reports']
    rows=[]
    for report in reports:
        if not report.get('status','').startswith('complete'):
            continue
        hit=report['endpoints']['floor']
        observations=[o for o in report['observations'] if o['feature']=='floor']
        assert observations[-1]['hit']==observations[-2]['hit']==hit
        assert observations[-1]['xy_error']<=.02
        rows.append(dict(id=report['id'],area=report['area'],source_x=hit[0],source_y=hit[1],
            source_z=hit[2],unit='source_units',confidence='confirmed native collision hit',
            output_rounding='.01 per coordinate',target_xy_error=observations[-1]['xy_error'],
            source_build=report['source_build'],surface=observations[-1]['hit_description'][0],
            production_status='raw source endpoint; conversion in SCALE_CALIBRATION.json; render/collision crosscheck unresolved'))
    with (root/'reference/FLOOR_DATUMS.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n')
        writer.writeheader();writer.writerows(rows)
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="760" viewBox="0 0 1120 760">',
         '<rect width="1120" height="760" fill="#f5f4ef"/>',
         '<g font-family="Arial,sans-serif" fill="#24282b">',
         '<text x="35" y="35" font-size="23" font-weight="bold">Dust II — surveyed native floor datums</text>',
         '<text x="35" y="60" font-size="14">CS2 build 25640462 • Source units • +Y upward • conversion documented separately in SCALE_CALIBRATION.json</text>',
         '<text x="35" y="82" font-size="13">Point evidence only: no boundary, route, room extent or continuous surface is inferred.</text>']
    # Include T Spawn's negative Y without clipping it below the plot.
    def xy(x,y):return 75+(x+2200)*.15, 640-(y+1000)*.135
    for x in range(-2000,2001,500):
        px,_=xy(x,0)
        svg.append(f'<path d="M{px} 120 V640" stroke="#d8d9d4"/><text x="{px}" y="665" font-size="11" text-anchor="middle">{x}</text>')
    for y in range(-1000,2801,400):
        _,py=xy(0,y)
        svg.append(f'<path d="M75 {py} H725" stroke="#d8d9d4"/><text x="65" y="{py+4}" font-size="11" text-anchor="end">{y}</text>')
    svg.append('<text x="390" y="690" font-size="13">Source X</text><text x="20" y="365" font-size="13">Y</text>')
    for index,row in enumerate(rows,1):
        x,y=xy(row['source_x'],row['source_y'])
        svg.append(f'<circle cx="{x}" cy="{y}" r="6" fill="#a9302a"/><text x="{x+10}" y="{y-7}" font-size="13" font-weight="bold">{index}</text><text x="{x+10}" y="{y+11}" font-size="11">z {row["source_z"]:.2f}</text>')
        label=html.escape(row['area'])
        if len(label)>27:label='Upper Mid / Suicide approach'
        svg.append(f'<text x="760" y="{145+index*42}" font-size="13">{index}. {label}</text><text x="778" y="{161+index*42}" font-size="11">({row["source_x"]:.2f}, {row["source_y"]:.2f}, {row["source_z"]:.2f})</text>')
    svg.extend(['<text x="35" y="727" font-size="12">Repeated endpoints agree at printed precision. This is repeatability, not absolute architectural accuracy.</text>',
                '<text x="35" y="746" font-size="12">Evidence: ELEVATION_PROBES.json • Register: FLOOR_DATUMS.csv • Gate 1 remains incomplete.</text>', '</g></svg>'])
    (root/'reference/FLOOR_DATUM_PLAN.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8',newline='\n')
    print(f'Built {len(rows)} native datums; no physical conversion applied')

if __name__=='__main__':
    build(Path(__file__).resolve().parent.parent)
