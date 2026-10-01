"""Record a collision-enabled controlled walk through an existing CS2 worker.

--config JSON --session QUEUE --output JSON. Config: id, build, start=[x,y,z],
waypoints=[[x,y],...], maxspeed=80, arrival_radius=25. Start is the only teleport.
Changes local sv_maxspeed for slow steering, restores it, releases input always.
This tests connectivity, not default-speed travel time or jump performance.
"""
import argparse
from datetime import datetime,timezone
import json
import math
from pathlib import Path
import re
from cs2_console import request_exchange

NUMBER=r'-?\d+(?:\.\d+)?'

def walk(a):
    if a.output.exists():raise FileExistsError(a.output)
    config=json.loads(a.config.read_text(encoding='utf-8'))
    report=dict(id=config['id'],source_build=config['build'],source_map='de_dust2',
        timestamp_utc=datetime.now(timezone.utc).isoformat(),unit='source_units',
        config=config,teleports_during_route=0,observations=[],status='in progress')
    def save():
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    serial=0
    def send(command,seconds=.3):
        nonlocal serial
        serial+=1;marker=f'FN_WALK_{serial}'
        lines=request_exchange(a.session,command+'; echo '+marker,seconds)['received_prints']
        if not any(line.strip()==marker for line in lines):
            raise RuntimeError('Missing live command marker; stop')
        return lines
    def pose():
        lines=send('getpos_exact',.3)
        line=next((s.strip() for s in lines if s.startswith('setpos_exact ')),None)
        if line is None:raise RuntimeError('Missing pose; stop')
        return [float(x) for x in re.findall(NUMBER,line)],line
    lines=send('sv_maxspeed',.5)
    original_speed=next((float(m.group(1)) for s in lines if (m:=re.search(r'sv_maxspeed = ('+NUMBER+r')',s))),None)
    if original_speed is None:raise RuntimeError('No original speed; stop')
    save()
    try:
        send('-forward; -back; -left; -right; -jump; noclip 1',.5)
        x,y,z=config['start']
        send(f'setpos_exact {x} {y} {z}; setang_exact 0 0 0',.7)
        lines=send(f'sv_maxspeed {config.get("maxspeed",80)}; noclip 0',1)
        if not any('noclip OFF' in s for s in lines):raise RuntimeError('Collision mode not verified')
        report['collision_mode_reply']='noclip OFF'
        current,line=pose();report['settled_start_pose']=line;save()
        for index,target in enumerate(config['waypoints']):
            stagnant=0
            for step in range(80):
                current,line=pose()
                distance=math.hypot(target[0]-current[0],target[1]-current[1])
                if distance<=config.get('arrival_radius',25):break
                yaw=math.degrees(math.atan2(target[1]-current[1],target[0]-current[0]))
                send(f'setang_exact 0 {yaw} 0',.15)
                seconds=max(.05,min(.4,(distance-10)/config.get('maxspeed',80)-.2))
                send('+forward',seconds)
                send('-forward',.15)
                after,after_line=pose()
                progress=distance-math.hypot(target[0]-after[0],target[1]-after[1])
                report['observations'].append(dict(waypoint=index+1,step=step+1,
                    before_pose=line,after_pose=after_line,requested_yaw=yaw,
                    requested_hold_seconds=seconds,progress_toward_target=progress))
                save()
                stagnant=stagnant+1 if progress<1 else 0
                if stagnant>=3:
                    report['status']='blocked; path requires inspection';save();return
            else:
                report['status']='iteration limit; not validated';save();return
        final,line=pose();report.update(final_pose=line,status='completed collision walk',
            limitations='reduced speed; waypoint arrival tolerance; not special traversal or metric calibration')
        save()
    except Exception as error:
        report['status']='failed; inspect console';report['error']=str(error);save();raise
    finally:
        # Release first, even if another command or pose read failed.
        try:
            send('-forward; -back; -left; -right; -jump',.3)
            send(f'sv_maxspeed {original_speed}; noclip 1',.5)
            report['restored_speed']=original_speed
            save()
        except Exception as error:
            report['cleanup_error']=str(error);save()
    print(json.dumps(dict(id=report['id'],status=report['status'],steps=len(report['observations']))))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,required=True)
    p.add_argument('--session',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    walk(p.parse_args())
