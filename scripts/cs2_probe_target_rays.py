"""Repeat native rays from declared camera eyes toward known target points.

--config JSON --session QUEUE --output PRIVATE_JSON. Config owns id/build/area
and rays [{id,eye[x,y,z],target[x,y,z]}]. The empirically checked64 camera_up
model determines the source pose for each directed ray; observed pose/actual
eye, native first hit/material/rangefinder and target discrepancy are saved.
First-hit agreement is collision evidence, not automatic renderer visibility,
architectural selection, full-body bounds or playerclip acceptance.
"""
import argparse,json,math,re
from datetime import datetime,timezone
from pathlib import Path
from cs2_console import request_exchange

NUMBER=r'-?\d+(?:\.\d+)?'


def numbers(s):return [float(v) for v in re.findall(NUMBER,s)]


def up(pitch,yaw):
    p,y=math.radians(pitch),math.radians(yaw)
    return [math.sin(p)*math.cos(y),math.sin(p)*math.sin(y),math.cos(p)]


def probe(a):
    assert not a.output.exists(),'Preserve previous evidence; choose a separately named output'
    config=json.loads(a.config.read_text());assert config['rays']
    report=dict(id=config['id'],source_build=config['build'],area=config['area'],source_map='de_dust2',timestamp_utc=datetime.now(timezone.utc).isoformat(),config=config,unit='source_units',observations=[],status='in progress',scope=__doc__)
    serial=0
    def save():
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n')
    def send(command,seconds=.6):
        nonlocal serial
        serial+=1;marker=f'FN_TARGET_RAY_{serial}'
        lines=request_exchange(a.session,command+'; echo '+marker,seconds)['received_prints']
        assert any(s.strip()==marker for s in lines),'Missing exact live echo; inspect before input'
        return lines
    def pose():
        ps=[s.strip() for s in send('getpos_exact') if s.startswith('setpos_exact ')];assert len(ps)==1;return ps[0]
    original=pose();report['original_pose']=original;save()
    try:
        for ray in config['rays']:
            eye,target=ray['eye'],ray['target'];assert len(eye)==len(target)==3 and all(math.isfinite(v) for v in eye+target)
            delta=[b-a for a,b in zip(eye,target)];length=math.sqrt(sum(v*v for v in delta));assert length>1
            pitch=-math.degrees(math.asin(delta[2]/length));yaw=math.degrees(math.atan2(delta[1],delta[0]));assert abs(pitch)<=89
            xyz=[v-64*w for v,w in zip(eye,up(pitch,yaw))]
            pair=[]
            for repeat in [1,2]:
                send(f'setpos_exact {xyz[0]:.6f} {xyz[1]:.6f} {xyz[2]:.6f}; setang_exact {pitch:.6f} {yaw:.6f} 0')
                observed=pose();values=numbers(observed)
                assert len(values)==6 and math.dist(values[:3],xyz)<=.01 and abs(values[3]-pitch)<=.01 and abs((values[4]-yaw+180)%360-180)<=.01 and abs(values[5])<=.01
                actual_eye=[v+64*w for v,w in zip(values[:3],up(values[3],values[4]))];assert math.dist(actual_eye,eye)<=.02
                lines=send('cast_ray; rangefinder');hits=[m for s in lines if (m:=re.search(r'Hit position: ('+NUMBER+r'), ('+NUMBER+r'), ('+NUMBER+r')',s))];distances=[s.strip() for s in lines if s.startswith('DISTANCE:')];surfaces=[s.strip() for s in lines if s.startswith('Hit:')]
                assert len(hits)==len(distances)==1 and surfaces,'Missing unique native first-hit/rangefinder result'
                point=[float(hits[0].group(i)) for i in [1,2,3]];distance=float(re.search(r'DISTANCE:\s+('+NUMBER+r') inches',distances[0]).group(1))
                o=dict(station_id=ray['id'],repeat=repeat,pose=observed,requested_eye=eye,eye_origin=actual_eye,target_point=target,requested_pitch=pitch,requested_yaw=yaw,hit=point,surface=surfaces,rangefinder_reply=distances[0],endpoint_difference_native=math.dist(point,target),distance_before_target_native=math.dist(actual_eye,target)-math.dist(actual_eye,point))
                report['observations'].append(o);pair.append(o);save()
                assert math.dist(actual_eye,point)>.1,'Own-origin collision; no endpoint accepted'
                assert abs(math.dist(actual_eye,point)-distance)<=.02,'Native rangefinder crosscheck failed'
            assert pair[0]['hit']==pair[1]['hit'] and pair[0]['surface']==pair[1]['surface'] and pair[0]['pose']==pair[1]['pose'],'Native repeat disagreement'
        report['status']='complete; directed first-hit diagnostics; rendered correspondence pending'
    except BaseException as error:
        report.update(status='failed; preserve partial observations and inspect before resume',error=str(error));raise
    finally:
        try:
            send(original);restored=pose();before,after=numbers(original),numbers(restored);errors=[abs(a-b) for a,b in zip(before,after)];assert len(errors)==6;errors[4]=abs((after[4]-before[4]+180)%360-180);assert max(errors)<=.01
            report.update(restored_pose=restored,restore_numeric_errors=errors)
        except BaseException as error:report['restore_error']=str(error)
        save()
    print(json.dumps(dict(id=report['id'],status=report['status'],observations=len(report['observations']),results=[dict(id=o['station_id'],difference_native=o['endpoint_difference_native'],before_target_native=o['distance_before_target_native']) for o in report['observations'] if o['repeat']==1])))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ['config','session','output']:p.add_argument('--'+key,type=Path,required=True)
    probe(p.parse_args())
