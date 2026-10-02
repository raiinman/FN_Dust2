"""Native cross-marker and clean camera captures; no entity/asset extraction.

--plan JSON --session QUEUE --addon PATH --output PRIVATE_DIRECTORY.
Plan: id/build/pose[x,y,z,pitch,yaw], anchors[{id,point[x,y,z],half_size}].
Optional marker_plane is XY (default), XZ or YZ for the visible cross axes.
Drawline crosses settle before a separate screenshot request. Independent image/pixel
review is required; this helper never grants geometric calibration acceptance.
"""
import argparse,hashlib,json,math,re,shutil
from datetime import datetime,timezone
from pathlib import Path
from cs2_console import request_exchange
from cs2_capture import preview_tga

def run(a):
    plan=json.loads(a.plan.read_text());base=plan['id'];pose=plan['pose']
    assert re.fullmatch(r'[A-Za-z0-9_]{1,50}',base) and len(pose)==5
    assert plan.get('debug_overlay_initially_visible') is True,'Observe visible debug marks before running; visibility cannot be inferred from cvar defaults'
    assert len(plan['anchors'])>=6 and all(math.isfinite(v) for v in pose)
    plane=plan.get('marker_plane','XY');assert plane in ['XY','XZ','YZ']
    draw=[]
    for anchor in plan['anchors']:
        x,y,z=anchor['point'];d=anchor['half_size']
        assert all(math.isfinite(v) for v in [x,y,z,d]) and 10<=d<=200
        for axis in {'XY':[0,1],'XZ':[0,2],'YZ':[1,2]}[plane]:
            start=[x,y,z];end=[x,y,z];start[axis]-=d;end[axis]+=d
            draw.append('drawline '+' '.join(str(v) for v in start+end))
    output=a.output.resolve();repo=Path(__file__).resolve().parent.parent
    assert output!=repo and repo not in output.parents
    output.mkdir(parents=True,exist_ok=True)
    ids=[base+'_MARKED',base+'_CLEAN']
    assert all(not (output/(i+ext)).exists() for i in ids for ext in ['.json','.tga','_attempt.json'])
    serial=0
    def send(cmd,seconds=.5):
        nonlocal serial
        serial+=1;marker=f'FN_CAMERA_CAL_{serial}'
        lines=request_exchange(a.session,cmd+'; echo '+marker,seconds)['received_prints']
        assert any(s.strip()==marker for s in lines),'Missing live echo; inspect queue'
        return lines
    send(f'setpos_exact {pose[0]} {pose[1]} {pose[2]}; setang_exact {pose[3]} {pose[4]} 0',1)
    observed=next(s.strip() for s in send('getpos_exact') if s.startswith('setpos_exact '))
    values=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',observed)]
    assert max(abs(values[i]-pose[i]) for i in range(4))<=.01
    assert abs((values[4]-pose[4]+180)%360-180)<=.01
    hidden=False
    try:
        for i in ids:
            if i.endswith('_CLEAN'):
                send('debugoverlay_toggle');hidden=True
            send('ent_clear_debug_overlays; cl_ent_clear_debug_overlays')
            basename='d2_'+hashlib.sha256(i.encode()).hexdigest()[:10]
            attempt=dict(id=i,timestamp_utc=datetime.now(timezone.utc).isoformat(),pose_command=observed,engine_capture_basename=basename,status='screenshot pending')
            (output/(i+'_attempt.json')).write_text(json.dumps(attempt,indent=2)+'\n')
            if i.endswith('_MARKED'):
                # A same-request screenshot can show the preceding overlay frame.
                # Return a game tick before capturing the new native primitives.
                attempt['draw_received_prints']=send('; '.join(draw),1)
            lines=send(f'screenshot {basename}',3)
            attempt.update(received_prints=lines,status='screenshot command returned');(output/(i+'_attempt.json')).write_text(json.dumps(attempt,indent=2)+'\n')
            names=[m.group(1).strip() for s in lines if (m:=re.search(r'Screenshot written to: (.+)',s))]
            assert len(names)==1
            source=(a.addon.resolve()/names[0]).resolve();assert a.addon.resolve() in source.parents and source.suffix.lower()=='.tga'
            tga=output/(i+'.tga');shutil.copyfile(source,tga);png=output/(i+'.png');width,height=preview_tga(tga,png)
            result=dict(id=i,timestamp_utc=attempt['timestamp_utc'],engine_capture_basename=basename,pose_command=observed,pose_unit='source_units',width=width,height=height,requested_pose=pose,source_build=plan['build'],source_map='de_dust2',tga_sha256=hashlib.sha256(tga.read_bytes()).hexdigest(),png_sha256=hashlib.sha256(png.read_bytes()).hexdigest(),anchors=plan['anchors'] if i.endswith('_MARKED') else [],status='captured; requires native image and projection review')
            result['marker_plane']=plane
            (output/(i+'.json')).write_text(json.dumps(result,indent=2)+'\n');print(i,flush=True)
    finally:
        send('ent_clear_debug_overlays; cl_ent_clear_debug_overlays')
        if hidden:send('debugoverlay_toggle')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['plan','session','addon','output']:p.add_argument('--'+name,type=Path,required=True)
    run(p.parse_args())
