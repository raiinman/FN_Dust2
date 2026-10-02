"""Check a constrained native plan camera against two poses and32 holdouts.

Eight original overhead markers fit four intrinsic parameters. Original16
overhead holdouts and all16 separate local Pit markers are independent of that
fit. Preserve the rejected translation of the unconstrained matrix. Output
permits the tested two poses; other poses require native held-out checks.
"""
import hashlib,json,math,re
from pathlib import Path
from build_pit_camera import dot,line

def basis(pose):
 assert len(pose)==6 and pose[5]==0
 p,y=map(math.radians,pose[3:5]);up=[math.sin(p)*math.cos(y),math.sin(p)*math.sin(y),math.cos(p)]
 forward=[math.cos(p)*math.cos(y),math.cos(p)*math.sin(y),-math.sin(p)];right=[math.sin(y),-math.cos(y),0]
 return [pose[i]+64*up[i] for i in range(3)],right,up,forward

def normalized(world,pose):
 eye,right,up,forward=basis(pose);delta=[world[i]-eye[i] for i in range(3)];depth=dot(delta,forward);assert depth>0
 return [dot(delta,right)/depth,-dot(delta,up)/depth],depth

def build(root):
 ref=root/'reference';over=json.loads((ref/'MAP_CAMERA_CALIBRATION.json').read_text());pit=json.loads((ref/'PIT_CAMERA_CALIBRATION.json').read_text())
 assert over['source_build']==pit['source_build'] and over['image_size']==pit['image_size']==[1280,720]
 captures=over['captures']+pit['captures'];byid={c['id']:c for c in captures}
 for c in captures:assert hashlib.sha256((root/c['repository_image_path']).read_bytes()).hexdigest()==c['jpeg_sha256']
 groups=[]
 for g in over['groups']:
  pose=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',byid[g['capture_id']]['pose_command'])]
  groups.append(dict(capture_id=g['capture_id'],pose=pose,role=g['role'],anchors=g['anchors']))
 for name,key in [('QA_PIT_CAMERA_TRANSFER_001_MARKED','fit_anchors'),('QA_PIT_CAMERA_HOLDOUT_001_MARKED','holdout_anchors')]:groups.append(dict(capture_id=name,pose=pit['observed_pose'],role='independent separate-pose holdout',anchors=pit[key]))
 fit=groups[0];assert fit['role']=='fit' and len(fit['anchors'])==8
 q=[normalized(a['world'],fit['pose'])[0] for a in fit['anchors']]
 fx,cx=line([v[0] for v in q],[a['pixel'][0] for a in fit['anchors']]);fy,cy=line([v[1] for v in q],[a['pixel'][1] for a in fit['anchors']]);assert abs(fx/fy-1)<.005
 depths=[]
 for g in groups:
  assert g['pose'][3:]==fit['pose'][3:]
  for a in g['anchors']:
   uv,depth=normalized(a['world'],g['pose']);depths.append(depth);a['constrained_projected_pixel']=[cx+fx*uv[0],cy+fy*uv[1]];a['constrained_residual_px']=math.dist(a['constrained_projected_pixel'],a['pixel'])
  g['max_residual_px']=max(a['constrained_residual_px'] for a in g['anchors']);assert g['max_residual_px']<1
 held=sum(len(g['anchors']) for g in groups[1:]);assert held==32
 result=dict(source_build=pit['source_build'],source_map='de_dust2',status='ACCEPTED constrained projection at two tested plan poses; other poses require independent native checks',image_size=[1280,720],intrinsics=dict(fx=fx,fy=fy,cx=cx,cy=cy),groups=groups,captures=captures,poses_validated=[fit['pose'],pit['observed_pose']],independent_holdouts=held,max_independent_residual_px=max(g['max_residual_px'] for g in groups[1:]),checked_forward_depth_range= [min(depths),max(depths)],model='Zero-roll native pose +64 camera_up; fitted fx/fy/cx/cy. Fixed pitch88.999908/yaw90. Authored cross coordinates are independent of pixel extraction.',rejected_unconstrained_transfer=pit['rejected_transfer'],limits='Only two exact poses,1280x720 and fixed observed orientation/settings tested. Additional poses/orientations/resolutions require fresh native marker checks. Floor/wall edge identity, independently known Z, under-roof visibility and render/collision agreement remain separate. No full footprint or Gate1 acceptance.')
 (ref/'PLAN_CAMERA_MODEL.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(intrinsics=result['intrinsics'],independent_holdouts=held,max_independent_px=result['max_independent_residual_px'],poses=len(result['poses_validated']),gate1='FAIL')))
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
