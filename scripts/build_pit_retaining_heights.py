"""Validate local Pit plaster/Rock facing interfaces and cap/ground points.

PIT_RETAINING_HEIGHT_REVIEW explicitly selects repeated independent-origin
native reports. Rebuild JSON/CSV/SVG, render and inspect. Absolute first-facing
Z bounds are not highest cap, hidden body base or entire wall height. Separate
corrected first-down cap and adjacent-ground samples retain their actual XY.
"""
import csv,json,math,re
from pathlib import Path
from build_connector_profile import points

def cap_chord(selection,reports):
 if 'cap_section' not in selection:return None
 s=selection['cap_section'];r=reports[s['report']]
 assert r['source_build']=='25640462' and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01
 accepted=next(v for v in r['accepted_endpoint_spans'] if v['id']==s['measurement_id'])
 endpoints=[]
 for role,yaw in [('low',0),('high',180)]:
  selected=[]
  assert accepted[role]==s[role]
  for key in [role,role+'_check']:
   selector=s[key];assert selector['yaw']==yaw
   station=next(v for v in r['config']['stations'] if v['id']==selector['station_id'])
   a,o=[o for o in r['observations'] if o['station_id']==selector['station_id'] and o['yaw']==yaw]
   assert a['repeat']==1 and o['repeat']==2 and a['hit']==o['hit'] and a['surface']==o['surface'] and a['pose']==o['pose']
   v=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',o['pose'])];eye=v[:2]+[v[2]+64]
   assert len(v)==6 and math.dist(v[:3],station['pose'])<=.01 and math.dist(eye,o['eye_origin'])<=.01
   assert abs(v[3])<=.01 and abs(v[5])<=.01 and abs((v[4]-yaw+180)%360-180)<=.01
   assert math.dist(eye,o['hit'])>.1 and abs(float(o['rangefinder_reply'].split()[1])-math.dist(eye,o['hit']))<=.02
   assert 'surfaceprop rock,' in str(o['surface']) and 'shape type: Hull,' in str(o['surface'])
   assert abs(o['hit'][1]-eye[1])<=.02 and abs(o['hit'][2]-eye[2])<=.02
   selected.append(o)
  assert selected[0]['hit']==selected[1]['hit'] and selected[0]['surface']==selected[1]['surface']
  assert selected[0]['eye_origin'][0]!=selected[1]['eye_origin'][0];endpoints.append(selected[0]['hit'])
 low,high=endpoints;assert low[1:]==high[1:] and high[0]>low[0]
 return dict(report=r['id'],measurement_id=s['measurement_id'],low=low,high=high,width_cm=2.54*(high[0]-low[0]),scope=accepted['notes'])

def sections(ref):
 spec=json.loads((ref/'PIT_RETAINING_HEIGHT_REVIEW.json').read_text())
 arch=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text());profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());floor_points=points(profile)
 reports={r['id']:r for r in arch['reports']};columns={r['id']:r for r in profile['reports']};rows=[]
 pad=spec['numerical_allowance_native'];assert pad==.01 and spec['source_build']=='25640462'
 for selection in spec['selections']:
  r=reports[selection['report']];c=r['config']
  assert r['source_build']==spec['source_build'] and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01
  assert c['normal_axis']==0 and c['tangent_axis']==2 and c['normal_band_is_classifier'] and c['maximum_bracket_native']<=.1
  assert c['on_material']=='concrete' and c['on_shape']=='Mesh' and c['off_material']=='rock' and c['off_shape']=='Hull'
  assert len(c['origins'])==2 and len({o['normal_coordinate'] for o in c['origins']})==2 and len(r['brackets'])==2
  intervals=[];native=[]
  for bracket in r['brackets']:
   origin=next(o for o in c['origins'] if o['id']==bracket['origin_id']);assert origin['fixed_lateral_native']==750
   interval=bracket['tangent_interval_native'];assert interval[1]-interval[0]<=.1;intervals.append(interval)
   for key,mat,shape in [('on','concrete','Mesh'),('off','rock','Hull')]:
    index=bracket[key]['observation_index'];a,o=r['observations'][index-1:index+1]
    assert a['repeat']==1 and o['repeat']==2 and a['hit']==o['hit'] and a['surface']==o['surface'] and a['pose']==o['pose']
    assert o['origin_id']==origin['id'] and bracket[key]['on_component']==(key=='on')
    assert 'surfaceprop '+mat+',' in str(o['surface']) and 'shape type: '+shape+',' in str(o['surface'])
    v=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',o['pose'])];eye=v[:2]+[v[2]+64]
    assert len(v)==6 and math.dist(eye,o['eye_origin'])<=.01 and abs(eye[0]-origin['normal_coordinate'])<=.01 and abs(eye[1]-750)<=.01
    assert abs(eye[2]-bracket[key]['coordinate'])<=.01 and abs(v[3])<=.01 and abs(v[5])<=.01 and abs((v[4]-origin['yaw']+180)%360-180)<=.01
    assert math.dist(eye,o['hit'])>.1 and abs(float(o['rangefinder_reply'].split()[1])-math.dist(eye,o['hit']))<=.02
    assert abs(o['hit'][1]-750)<=.02 and abs(o['hit'][2]-eye[2])<=.02
    if key=='on':assert origin['on_normal_band'][0]<=o['hit'][0]<=origin['on_normal_band'][1]
    native.append(dict(origin=origin['id'],component=key,point=o['hit'],surface=o['surface']))
  assert intervals[0]==intervals[1]
  elevations=[2.54*(intervals[0][0]-pad),2.54*(intervals[0][1]+pad)]
  selected=[]
  for id in selection.get('cap_ground_reports',[]):
   column=columns[id];point=floor_points[id];assert column['source_build']==spec['source_build'] and abs(point[1]-750)<=.02
   selected.append(dict(report=id,point=point,surface=column['observations'][-1]['hit_description'],semantics=column['surface_semantics']))
  rows.append(dict(id=selection['measurement_id'],side=selection['side'],report=r['id'],native_y=750,facing_interface_z_interval=intervals[0],elevation_interval_cm=elevations,interface_points=native,cap_ground_points=selected,cap_chord=cap_chord(selection,reports),scope='Absolute sourceZ0-referenced local firstMesh/Rock facing interface. Cap overhang/relief can occlude continuation; not highest cap or floor-to-top/full body height. Native cap/ground points retain differentX.'))
 return rows

