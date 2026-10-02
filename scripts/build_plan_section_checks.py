"""Check fresh angular midpoint rays against predictions fixed before capture.

Rebuild PLAN_SECTION_CHECKS.csv from PLAN_SECTION_CHECKS.json. Baseline hashes,
native repeated hits and rangefinder distances are validated. Chord errors are
diagnostics, never a universal surface bound or whole-footprint acceptance.
"""
import csv,hashlib,json,math,re
from pathlib import Path

def cross(a,b):return a[0]*b[1]-a[1]*b[0]

def build(root):
 ref=root/'reference';data=json.loads((ref/'PLAN_SECTION_CHECKS.json').read_text());factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
 rows=[]
 for model in data['models']:
  baseline=model['baseline_report'];assert hashlib.sha256(json.dumps(baseline,sort_keys=True).encode()).hexdigest()==model['baseline_report_sha256']
  r=model['check_report'];assert r['status'].startswith('complete') and max(r['restore_numeric_errors'])<=.01 and r['source_build']==baseline['source_build']==data['source_build']
  station=baseline['config']['stations'][0];pose=station['pose'];points={o['yaw']:o['hit'] for o in baseline['observations'] if o['repeat']==2}
  assert r['config']==model['config'] and r['config']['stations'][0]['pose']==pose and len(r['observations'])==2*len(model['cases'])
  for case in model['cases']:
   angle=case['yaw'];a=[points[case['bracket_yaws'][0]][j]-pose[j] for j in (0,1)];b=[points[case['bracket_yaws'][1]][j]-pose[j] for j in (0,1)];edge=[b[j]-a[j] for j in (0,1)];direction=[math.cos(math.radians(angle)),math.sin(math.radians(angle))];radius=cross(a,edge)/cross(direction,edge);predicted=[pose[0]+radius*direction[0],pose[1]+radius*direction[1],pose[2]+64];assert math.dist(predicted,case['predicted_hit'])<1e-7
   obs=[o for o in r['observations'] if o['yaw']==angle];assert len(obs)==2 and obs[0]['hit']==obs[1]['hit'] and obs[0]['surface']==obs[1]['surface']
   for o in obs:
    distance=re.search(r'DISTANCE:\s+(-?\d+(?:\.\d+)?) inches',o['rangefinder_reply']);assert distance and abs(float(distance.group(1))-math.dist(o['eye_origin'],o['hit']))<=.02
   error=math.dist(predicted,obs[0]['hit']);rows.append(dict(area=baseline['area'],baseline=baseline['id'],check_report=r['id'],yaw=angle,bracket_yaws=str(case['bracket_yaws']),predicted_native=str(predicted),observed_native=str(obs[0]['hit']),error_cm=round(error*factor,6),surface=str(obs[0]['surface']),result='agrees at checked point only' if error<=data['local_agreement_threshold_native'] else 'candidate chord rejected',limits='Independent point diagnostic; no unseen surface, portal edge or rendered-offset bound'))
 with (ref/'PLAN_SECTION_CHECKS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 for area in sorted({r['area'] for r in rows}):
  rr=[r for r in rows if r['area']==area];print(area,len(rr),'checks;',sum(r['result']=='candidate chord rejected' for r in rr),'rejected chords; maximum',max(r['error_cm'] for r in rr),'cm')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
