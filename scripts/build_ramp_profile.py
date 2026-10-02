"""Rebuild ordered Pit/Long centerline evidence; no continuous ramp inference.

Run python scripts/build_ramp_profile.py, then render/inspect the SVG. Reuses
the repeated-point validator; labels sampling endpoints, not architectural ends.
"""
import csv,json,html,math
from pathlib import Path
from build_connector_profile import points

def build(root):
 ref=root/'reference';groups=json.loads((ref/'RAMP_PROFILE_GROUPS.json').read_text())
 profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());p=points(profile)
 assert profile['source_build']==groups['source_build']
 factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
 rows=[];svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="860" viewBox="0 0 1280 860">','<rect width="1280" height="860" fill="#12202b"/>','<g fill="#edf4f8" font-family="sans-serif">','<text x="35" y="35" font-size="23">Pit and Long road: measured centerline samples at source X1400</text>','<text x="35" y="60" font-size="15">Calibrated 2.54 cm/native unit. Dashed connectors show sample order only; no fitted surface or full ramp ends.</text>']
 for index,(name,ids) in enumerate(groups['profiles'].items()):
  assert len(ids)==20;hits=[p[i] for i in ids];assert all(b[1]>a[1] for a,b in zip(hits,hits[1:]))
  ymin,ymax=hits[0][1],hits[-1][1];zmin,zmax=min(h[2] for h in hits)-15,max(h[2] for h in hits)+15;top=100+index*345
  x=lambda y:90+1100*(y-ymin)/(ymax-ymin)
  y=lambda z:top+240-240*(z-zmin)/(zmax-zmin)
  svg.append(f'<text x="90" y="{top}" font-size="18">{html.escape(name)} — source Y{ymin:g}..{ymax:g}; Z{hits[0][2]:g}..{hits[-1][2]:g}</text>')
  for j in range(5):
   z=zmin+(zmax-zmin)*j/4;yy=y(z)
   svg.append(f'<path d="M90 {yy:.2f}H1190" stroke="#415564"/><text x="10" y="{yy+5:.2f}" font-size="13">{z*factor:.1f}cm</text>')
  svg.append('<polyline fill="none" stroke="#f4b76b" stroke-dasharray="5 6" points="'+' '.join(f'{x(h[1]):.2f},{y(h[2]):.2f}' for h in hits)+'"/>')
  for ident,h in zip(ids,hits):
   svg.append(f'<circle cx="{x(h[1]):.2f}" cy="{y(h[2]):.2f}" r="4" fill="#72ddd3"><title>{ident}: native {h}; calibrated Z{h[2]*factor:.4f}cm</title></circle>')
  for j in range(5):
   yy=ymin+(ymax-ymin)*j/4
   svg.append(f'<text x="{x(yy):.2f}" y="{top+270}" text-anchor="middle" font-size="13">Y {yy:g} / {yy*factor:.1f}cm</text>')
  for a,b,ha,hb in zip(ids,ids[1:],hits,hits[1:]):
   rows.append(dict(profile=name,from_id=a,to_id=b,horizontal_sample_interval_cm=round(math.dist(ha[:2],hb[:2])*factor,4),rise_cm=round((hb[2]-ha[2])*factor,4),limits='Discrete sample pair; no full ramp transition, constant slope, side width or rendered offset acceptance'))
 svg+=['<text x="35" y="815" font-size="15">A-entry X1200/Y2800 hull and X1450/X950 companion samples remain separate from these centerlines.</text>','<text x="35" y="840" font-size="15">Native collision pavement differs from nearby curb/cap and player hull support. Gate 1 footprint remains incomplete.</text>','</g></svg>']
 (ref/'RAMP_PROFILE.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
 with (ref/'RAMP_SEGMENTS.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print('40 validated centerline points;38 sample intervals; no continuous surface acceptance')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
