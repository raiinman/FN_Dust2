"""Validate and compare Pit upper-side first hits at measured-floor heights.

Rebuild PIT_UPPER_SIDE_CHECKS JSON/CSV/SVG, then render and inspect. The figure
compares actual local and remote first-hit components. Dashed references are
not measured continuous walls; first-hit changes never certify body endpoints.
"""
import csv,hashlib,json,math,re
from pathlib import Path

def height_points(arch):
 r=next((r for r in arch['reports'] if r['id']=='PIT_UPPER_Y750_HEIGHT_PREFLIGHT_016'),None)
 if r is None:return []
 assert r['source_build']=='25640462' and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01
 result=[]
 for i in range(0,len(r['observations']),2):
  a,o=r['observations'][i:i+2]
  assert a['repeat']==1 and o['repeat']==2 and a['hit']==o['hit'] and a['surface']==o['surface'] and a['pose']==o['pose']
  station=next(s for s in r['config']['stations'] if s['id']==o['station_id'])
  v=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',o['pose'])];eye=v[:2]+[v[2]+64]
  assert len(v)==6 and math.dist(v[:3],station['pose'])<=.01 and math.dist(eye,o['eye_origin'])<=.01
  assert abs(v[3])<=.01 and abs(v[5])<=.01 and abs((v[4]-o['yaw']+180)%360-180)<=.01
  assert abs(eye[1]-750)<=.01 and abs(o['hit'][1]-750)<=.02 and abs(o['hit'][2]-eye[2])<=.02
  assert math.dist(eye,o['hit'])>.1 and abs(float(o['rangefinder_reply'].split()[1])-math.dist(eye,o['hit']))<=.02
  normal=1592 if o['yaw']==0 else 1272
  local=abs(o['hit'][0]-normal)<=.02 and 'surfaceprop concrete,' in str(o['surface']) and 'shape type: Mesh,' in str(o['surface'])
  result.append(dict(report=r['id'],station=o['station_id'],yaw=o['yaw'],eye=eye,hit=o['hit'],local_mesh=local,surface=o['surface']))
 assert len(result)==24
 return result

