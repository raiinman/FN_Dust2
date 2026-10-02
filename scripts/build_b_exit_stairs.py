"""Rebuild sampled B entrance center stair evidence from reviewed native rays.

Validates four repeated center/lateral face positions, corrected tread/ground
points and full outside-image hash/count. Writes CSV/SVG and three calibrated
inter-face run rows. Full curved sides and unsampled ground remain separate.
"""
import csv,hashlib,json,math,re
from pathlib import Path
from build_connector_profile import points

def rows(ref):
 a=json.loads((ref/'B_EXIT_STAIR_PROFILE.json').read_text());profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());p=points(profile);reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']};factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54 and profile['source_build']==a['source_build']
 image=a['rendered_review'];assert hashlib.sha256((ref.parent/image['image_path']).read_bytes()).hexdigest()==image['sha256'] and image['count']==len(a['tread_reports'])==len(a['eye_levels'])==4
 faces={}
 for x in [a['center_x']]+a['lateral_x']:
  r=reports[a['center_face_report'] if x==a['center_x'] else a['lateral_face_report']];assert r['status'].startswith('complete') and max(r['restore_numeric_errors'])<=.01 and r['source_build']==a['source_build']
  for eye in a['eye_levels']:
   station=f'B_EXIT_FACE_EYE{eye}' if x==a['center_x'] else f'B_EXIT_X{abs(x)}_EYE{eye}';obs=[o for o in r['observations'] if o['station_id']==station];assert len(obs)==2 and obs[0]['hit']==obs[1]['hit'] and obs[0]['surface']==obs[1]['surface']
   for o in obs:
    assert o['yaw']==-90 and o['hit'][0]==x and o['hit'][2]==eye and 'surfaceprop concrete' in str(o['surface']) and 'shape type: Hull' in str(o['surface'])
    d=re.search(r'DISTANCE:\s+(-?\d+(?:\.\d+)?) inches',o['rangefinder_reply']);assert d and abs(float(d.group(1))-math.dist(o['eye_origin'],o['hit']))<=.02
   faces[x,eye]=obs[0]['hit'][1]
 for eye in a['eye_levels']:assert len({faces[x,eye] for x in [a['center_x']]+a['lateral_x']})==1
 assert not set(a['excluded_tread_reports'])&set(a['tread_reports']);ground=p[a['lower_ground_report']];assert ground[0]==a['center_x'] and 0<ground[1]-faces[a['center_x'],a['eye_levels'][0]]<.2
 result=[];lower=ground
 for i,(eye,id) in enumerate(zip(a['eye_levels'],a['tread_reports'])):
  upper=p[id];face=faces[a['center_x'],eye];assert upper[0]==a['center_x'] and upper[1]<face and upper[2]>lower[2]
  next_face=faces[a['center_x'],a['eye_levels'][i+1]] if i<3 else None
  result.append(dict(id='B_EXIT_RISER_'+str(i+1),face_y_native=face,lower_z_native=lower[2],upper_z_native=upper[2],rise_cm=round((upper[2]-lower[2])*factor,4),run_to_next_face_cm=round((face-next_face)*factor,4) if next_face is not None else '',limits=a['limits']));lower=upper
 return result

def measurement_rows(ref):
 return [dict(id=r['id']+'_RUN_TO_NEXT_FACE',area='B Tunnel Exit',feature='Center concrete riser-face interval '+r['id'],value=r['run_to_next_face_cm'],unit='cm',method='repeated concrete face endpoints, two independent lateral checks; SCALE_CALIBRATION',source_id='B_EXIT_STAIR_PROFILE/'+r['id'],confidence='confirmed repeated sampled collision interval',tolerance='.0508 cm endpoint rounding; full curved sides/terminal bounds separate',notes=r['limits']) for r in rows(ref) if r['run_to_next_face_cm']!='']

def build(root):
 ref=root/'reference';flight=rows(ref)
 with (ref/'B_EXIT_STAIR_FLIGHT.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=flight[0]);w.writeheader();w.writerows(flight)
 first=flight[0]['face_y_native'];bottom=flight[0]['lower_z_native'];sx=lambda y:170+(first-y)*17;sy=lambda z:390-(z-bottom)*9
 svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650">','<rect width="1100" height="650" fill="#12202b"/>','<g fill="#edf4f8" font-family="Arial">','<text x="35" y="38" font-size="24">B tunnel entrance — sampled four-step center section</text>','<text x="35" y="68" font-size="16">Native concrete riser faces agree at X-2008/-1984/-1960. Scale2.54cm/native.</text>']
 path=[f'M{sx(first)+0:g},{sy(bottom):g}']
 for i,row in enumerate(flight):
  x=sx(row['face_y_native']);lo,hi=sy(row['lower_z_native']),sy(row['upper_z_native']);path.extend([f'L{x:g},{lo:g}',f'L{x:g},{hi:g}']);svg.append(f'<text x="{x+9:g}" y="{(lo+hi)/2:g}" font-size="15">{row["rise_cm"]:g}cm</text>')
  if i<3:
   end=sx(flight[i+1]['face_y_native']);path.append(f'L{end:g},{hi:g}');svg.append(f'<text x="{(x+end)/2:g}" y="{hi-12:g}" text-anchor="middle" font-size="15">{row["run_to_next_face_cm"]:g}cm</text>')
  svg.append(f'<text x="{x:g}" y="425" text-anchor="middle" font-size="13">Y{row["face_y_native"]:g}</text>')
 svg.append('<path d="'+' '.join(path)+'" fill="none" stroke="#72ddd3" stroke-width="4"/>')
 total=round(sum(r['rise_cm'] for r in flight),4);run=round(sum(r['run_to_next_face_cm'] for r in flight if r['run_to_next_face_cm']!=''),4)
 svg.extend([f'<text x="35" y="470" font-size="18">Sampled ground-to-upper-tread rise{total:g}cm · three inter-face intervals total{run:g}cm.</text>','<text x="35" y="505" font-size="16">First ground sample is.17native before lowest face; slight ground slope is not a uniform8native rise.</text>','<text x="35" y="535" font-size="16">Four rendered principal steps independently reviewed; anomalous Y1816 lower Mesh excluded.</text>','<text x="35" y="565" font-size="16">Diagram is a sampled center section; curved full sides, exact terminal contact and upper landing unaccepted.</text>','<text x="35" y="595" font-size="16">48native lateral face checks do not certify whole-width interpolation or rendered/collision offset.</text>','</g></svg>']);(ref/'B_EXIT_STAIR_PROFILE.svg').write_text('\n'.join(svg)+'\n');print('Four sampled rises;',total,'cm;three face intervals;',run,'cm;full sides pending')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
