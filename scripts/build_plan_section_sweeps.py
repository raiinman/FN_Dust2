"""Derive native horizontal-section evidence; never infer unsampled boundary edges."""
import csv,json,math,re
from pathlib import Path
from html import escape

def build(root):
 ref=root/'reference';data=json.loads((ref/'PLAN_SECTION_SWEEPS.json').read_text());factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
 rows=[];open_rows=[]
 for report in data['reports']:
  assert report['status'].startswith('complete') and max(report['restore_numeric_errors'])<=.01
  for station in report['config']['stations']:
   for yaw in station['yaws']:
    obs=[o for o in report['observations'] if o['station_id']==station['id'] and o['yaw']==yaw]
    opened=[o for o in report.get('open_observations',[]) if o['station_id']==station['id'] and o['yaw']==yaw]
    if opened:
     assert report['config'].get('allow_open_rays') and not obs and len(opened)==2 and {o['repeat'] for o in opened}=={1,2}
     assert all(o['semantic_reply']==["Rangefinder didn't hit anything"] and o['eye_origin']==[station['pose'][0],station['pose'][1],station['pose'][2]+64] for o in opened)
     open_rows.append(dict(report=report['id'],area=report['area'],station=station['id'],yaw=yaw,eye_origin_native=str(opened[0]['eye_origin']),semantic_reply="Rangefinder didn't hit anything",limits='No endpoint/distance; does not prove absent player collision, floor extent or rendered boundary'))
     continue
    assert len(obs)==2 and obs[0]['hit']==obs[1]['hit'] and obs[0]['surface']==obs[1]['surface']
    o=obs[0];distance=math.dist(o['eye_origin'],o['hit']);assert distance>.1
    for v in obs:
     matched=re.search(r'DISTANCE:\s+(-?\d+(?:\.\d+)?) inches',v['rangefinder_reply']);assert matched and abs(float(matched.group(1))-distance)<=.02
    x,y,z=o['hit'];assert abs(z-o['eye_origin'][2])<=.02
    material=re.search('surfaceprop ([^,]+)',o['surface'][0]).group(1)
    rows.append(dict(report=report['id'],area=report['area'],station=station['id'],yaw=yaw,x_native=x,y_native=y,z_native=z,x_cm=round(x*factor,4),y_cm=round(y*factor,4),z_cm=round(z*factor,4),distance_cm=round(distance*factor,4),surface=material,confidence='confirmed repeated first-hit point',limits=report['review']))
 assert rows and len({(r['report'],r['station'],r['yaw']) for r in rows})==len(rows)
 with (ref/'PLAN_SECTION_POINTS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 if open_rows:
  with (ref/'PLAN_SECTION_OPEN_RAYS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=open_rows[0]);w.writeheader();w.writerows(open_rows)
 parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1200" viewBox="0 0 1600 1200">','<rect width="1600" height="1200" fill="#101923"/>','<g fill="#edf3f8" font-family="Arial"><text x="40" y="38" font-size="25">Dust II — native horizontal first-hit sections</text><text x="40" y="68" font-size="17">Build25640462 · 2.54cm/native · source X right / Y up · repeated endpoint evidence</text><text x="40" y="96" font-size="16">No lines join neighboring rays: angular gaps, cover occlusion and portals remain unsurveyed.</text></g>']
 # Fixed full-map axes preserve relative position across floor layers.
 scale=.145
 def xy(x,y,layer):return 45+layer*790+(x+2600)*scale,145+(3500-y)*scale
 for layer,title in [(0,'LOWER · ray Z below native datum0'),(1,'UPPER · ray Z at/above native datum0')]:
  left=45+layer*790;parts.append(f'<text x="{left}" y="128" fill="#cbd9e4" font-family="Arial" font-size="19">{title}</text>')
  for x in range(-2500,2001,500):
   a,b=xy(x,-1400,layer),xy(x,3500,layer);parts.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="#344550"/><text x="{a[0]-16}" y="{a[1]+20}" fill="#a6b9c7" font-family="Arial" font-size="11">{x*factor/100:.1f}m</text>')
  for y in range(-1000,3501,500):
   a,b=xy(-2600,y,layer),xy(2200,y,layer);parts.append(f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="#344550"/><text x="{b[0]+4}" y="{b[1]+4}" fill="#a6b9c7" font-family="Arial" font-size="11">{y*factor/100:.1f}m</text>')
  for row in rows:
   if (row['z_native']>=0)!=bool(layer):continue
   x,y=xy(row['x_native'],row['y_native'],layer);color='#52d0e3' if row['surface']=='concrete' else '#f0b64c'
   title=escape(f"{row['report']} yaw{row['yaw']}: ({row['x_cm']},{row['y_cm']},{row['z_cm']})cm · {row['surface']} · first hit only")
   parts.append(f'<g><title>{title}</title><circle cx="{x}" cy="{y}" r="2.8" fill="{color}"/></g>')
  for report in data['reports']:
   for station in report['config']['stations']:
    x,y,z=station['pose'];z+=64
    if (z>=0)!=bool(layer):continue
    u,v=xy(x,y,layer);label=escape(report['area']);parts.append(f'<circle cx="{u}" cy="{v}" r="4" fill="#edf3f8"/><text x="{u+7}" y="{v-7}" fill="#edf3f8" font-family="Arial" font-size="12">{label} · Z{z*factor/100:+.3f}m</text>')
 parts.append(f'<g fill="#edf3f8" font-family="Arial" font-size="16"><text x="45" y="925">{len(rows)} distinct direction points, each repeated twice with native rangefinder crosscheck.</text><text x="45" y="955">Cyan: concrete surface. Gold: other material (often cover); color alone never assigns architectural identity.</text><text x="45" y="985">Z is the exact horizontal collision section, not a floor elevation or full-height wall.</text><text x="45" y="1015">Every point retains pose, surface/shape/face, repetitions and source-build identity in PLAN_SECTION_SWEEPS.</text><text x="45" y="1045">Output rounding ≤.0508cm per span; angular gaps/render-to-collision offsets are NOT bounded by that rounding.</text><text x="45" y="1075">Gate1 FAIL: wall/corner interpretation, independent withheld checks and continuous layered footprint remain pending.</text></g></svg>')
 if open_rows:
  parts[-1]=parts[-1].replace('</svg>',f'<text x="45" y="1115" fill="#f0b64c" font-family="Arial" font-size="16">{len(open_rows)} repeated native no-hit directions separately recorded in PLAN_SECTION_OPEN_RAYS; no endpoint/distance.</text><text x="45" y="1145" fill="#f0b64c" font-family="Arial" font-size="16">Native ray misses do not prove absent player collision, floor extent or rendered boundaries.</text></svg>')
 (ref/'PLAN_SECTION_SWEEPS.svg').write_text('\n'.join(parts)+'\n')
 print(f'{len(rows)} repeated native section points;{len(open_rows)} no-hit directions; no inferred edges or footprint acceptance')

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