def facing_limits(arch):
 result=[]
 for side,num,off_material,off_shape in [('WEST','012','sand','Mesh'),('EAST','013','concrete','Hull')]:
  r=next((r for r in arch['reports'] if r['id']==f'PIT_{side}_Z0_FIRST_MESH_LIMIT_{num}'),None)
  if r is None:continue
  c=r['config'];assert r['source_build']=='25640462' and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01
  assert c['height_native']==0 and c['normal_axis']==0 and c['tangent_axis']==1 and len(c['origins'])==2
  assert len({o['normal_coordinate'] for o in c['origins']})==2 and len(r['brackets'])==2
  intervals=[];points=[]
  for bracket in r['brackets']:
   origin=next(o for o in c['origins'] if o['id']==bracket['origin_id'])
   interval=bracket['tangent_interval_native'];assert interval[1]-interval[0]<=.1
   intervals.append(interval)
   for key,mat,shape in [('on','concrete','Mesh'),('off',off_material,off_shape)]:
    index=bracket[key]['observation_index'];a,o=r['observations'][index-1:index+1]
    assert a['repeat']==1 and o['repeat']==2 and a['hit']==o['hit'] and a['surface']==o['surface'] and a['pose']==o['pose']
    assert o['origin_id']==origin['id'] and 'surfaceprop '+mat+',' in str(o['surface']) and 'shape type: '+shape+',' in str(o['surface'])
    v=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',o['pose'])];eye=v[:2]+[v[2]+64]
    assert len(v)==6 and math.dist(eye,o['eye_origin'])<=.01 and abs(eye[2])<=.01
    assert abs(v[3])<=.01 and abs(v[5])<=.01 and abs((v[4]-origin['yaw']+180)%360-180)<=.01
    assert abs(eye[0]-origin['normal_coordinate'])<=.01 and abs(eye[1]-bracket[key]['coordinate'])<=.01
    assert abs(o['hit'][1]-eye[1])<=.02 and abs(o['hit'][2])<=.02 and math.dist(eye,o['hit'])>.1
    assert abs(float(o['rangefinder_reply'].split()[1])-math.dist(eye,o['hit']))<=.02
    if key=='on':assert origin['on_normal_band'][0]<=o['hit'][0]<=origin['on_normal_band'][1]
    points.append(dict(origin=origin['id'],component=key,hit=o['hit'],surface=o['surface']))
  assert intervals[0]==intervals[1]
  result.append(dict(side=side,report=r['id'],native_y_interval=intervals[0],source_y_cm_interval=[2.54*y for y in intervals[0]],height_native=0,points=points,scope='Repeated fixed-Z first-facing visibility/material limit, not full-height structural end or ground outline.'))
 return result

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
 limits=facing_limits(arch)
 captures=json.loads((ref/'CAPTURE_CRASH_RECOVERY.json').read_text())['captures'];contexts=[]
 for id in ['QA_PIT_UPPER_ENDS_CONTEXT_014','QA_PIT_WEST_UPPER_END_CONTEXT_014','QA_PIT_EAST_UPPER_END_CONTEXT_014','QA_PIT_WEST_END_INTERIOR_015','QA_PIT_EAST_END_INTERIOR_015']:
  c=next((c for c in captures if c['id']==id),None)
  if c is None:continue
  assert c['source_build']=='25640462' and hashlib.sha256(Path(c['repository_image_path']).read_bytes()).hexdigest()==c['jpeg_sha256']
  contexts.append({key:c[key] for key in ['id','repository_image_path','jpeg_sha256','pose_command','review']})
 heights=height_points(arch)
 result=dict(source_build='25640462',points=rows,height_points=heights,facing_limits=limits,reviewed_component_contexts=contexts,context_limits='Ground images corroborate retaining-body/cap/curb association. Utility pole overlaps precise west terminal. New context poses have no camera calibration; no metric image inversion accepted.',scope='At Y750 high64 west misses lowMesh while low20 and fixedZ0 see it. Other upper stations reach separate terrain/barrel/remote masonry. Same ray height is required for longitudinal facing-limit comparison. No far-hit width, continuous wall, actual body end or closed footprint inferred.',gate1='FAIL')
 (ref/'PIT_UPPER_SIDE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 with (ref/'PIT_UPPER_SIDE_CHECKS.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1450"><rect width="1400" height="1450" fill="#14202e"/><g font-family="Arial" fill="white"><text x="30" y="40" font-size="25">Pit upper sides / measured height comparison</text><text x="30" y="74" font-size="17">Actual repeated native first hits. Points at separate elevations; no continuous wall or footprint acceptance.</text>']
 groups=[('005 / floor+64',rows[:8]),('006 / floor+20',rows[8:16]),('007 / fixed Z0',rows[16:])]
 for j,(label,points) in enumerate(groups):
  y0=125+j*280;sx=lambda x:100+(x-450)*.6;sy=lambda y:y0+210-(y-740)*1.1
  svg.append(f'<text x="30" y="{y0}" font-size="20">{label}</text>')
  for x in [1272,1592]:svg.append(f'<path d="M{sx(x)},{y0+15}V{y0+225}" stroke="#8296a7" stroke-dasharray="5 5"/>')
  for y in [750,800,850,900]:svg.append(f'<text x="35" y="{sy(y)+5}" font-size="15">Y{y}</text>')
  for p in points:
   color='#49f6e0' if p['local_mesh'] else '#ff926e';svg.append(f'<circle cx="{sx(p["hit_x"])}" cy="{sy(p["hit_y"])}" r="4" fill="{color}"/>')
  svg.append(f'<text x="1010" y="{y0+230}" font-size="16">Cyan: local concreteMesh</text><text x="1010" y="{y0+250}" font-size="16">Coral: unlike/distant surface</text>')
 svg.append('<text x="30" y="995" font-size="16">Dashed X1272/1592 references are comparison axes only. Numeric file retains every component and exact eye/hit Z.</text>')
 for j,limit in enumerate(limits):
  low,high=limit['native_y_interval'];svg.append(f'<text x="30" y="{1030+j*30}" font-size="16">{limit["side"]}: first-facing limit Y[{low:.8f},{high:.8f}] atZ0, two independent X origins. Body end remains separate.</text>')
 if heights:
  sx=lambda x:100+(x-450)*.6;sz=lambda z:1360-z*1.5
  svg.append('<text x="30" y="1105" font-size="20">016 / fixed Y750 height checks, both X origins</text>')
  for x in [1272,1592]:svg.append(f'<path d="M{sx(x)},1140V1380" stroke="#8296a7" stroke-dasharray="5 5"/>')
  for z in [0,20,40,64,96,128]:svg.append(f'<text x="30" y="{sz(z)+5}" font-size="15">Z{z}</text>')
  for p in heights:
   color='#49f6e0' if p['local_mesh'] else '#ff926e';svg.append(f'<circle cx="{sx(p["hit"][0])}" cy="{sz(p["hit"][2])}" r="4" fill="{color}"/>')
  svg.append('<text x="30" y="1410" font-size="16">Local firstMesh limits differ by side; remote upper hits are separate architecture. Highest cap and ground contact remain separate.</text>')
 svg.append('</g></svg>')
 (ref/'PIT_UPPER_SIDE_CHECKS.svg').write_text('\n'.join(svg)+'\n')
 print(f'{len(rows)} repeated first-hit points; no new physical rows; Gate1 FAIL')

if __name__=='__main__':main()
