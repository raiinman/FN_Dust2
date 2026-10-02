"""Derive separate measured Long inner timber-header/stone-arch profiles.

Columns selected in LONG_INNER_PORTAL_PROFILE are repeated native collision
reports; sample-order connectors never fit or certify unsampled geometry.
"""
import csv,json,math
from pathlib import Path

def build(root):
 ref=root/'reference';spec=json.loads((ref/'LONG_INNER_PORTAL_PROFILE.json').read_text());reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']}
 factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
 rows=[]
 for component,ids in spec['components'].items():
  for ident in ids:
   r=reports[ident];assert r['source_build']==spec['source_build'] and r['status'].startswith('complete;') and len(r['accepted_columns'])==1
   floor,top=[r['endpoints'][key] for key in ['floor','ceiling']];assert math.dist(floor[:2],top[:2])<=.04 and top[2]>floor[2]
   for key,endpoint in [('floor',floor),('ceiling',top)]:
    obs=[o for o in r['observations'] if o['feature']==key];assert obs[-1]['hit']==obs[-2]['hit']==endpoint and obs[-1]['xy_error']<=.02
   rows.append(dict(component=component,report_id=ident,source_x=floor[0],source_y=floor[1],source_floor_z=floor[2],source_top_z=top[2],x_cm=round(floor[0]*factor,4),y_cm=round(floor[1]*factor,4),floor_z_cm=round(floor[2]*factor,4),top_z_cm=round(top[2]*factor,4),column_height_cm=round((top[2]-floor[2])*factor,4),confidence='confirmed repeated selected collision column',limits=spec['limits']))
 with (ref/'LONG_INNER_PORTAL_PROFILE.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1250" height="790" viewBox="0 0 1250 790">','<rect width="1250" height="790" fill="#12202b"/>','<g fill="#edf4f8" font-family="sans-serif">','<text x="35" y="35" font-size="24">Long inner portal — separate repeated collision components</text>','<text x="35" y="65" font-size="16">Build25640462; 2.54cm/native. Axes use world meters; two distinct wall-depth sections.</text>']
 for n,component in enumerate(spec['components']):
  selected=sorted([r for r in rows if r['component']==component],key=lambda r:r['source_x']);left=60+n*600;sx=lambda x:left+65+(x-550)*2;sy=lambda z:595-z*1.5
  parts.append(f'<text x="{left}" y="107" font-size="20">{component.replace("_"," ")} · Y{selected[0]["y_cm"]/100:.4f}m</text>')
  for z in [0,50,100,150,200,250,300]:parts.append(f'<path d="M{left+65},{sy(z):.2f}h360" stroke="#415765"/><text x="{left}" y="{sy(z)+5:.2f}" font-size="13">Z{z*factor/100:.2f}m</text>')
  for x in [560,600,640,680,720]:parts.append(f'<text x="{sx(x)-16:.2f}" y="625" font-size="13">{x*factor/100:.2f}</text>')
  for key,colour in [('source_floor_z','#6bd4b2'),('source_top_z','#e9ba73')]:
   parts.append('<polyline points="'+' '.join(f'{sx(r["source_x"]):.2f},{sy(r[key]):.2f}' for r in selected)+f'" fill="none" stroke="{colour}" stroke-width="2" stroke-dasharray="4 4"/>')
   for r in selected:parts.append(f'<circle cx="{sx(r["source_x"]):.2f}" cy="{sy(r[key]):.2f}" r="4" fill="{colour}"><title>{r["report_id"]}; height{r["column_height_cm"]}cm</title></circle>')
  for r in selected:parts.append(f'<text x="{sx(r["source_x"])-22:.2f}" y="{sy(r["source_top_z"])-12:.2f}" font-size="12">{r["column_height_cm"]:.2f}</text>')
  if component=='stone_intrados' and spec.get('intrados_section_report'):
   report=reports[spec['intrados_section_report']]
   for section in report['accepted_sections']:
    obs=[o for o in report['observations'] if o['station_id']==section['station_id']];assert len(obs)==4 and obs[0]['hit']==obs[1]['hit'] and obs[2]['hit']==obs[3]['hit']
    high,low=obs[0]['hit'],obs[2]['hit'];assert high[1]==low[1]==selected[0]['source_y'] and high[2]==low[2] and high[0]>low[0]
    yy=sy(high[2]);parts.append(f'<path d="M{sx(low[0]):.2f},{yy:.2f}H{sx(high[0]):.2f}" stroke="#b89bef" stroke-width="2"/><text x="{left+435}" y="{yy+5:.2f}" font-size="12" fill="#b89bef">{(high[0]-low[0])*factor:.2f}cm</text>')
  parts.append(f'<text x="{left+90}" y="653" font-size="14">World X (m). Point labels: local column height(cm).</text>')
 parts+=['<text x="35" y="700" font-size="16">Gold: first overhead. Green: floor. Purple: independent width chords. Dashed lines connect samples, never fitted surfaces.</text>','<text x="35" y="735" font-size="16">Header is timber atY744; intrados is concrete atY762. Leaf clearance, full arch ends and render offsets remain separate.</text>','<text x="35" y="770" font-size="16">Gate1 FAIL: critical dimensions and calibrated continuous layered whole-map footprint remain incomplete.</text>','</g></svg>']
 (ref/'LONG_INNER_PORTAL_PROFILE.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8');print(f'{len(rows)} selected repeated header/arch columns; sample-only profiles')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
