"""Validate and compare Pit upper-side first hits at measured-floor heights.

Rebuild PIT_UPPER_SIDE_CHECKS JSON/CSV/SVG, then render and inspect. The figure
compares actual local and remote first-hit components. Dashed references are
not measured continuous walls; first-hit changes never certify body endpoints.
"""
import csv,json,math,re
from pathlib import Path

def main():
 ref=Path('reference');arch=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
 connectors=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text())
 rows=[]
 for id in ['PIT_UPPER_FLOOR_RELATIVE_SIDE_PREFLIGHT_005','PIT_UPPER_FLOOR_PLUS20_SIDE_PREFLIGHT_006','PIT_UPPER_FIXED_Z0_END_PREFLIGHT_007']:
  r=next(r for r in arch['reports'] if r['id']==id)
  assert r['source_build']=='25640462' and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01
  for anchor in r['config'].get('source_floor_anchors',[]):
   floor=next(v for v in connectors['reports'] if v['id']==anchor['report'])
   # Original corrected native floor coordinates own origin selection.
   samples=[o for o in floor['observations'] if o.get('feature')=='floor'][-2:]
   assert len(samples)==2 and samples[0]['hit']==samples[1]['hit']==floor['endpoints']['floor']
   assert all(o['xy_error']<=.02 and math.dist(o['hit'],anchor['floor_point'])<=.02 for o in samples)
  for i in range(0,len(r['observations']),2):
   a,o=r['observations'][i:i+2]
   assert a['repeat']==1 and o['repeat']==2 and a['hit']==o['hit'] and a['surface']==o['surface'] and a['pose']==o['pose']
   v=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',o['pose'])]
   eye=v[:2]+[v[2]+64];assert len(v)==6 and math.dist(eye,o['eye_origin'])<=.01
   assert abs(v[3])<=.01 and abs(v[5])<=.01 and abs((v[4]-o['yaw']+180)%360-180)<=.01
   assert math.dist(eye,o['hit'])>.1 and abs(float(o['rangefinder_reply'].split()[1])-math.dist(eye,o['hit']))<=.02
   assert abs(eye[1]-o['hit'][1])<=.02 and abs(eye[2]-o['hit'][2])<=.02
   expected=1592 if o['yaw']==0 else 1272
   local=abs(o['hit'][0]-expected)<=.02 and 'surfaceprop concrete,' in str(o['surface']) and 'shape type: Mesh,' in str(o['surface'])
   rows.append(dict(report=id,station=o['station_id'],yaw=o['yaw'],source_x=eye[0],source_y=eye[1],eye_z=eye[2],hit_x=o['hit'][0],hit_y=o['hit'][1],hit_z=o['hit'][2],local_mesh=local,material_shape='; '.join(o['surface'])))
 result=dict(source_build='25640462',points=rows,scope='At Y750 high64 west misses lowMesh while low20 and fixedZ0 see it. Other upper stations reach separate terrain/barrel/remote masonry. Same ray height is required for longitudinal facing-limit comparison. No far-hit width, continuous wall, actual body end or closed footprint inferred.',gate1='FAIL')
 (ref/'PIT_UPPER_SIDE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 with (ref/'PIT_UPPER_SIDE_CHECKS.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1050"><rect width="1400" height="1050" fill="#14202e"/><g font-family="Arial" fill="white"><text x="30" y="40" font-size="25">Pit upper sides / measured height comparison</text><text x="30" y="74" font-size="17">Actual repeated native first hits. Points at separate elevations; no continuous wall or footprint acceptance.</text>']
 groups=[('005 / floor+64',rows[:8]),('006 / floor+20',rows[8:16]),('007 / fixed Z0',rows[16:])]
 for j,(label,points) in enumerate(groups):
  y0=125+j*280;sx=lambda x:100+(x-450)*.6;sy=lambda y:y0+210-(y-740)*1.1
  svg.append(f'<text x="30" y="{y0}" font-size="20">{label}</text>')
  for x in [1272,1592]:svg.append(f'<path d="M{sx(x)},{y0+15}V{y0+225}" stroke="#8296a7" stroke-dasharray="5 5"/>')
  for y in [750,800,850,900]:svg.append(f'<text x="35" y="{sy(y)+5}" font-size="15">Y{y}</text>')
  for p in points:
   color='#49f6e0' if p['local_mesh'] else '#ff926e';svg.append(f'<circle cx="{sx(p["hit_x"])}" cy="{sy(p["hit_y"])}" r="4" fill="{color}"/>')
  svg.append(f'<text x="1010" y="{y0+230}" font-size="16">Cyan: local concreteMesh</text><text x="1010" y="{y0+250}" font-size="16">Coral: unlike/distant surface</text>')
 svg.append('<text x="30" y="995" font-size="16">Dashed X1272/1592 references are comparison axes only. Numeric file retains every component and exact eye/hit Z.</text></g></svg>')
 (ref/'PIT_UPPER_SIDE_CHECKS.svg').write_text('\n'.join(svg)+'\n')
 print(f'{len(rows)} repeated first-hit points; no new physical rows; Gate1 FAIL')

if __name__=='__main__':main()