def measurement_rows(ref):
 result=[]
 for r in sections(ref):
  lo,hi=r['elevation_interval_cm']
  result.append(dict(id=r['id'],area='Pit',feature=f'{r["side"]} local plaster/Rock first-facing upper interface at nativeY750',value=round((lo+hi)/2,5),unit='cm',method='two independent outside origins; repeated firstMesh/Rock height brackets; SCALE_CALIBRATION',source_id='PIT_RETAINING_HEIGHT_REVIEW/'+r['report'],confidence='confirmed bounded local collision-facing elevation',tolerance=f'Interval[{lo:.6f},{hi:.6f}]cm including .01native allowance; sourceZ0 datum',notes=r['scope']))
 return result

def main():
 ref=Path('reference');rows=sections(ref)
 (ref/'PIT_RETAINING_HEIGHTS.json').write_text(json.dumps(dict(source_build='25640462',sections=rows,gate1='FAIL'),indent=2)+'\n')
 measurements=measurement_rows(ref)
 with (ref/'PIT_RETAINING_HEIGHTS.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(measurements[0]));w.writeheader();w.writerows(measurements)
 svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="950"><rect width="1400" height="950" fill="#14202e"/><g font-family="Arial" fill="white"><text x="30" y="40" font-size="25">Pit upper retaining sections / plaster, cap and adjacent ground</text><text x="30" y="75" font-size="17">Native XZ points at Y750. First-facing interfaces are separate from full cap, ground contact and entire body.</text>']
 for j,r in enumerate(rows):
  left=35+j*690;normal=1272 if r['side']=='WEST' else 1592
  sx=lambda x:left+330+(x-normal)*9;sz=lambda z:610-z*4
  svg.append(f'<text x="{left}" y="135" font-size="22">{r["side"]} / first plaster-to-Rock interval</text>')
  lo,hi=r['elevation_interval_cm'];svg.append(f'<text x="{left}" y="170" font-size="16">Absolute sourceZ0 elevation [{lo:.4f},{hi:.4f}]cm</text>')
  if r['cap_chord']:
   chord=r['cap_chord'];low,high=chord['low'],chord['high']
   svg.append(f'<text x="{left}" y="205" font-size="16">Sampled Rockcap width{chord["width_cm"]:.4f}cm atZ{low[2]:.0f}</text>')
   svg.append(f'<path d="M{sx(low[0])},{sz(low[2])}H{sx(high[0])}" stroke="#ffffff" stroke-dasharray="5 5"/>')
   for point in [low,high]:svg.append(f'<circle cx="{sx(point[0])}" cy="{sz(point[2])}" r="4" fill="#ffffff"/>')
  for z in [-30,0,20,40,60,80]:svg.append(f'<text x="{left}" y="{sz(z)+5}" font-size="15">Z{z}</text><path d="M{left+65},{sz(z)}h545" stroke="#506477"/>')
  unique=set()
  for p in r['interface_points']:
   point=p['point'];key=tuple(point)
   if key in unique:continue
   unique.add(key);color='#ffc75d' if p['component']=='on' else '#ca92ff';svg.append(f'<circle cx="{sx(point[0])}" cy="{sz(point[2])}" r="4" fill="{color}"/>')
  for p in r['cap_ground_points']:
   point=p['point'];svg.append(f'<circle cx="{sx(point[0])}" cy="{sz(point[2])}" r="5" fill="#49f6e0"/><text x="{sx(point[0])-40}" y="{sz(point[2])-18}" font-size="14">X{point[0]:.2f}/Z{point[2]:.2f}</text>')
 svg.append('<text x="30" y="800" font-size="16">Amber: repeated plaster first hit. Purple: adjacent Rock Hull first hit. Cyan: independently corrected cap/ground points.</text><text x="30" y="835" font-size="16">No connecting body surface, highest-cap envelope, hidden base or exact floor contact inferred. Gate1 remains FAIL.</text></g></svg>')
 (ref/'PIT_RETAINING_HEIGHTS.svg').write_text('\n'.join(svg)+'\n')
 print([(r['side'],r['elevation_interval_cm']) for r in rows])

if __name__=='__main__':main()
