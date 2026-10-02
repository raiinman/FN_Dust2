"""Plot explicitly reviewed B down-hit points; never interpolate a platform."""
import json
from pathlib import Path
from html import escape


def build(root):
    ref=root/'reference';profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text())
    spec=profile['b_platform_column_review'];cases=spec['plan']['cases'];reports={r['id']:r for r in profile['reports']}
    assert len(cases)==9 and max(spec['driver_recovery']['restore_numeric_errors'])==0
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="920" viewBox="0 0 1400 920">','<rect width="1400" height="920" fill="#14202e"/><g font-family="Arial" fill="white">','<text x="30" y="40" font-size="25">B Site / repeated central ground and cover samples</text>','<text x="30" y="75" font-size="17">Source XY plan / physical grid. First-down hit identity retained; no interpolation. Gate1 FAIL.</text>']
    sx=lambda x:160+(x+2000)*1.5;sy=lambda y:620-(y-2400)*1.5
    for x in [-2000,-1850,-1700]:svg.append(f'<path d="M{sx(x)},260V650" stroke="#526375"/><text x="{sx(x)-48}" y="680" font-size="16">X{x}</text>')
    for y in [2400,2500,2600]:svg.append(f'<path d="M125,{sy(y)}H650" stroke="#526375"/><text x="35" y="{sy(y)+5}" font-size="16">Y{y}</text>')
    rows=[]
    for c in cases:
        r=reports[c['id']];p=r['endpoints']['floor'];obs=[o for o in r['observations'] if o['feature']=='floor'][-2:];assert len(obs)==2 and obs[0]['hit']==obs[1]['hit']==p
        material=str(obs[-1]['hit_description']);cover='surfaceprop Wood_Plank,' in material;color='#ffbf69' if cover else '#60e4cb';x,y=c['xy']
        svg.append(f'<circle cx="{sx(x)}" cy="{sy(y)}" r="7" fill="{color}"><title>{escape(r["surface_semantics"])}</title></circle><text x="{sx(x)+12}" y="{sy(y)-12}" font-size="15" fill="{color}">Z{p[2]:.2f} / {p[2]*2.54:.3f}cm</text>')
        rows.append((c['id'],p,cover))
    svg.extend(['<text x="815" y="160" font-size="20">SourceZ0 elevations, not body heights</text>','<text x="815" y="193" font-size="16">Green: concrete/gravel Mesh point.</text>','<text x="815" y="222" font-size="16">Amber: Wood_Plank Hull cover top.</text>'])
    for n,(_,p,cover) in enumerate(rows):svg.append(f'<text x="815" y="{265+n*29}" font-size="15">X{p[0]:.2f} / Y{p[1]:.2f} / Z{p[2]:.2f}{" COVER" if cover else ""}</text>')
    rises=[(reports[f'B_PLATFORM_X2000_Y{y}_001']['endpoints']['floor'][2]-reports[f'B_PLATFORM_X1700_Y{y}_001']['endpoints']['floor'][2])*2.54 for y in [2500,2600]]
    svg.extend(['<path d="M160,735h150" stroke="white" stroke-width="3"/><text x="160" y="768" font-size="16">100native =254cm</text>',f'<text x="30" y="815" font-size="16">Ground point differences: X-1700 toX-2000 atY2500 ={rises[0]:.4f}cm; atY2600 ={rises[1]:.4f}cm.</text>','<text x="30" y="847" font-size="16">Different XY points: no exact retaining-face height, floor slope, constant platform or covered-body dimensions.</text>','<text x="30" y="880" font-size="16">Native overhead context inspected at actualpitch89. No camera fit/transfer granted by this numeric plan.</text></g></svg>'])
    (ref/'B_SITE_SURFACE_SAMPLES.svg').write_text('\n'.join(svg)+'\n')
    print('Nine reviewed B point samples; no surface interpolation')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
