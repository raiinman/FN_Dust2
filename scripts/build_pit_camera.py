"""Validate the locked native Pit camera with eight fit/eight held-out crosses.

Run python scripts/build_pit_camera.py after reviewed pixel registration. Fits
four intrinsic parameters to the empirically supported zero-roll camera offset,
checks independent holdouts, hashes and fixed-Z inverse. Local camera only;
reject translated unconstrained overhead matrix outside its tested range.
"""
import base64,hashlib,json,math
from pathlib import Path

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def line(q,v):
 n=len(q);slope=(n*sum(a*b for a,b in zip(q,v))-sum(q)*sum(v))/(n*sum(a*a for a in q)-sum(q)**2)
 return slope,(sum(v)-slope*sum(q))/n

def build(root):
 ref=root/'reference';a=json.loads((ref/'PIT_CAMERA_CALIBRATION.json').read_text());pose=a['observed_pose'];assert len(pose)==6 and pose[-1]==0
 assert a['image_size']==[1280,720] and a['fov_cs_debug_parameter']==90
 pitch,yaw=[math.radians(v) for v in pose[3:5]]
 up=[math.sin(pitch)*math.cos(yaw),math.sin(pitch)*math.sin(yaw),math.cos(pitch)]
 forward=[math.cos(pitch)*math.cos(yaw),math.cos(pitch)*math.sin(yaw),-math.sin(pitch)]
 right=[math.sin(yaw),-math.cos(yaw),0];eye=[pose[i]+64*up[i] for i in range(3)]
 def normalized(world):
  delta=[world[i]-eye[i] for i in range(3)];depth=dot(delta,forward);assert depth>0
  return dot(delta,right)/depth,-dot(delta,up)/depth
 fit=a['fit_anchors'];hold=a['holdout_anchors'];assert len(fit)==len(hold)==8 and not {x['id'] for x in fit}&{x['id'] for x in hold}
 fx,cx=line([normalized(x['world'])[0] for x in fit],[x['pixel'][0] for x in fit])
 fy,cy=line([normalized(x['world'])[1] for x in fit],[x['pixel'][1] for x in fit]);assert fx>0 and fy>0 and abs(fx/fy-1)<.005
 def project(world):
  u,v=normalized(world);return [cx+fx*u,cy+fy*v]
 def inverse(pixel,z):
  u,v=(pixel[0]-cx)/fx,(pixel[1]-cy)/fy;direction=[forward[i]+u*right[i]-v*up[i] for i in range(3)];t=(z-eye[2])/direction[2];assert t>0
  return [eye[i]+t*direction[i] for i in range(3)]
 for group in [fit,hold]:
  for x in group:x['projected_pixel']=project(x['world']);x['residual_px']=math.dist(x['pixel'],x['projected_pixel'])
 fitmax=max(x['residual_px'] for x in fit);holdmax=max(x['residual_px'] for x in hold);assert fitmax<1 and holdmax<1
 for c in a['captures']:assert hashlib.sha256((root/c['repository_image_path']).read_bytes()).hexdigest()==c['jpeg_sha256']
 bounds=[]
 for z in [-200,-100,0,80]:
  displacements=[]
  for x in hold:
   p=[*x['world'][:2],z];uv=project(p);assert math.dist(inverse(uv,z),p)<1e-8
   for du,dv in [(1.5,0),(-1.5,0),(0,1.5),(0,-1.5)]:displacements.append(math.dist(inverse([uv[0]+du,uv[1]+dv],z),p)*2.54)
  bounds.append(dict(source_z=z,max_1_5px_axis_displacement_cm=max(displacements)))
 a.update(status='ACCEPTED locked local projection; surface boundaries remain separate',intrinsics=dict(fx=fx,fy=fy,cx=cx,cy=cy),fit_max_residual_px=fitmax,holdout_max_residual_px=holdmax,validated_source_z_range=[-200,80],sampled_pixel_bounds=bounds,limits='Locked1400,450,400 p88.999908/y90/roll0,1280x720,FOV parameter90 only. Eight independent native holdouts include low Pit elevations. No other pose/intrinsic transfer accepted; fixed-Z inverse needs independently measured surface Z. Marker pixels are not rendered edge coordinates or render/collision agreement.')
 (ref/'PIT_CAMERA_CALIBRATION.json').write_text(json.dumps(a,indent=2)+'\n')
 clean=next(c for c in a['captures'] if c['id']=='QA_PIT_CAMERA_TRANSFER_001_CLEAN');data=base64.b64encode((root/clean['repository_image_path']).read_bytes()).decode()
 floor=json.loads((ref/'PIT_FLOOR_INTERPOLATION.json').read_text());parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1030" viewBox="0 0 1440 1030">','<rect width="1440" height="1030" fill="#12202b"/>','<g fill="#edf4f8" font-family="sans-serif"><text x="40" y="38" font-size="24">Pit calibrated native floor-strip diagnostic</text>',f'<text x="40" y="68" font-size="16">8 local fit / 8 independent camera checks; max{holdmax:.3f}px. Floor interpolation remains separately reviewed.</text></g>',f'<image x="40" y="95" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>']
 for triangle in floor['triangles']:
  pixels=[project(h) for h in triangle['source_xyz']]
  parts.append('<polygon points="'+' '.join(f'{u+40:.2f},{v+95:.2f}' for u,v in pixels)+'" fill="#24c8ed" fill-opacity=".08" stroke="#24c8ed" stroke-opacity=".5" stroke-width="1"/>')
 parts+=['<g fill="#edf4f8" font-family="sans-serif" font-size="16">','<text x="40" y="860">Cyan triangles project independently surveyed floor points. Near-wall gaps, cap surfaces and full Pit ends remain separate.</text>','<text x="40" y="895">Foreground roof/caps can hide surveyed floor. Projection does not certify visibility or identify rendered architectural edges.</text>',f'<text x="40" y="930">Checked floor interpolation error: {floor["max_observed_residual_cm"]:.3f}cm. Pixel allowance1.5px requires known surface elevation.</text>','<text x="40" y="965">Translated overhead matrix rejected at21.657px maximum error. This camera was fitted locally and checked independently.</text>','<text x="40" y="1000">Gate1 remains FAIL: full critical dimensions, continuous layered whole-map footprint and bounded uncertainty incomplete.</text>','</g></svg>']
 (ref/'PIT_CAMERA_FLOOR_PLAN.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
 print(json.dumps(dict(intrinsics=a['intrinsics'],fit_max_px=fitmax,holdout_max_px=holdmax,validated_z_range=a['validated_source_z_range'],gate1='FAIL')))
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
