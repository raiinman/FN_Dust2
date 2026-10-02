"""Validate native route-axis rays and derive diagnostic spans/open directions.

Input ROUTE_AXIS_SECTIONS.json and independently repeated connector floor data.
Two opposite axis hits define a local ray span only: materials/remote portals,
slopes and unsupported ray masks remain explicit. No full player clearance,
minimum whole-route width or architectural boundary accepted automatically.
"""
import csv,json,math,re
from pathlib import Path
from build_connector_profile import points

def build(root):
 ref=root/'reference';data=json.loads((ref/'ROUTE_AXIS_SECTIONS.json').read_text());profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());p=points(profile);factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54;rows=[];opened=[]
 for report in data['reports']:
  assert report['status'].startswith('complete') and max(report['restore_numeric_errors'])<=.01 and report['source_build']==data['source_build']==profile['source_build']
  for station in report['config']['stations']:
   floor=p[station['source_floor_report']];height=station['height_above_measured_floor_native'];axis=station['section_axis'];assert axis in (0,1) and station['yaws']==([0,180] if axis==0 else [90,-90]);assert math.dist(floor[:2],station['pose'][:2])<=.02 and abs(station['pose'][2]+64-floor[2]-height)<=.02
   samples=[]
   for yaw in station['yaws']:
    obs=[o for o in report['observations'] if o['station_id']==station['id'] and o['yaw']==yaw];miss=[o for o in report.get('open_observations',[]) if o['station_id']==station['id'] and o['yaw']==yaw]
    if miss:
     assert not obs and len(miss)==2 and report['config']['allow_open_rays'] and all(o['semantic_reply']==["Rangefinder didn't hit anything"] for o in miss);opened.append(dict(report=report['id'],station=station['id'],route=station['route'],yaw=yaw,eye_origin_native=str(miss[0]['eye_origin']),limits='Two native misses; no endpoint/distance. No absent playerclip, floor boundary or rendered-edge inference.'));continue
    assert len(obs)==2 and obs[0]['hit']==obs[1]['hit'] and obs[0]['surface']==obs[1]['surface']
    for o in obs:
     d=re.search(r'DISTANCE:\s+(-?\d+(?:\.\d+)?) inches',o['rangefinder_reply']);assert d and abs(float(d.group(1))-math.dist(o['eye_origin'],o['hit']))<=.02 and math.dist(o['eye_origin'],o['hit'])>.1 and abs(o['hit'][2]-floor[2]-height)<=.02
    samples.append(obs[0])
   if len(samples)!=2:continue
   hi,lo=samples;assert hi['hit'][axis]>floor[axis]>lo['hit'][axis] and all(abs(hi['hit'][i]-lo['hit'][i])<=.02 for i in range(3) if i!=axis)
   rows.append(dict(report=report['id'],station=station['id'],route=station['route'],floor_report=station['source_floor_report'],floor_native=str(floor),height_above_floor_native=height,axis='XY'[axis],low_native=str(lo['hit']),high_native=str(hi['hit']),span_cm=round(math.dist(hi['hit'],lo['hit'])*factor,4),low_surface=str(lo['surface']),high_surface=str(hi['surface']),confidence='confirmed repeated native first-hit ray span',limits='Diagnostic local ray span: diagonal route turns are not normal sections; cover, slope, cross-area hits and unknown playerclip ray-mask coverage preclude automatic whole-route minimum/architectural boundary acceptance.'))
 for name,rr in [('ROUTE_AXIS_SPANS.csv',rows),('ROUTE_AXIS_OPEN_RAYS.csv',opened)]:
  if rr:
   with (ref/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rr[0]);w.writeheader();w.writerows(rr)
 print(len(rows),'validated diagnostic axis spans;',len(opened),'native no-hit directions; no full clearance/footprint acceptance')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
