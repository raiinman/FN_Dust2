"""Bound a conditional first-hit angular transition at a known local plane.

One verified persistent worker, one source pose, independent repeated rays.
Config brackets an on-plane and off-plane direction. Optional required_shape_type
separates a concrete Mesh facade from an adjacent concrete Hull return. The projected bracket
localizes a visibility transition only; occluding returns/cover may hide a wall
that continues beyond it. No exact full wall endpoint or polygon acceptance.
"""
import argparse,json,math,re
from datetime import datetime,timezone
from pathlib import Path
from cs2_console import request_exchange

NUMBER=r'-?\d+(?:\.\d+)?'

def probe(a):
    assert not a.output.exists(),'Preserve completed/partial evidence before a separately named resume'
    config=json.loads(a.config.read_text());axis=config['axis'];assert axis in [0,1]
    xyz=config['pose'];assert len(xyz)==3
    r=dict(id=config['id'],source_build=config['build'],source_map='de_dust2',timestamp_utc=datetime.now(timezone.utc).isoformat(),config=config,unit='source_units',status='in progress',observations=[],brackets=[],scope=__doc__);serial=0
    def save():a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n')
    def send(command,seconds=.35):
        nonlocal serial
        serial+=1;marker='FN_BOUNDARY_TRANSITION_'+str(serial);lines=request_exchange(a.session,command+'; echo '+marker,seconds)['received_prints'];assert any(s.strip()==marker for s in lines),'No exact live echo';return lines
    def pose():
        ps=[s.strip() for s in send('getpos_exact') if s.startswith('setpos_exact ')];assert len(ps)==1;return ps[0]
    def values(p):return [float(v) for v in re.findall(NUMBER,p)]
    def plane_coordinate(angle):
        direction=[math.cos(math.radians(angle)),math.sin(math.radians(angle))];assert abs(direction[axis])>.001
        radius=(config['plane_native']-xyz[axis])/direction[axis];assert radius>0
        return xyz[1-axis]+radius*direction[1-axis]
    def sample(angle):
        pair=[]
        for repeat in [1,2]:
            send(f'setpos_exact {xyz[0]} {xyz[1]} {xyz[2]}; setang_exact 0 {angle} 0');p=pose();v=values(p)
            assert len(v)==6 and max(abs(v[i]-xyz[i]) for i in range(3))<=.01 and abs(v[3])<=.01 and abs(v[5])<=.01 and abs((v[4]-angle+180)%360-180)<=.01
            lines=send('cast_ray; rangefinder',.6);hits=[m for s in lines if (m:=re.search(r'Hit position: ('+NUMBER+r'), ('+NUMBER+r'), ('+NUMBER+r')',s))];dist=[s.strip() for s in lines if s.startswith('DISTANCE:')];surface=[s.strip() for s in lines if s.startswith('Hit:')]
            assert len(hits)==len(dist)==1 and surface,'No unique native hit; preserve and inspect'
            hit=[float(hits[0].group(i)) for i in [1,2,3]];eye=xyz[:2]+[xyz[2]+64];distance=re.search(r'DISTANCE:\s+('+NUMBER+') inches',dist[0]);assert distance and abs(float(distance.group(1))-math.dist(eye,hit))<=.02 and math.dist(eye,hit)>.1 and abs(hit[2]-eye[2])<=.02
            observation=dict(yaw=angle,repeat=repeat,pose=p,eye_origin=eye,hit=hit,surface=surface,rangefinder_reply=dist[0]);r['observations'].append(observation);pair.append(observation);save()
        assert pair[0]['hit']==pair[1]['hit'] and pair[0]['surface']==pair[1]['surface'],'Inconsistent native repeats'
        on=abs(pair[1]['hit'][axis]-config['plane_native'])<=config['on_plane_tolerance_native'] and 'surfaceprop concrete,' in str(surface)
        if config.get('required_shape_type'):
            assert config['required_shape_type'] in ['Mesh', 'Hull']
            on = on and ('shape type: '+config['required_shape_type']+',') in str(surface)
        return dict(yaw=angle,on_plane=on,projected_plane_coordinate_native=plane_coordinate(angle),observation_index=len(r['observations'])-1)
    original=pose();r['original_pose']=original;save()
    try:
        for case in config['brackets']:
            on,off=[sample(case[key]) for key in ['on_yaw','off_yaw']];assert on['on_plane'] and not off['on_plane'],'Initial bracket does not classify as configured'
            history=[on,off]
            for iteration in range(24):
                width=abs(on['projected_plane_coordinate_native']-off['projected_plane_coordinate_native'])
                if width<=config['maximum_bracket_native']:break
                point=sample((on['yaw']+off['yaw'])/2);history.append(point)
                if point['on_plane']:on=point
                else:off=point
            else:raise RuntimeError('Transition bracket failed to converge')
            r['brackets'].append(dict(id=case['id'],on=on,off=off,projected_coordinate_interval_native=sorted([on['projected_plane_coordinate_native'],off['projected_plane_coordinate_native']]),bracket_width_native=width,history=history,limits='Conditional single-transition first-hit bracket, not full wall endpoint. Ray origin, plane tolerance, material and possible occluding component retained.'))
            save()
        r['status']='complete; conditional first-hit brackets only; component/end-point review pending'
    except BaseException as error:r.update(status='failed; inspect partial rays and restoration before resuming',error=str(error));raise
    finally:
        try:
            send(original);restored=pose();before,after=values(original),values(restored);errors=[abs(x-y) for x,y in zip(before,after)];assert len(errors)==6;errors[4]=abs((after[4]-before[4]+180)%360-180);assert max(errors)<=.01;r.update(restored_pose=restored,restore_numeric_errors=errors)
        except BaseException as error:r['restore_error']=str(error)
        save()
    print(json.dumps(dict(id=r['id'],status=r['status'],brackets=r['brackets'])))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--config',type=Path,required=True);p.add_argument('--session',type=Path,required=True);p.add_argument('--output',type=Path,required=True);probe(p.parse_args())
