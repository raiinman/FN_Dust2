"""Validate repeated A-entry principal risers and derive calibrated flight rows.

Run python scripts/build_a_entry_stairs.py. Repeated horizontal concrete faces
at two lateral positions crosscheck spacing; reviewed flat floor samples define
individual rises. Lower pavement lip and upper sloping landing remain separate.
"""
import csv,json,math,re
from pathlib import Path
from build_connector_profile import points

def rows(ref):
 a=json.loads((ref/'A_ENTRY_STAIR_PROFILE.json').read_text());profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());p=points(profile)
 factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
 r=next(r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports'] if r['id']==a['face_report']);assert r['source_build']==a['source_build']==profile['source_build']
 faces={}
 for x in [1100,1200]:
  for eye in [98,104,112,120]:
   obs=[o for o in r['observations'] if o['station_id']==f'ENTRY_X{x}_EYE{eye}'];assert len(obs)==2 and obs[0]['hit']==obs[1]['hit']
   for o in obs:
    assert o['yaw']==90 and o['hit'][0]==x and o['hit'][2]==eye and all('surfaceprop concrete' in s for s in o['surface'])
    d=re.search(r'DISTANCE:\s+(-?\d+(?:\.\d+)?) inches',o['rangefinder_reply']);assert d and abs(float(d.group(1))-math.dist(o['eye_origin'],o['hit']))<=.02
   faces[x,eye]=obs[0]['hit'][1]
 for eye in [98,104,112,120]:assert faces[1100,eye]==faces[1200,eye]
 assert a['rendered_review']['count']==len(a['principal_risers'])==3
 result=[]
 for item in a['principal_risers']:
  lo,hi=p[item['lower_report']],p[item['upper_report']];assert lo[0]==hi[0]==1100 and hi[2]>lo[2]
  start,end=faces[1100,item['start_face_eye']],faces[1100,item['end_face_eye']];assert end>start
  result.append(dict(id=item['id'],source_y_start=start,source_y_end=end,lower_z=lo[2],upper_z=hi[2],rise_cm=round((hi[2]-lo[2])*factor,4),run_cm=round((end-start)*factor,4),limits=a['limits']))
 return result

def measurement_rows(ref):
 result=[];flight=rows(ref)
 for row in flight:
  for dimension in ['rise','run']:
   result.append(dict(id=row['id']+'_'+dimension.upper(),area='A Site Long entrance steps',feature='Principal center section '+row['id']+' '+dimension,value=row[dimension+'_cm'],unit='cm',method='repeated floor points and two-position repeated concrete faces; SCALE_CALIBRATION',source_id='A_ENTRY_STAIR_PROFILE/'+row['id'],confidence='confirmed repeated collision section',tolerance='.0508 cm endpoint rounding; rendered offsets and full width separate',notes=row['limits']))
 for dimension in ['rise','run']:
  result.append(dict(id='A_ENTRY_PRINCIPAL_FLIGHT_'+dimension.upper(),area='A Site Long entrance steps',feature='Three principal stair center sections total '+dimension,value=round(sum(r[dimension+'_cm'] for r in flight),4),unit='cm',method='three independently measured risers and face intervals; SCALE_CALIBRATION',source_id='A_ENTRY_STAIR_PROFILE',confidence='confirmed repeated collision section',tolerance='.0508 cm outer endpoint rounding; full width and rendered offsets separate',notes='Shallow lower lip excluded; upper sloping pavement separate. '+flight[0]['limits']))
 return result

if __name__=='__main__':
 ref=Path(__file__).resolve().parent.parent/'reference';flight=rows(ref)
 with (ref/'A_ENTRY_STAIR_FLIGHT.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=flight[0]);w.writeheader();w.writerows(flight)
 start=flight[0]['source_y_start'];bottom=flight[0]['lower_z']
 sx=lambda v:170+(v-start)*16
 sy=lambda v:340-(v-bottom)*8
 path=[f'M{sx(start):g},{sy(bottom):g}']
 svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="550" viewBox="0 0 1100 550">','<rect width="1100" height="550" fill="#12202b"/>','<g fill="#edf4f8" font-family="sans-serif">','<text x="35" y="38" font-size="24">A entrance — principal three-step center section</text>','<text x="35" y="68" font-size="16">Repeated floor and two-position face rays; 2.54 cm/native unit. Source X1100.</text>']
 for row in flight:
  end=row['source_y_end'];lo,hi=row['lower_z'],row['upper_z'];path.extend([f'L{sx(end):g},{sy(lo):g}',f'L{sx(end):g},{sy(hi):g}'])
  svg.append(f'<text x="{sx((row["source_y_start"]+end)/2):g}" y="{sy(lo)+28:g}" text-anchor="middle" font-size="16">{row["run_cm"]:g}cm run</text>')
  svg.append(f'<text x="{sx(end)-10:g}" y="{sy((lo+hi)/2)+5:g}" text-anchor="end" font-size="15">{row["rise_cm"]:g}cm rise</text>')
 svg.append('<path d="'+' '.join(path)+'" fill="none" stroke="#72ddd3" stroke-width="4"/>')
 for v in sorted({row[k] for row in flight for k in ['source_y_start','source_y_end']}):
  svg.append(f'<text x="{sx(v):g}" y="395" text-anchor="middle" font-size="14">Y{v:g}</text>')
 svg+=['<text x="35" y="445" font-size="18">Measured principal totals: rise60.96cm; horizontal run91.44cm.</text>','<text x="35" y="475" font-size="16">Shallow pavement lip precedes the first tread; sloping upper landing follows the last riser.</text>','<text x="35" y="505" font-size="16">Section diagram only. Full lateral extent and rendered/collision offsets remain separate.</text>','</g></svg>']
 (ref/'A_ENTRY_STAIR_PROFILE.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
 print(json.dumps(dict(principal_risers=len(flight),rise_cm=sum(r['rise_cm'] for r in flight),run_cm=sum(r['run_cm'] for r in flight),full_width='unaccepted')))
