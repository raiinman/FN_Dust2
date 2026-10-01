"""Survey floor/ceiling hits at one XY using the tested camera-up offset.

Use only at an inspected interior with a safe Z; never equates units to cm.
Example: --area 'CT Spawn' --build 25640462 --xy 160.122742 2369.676270
         --z -40 --session QUEUE --output JSON
Iteratively corrects actual hit XY, repeats settled endpoints and restores pose.
"""
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re
from cs2_console import request_exchange

NUMBER = r'-?\d+(?:\.\d+)?'

def survey(a):
    if a.output.exists():
        raise FileExistsError(a.output)
    def send(command,seconds=1):
        return request_exchange(a.session,command,seconds)['received_prints']
    def pose():
        line=next((s.strip() for s in send('getpos_exact') if s.startswith('setpos_exact ')),None)
        if line is None:
            raise RuntimeError('Missing pose; stop')
        return line,[float(n) for n in re.findall(NUMBER,line)]
    initial, original=pose()
    report=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
        source_build=a.build,source_map='de_dust2',area=a.area,unit='source_units',
        target_xy=a.xy,probe_player_z=a.z,initial_pose=initial,
        model='getpos + 64 * camera_up, zero roll; TRACE_ORIGIN.md',
        xy_tolerance=.02,observations=[],accepted_for_production=False)
    def save():
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    save()
    endpoints={}
    for feature in a.features:
        pitch=89 if feature=='floor' else -89
        x=a.xy[0]-64*math.sin(math.radians(pitch))
        y=a.xy[1]
        for iteration in range(5):
            send(f'setpos_exact {x} {y} {a.z}; setang_exact {pitch} 0 0')
            observed,v=pose()
            if max(abs(v[i]-[x,y,a.z,pitch,0,0][i]) for i in range(6))>.01:
                raise RuntimeError('Pose mismatch; stop')
            lines=send('cast_ray',2)
            hits=[re.search(r'Hit position: ('+NUMBER+r'), ('+NUMBER+r'), ('+NUMBER+r')',s) for s in lines]
            hits=[h for h in hits if h]
            if len(hits)!=1:
                report.update(status='incomplete; inspect before another command',
                    failure=dict(feature=feature,iteration=iteration+1,
                        observed_pose=observed,received_prints=lines))
                save()
                raise RuntimeError('No unique collision hit; inspect before retrying')
            hit=[float(hits[0].group(i)) for i in (1,2,3)]
            error=math.hypot(hit[0]-a.xy[0],hit[1]-a.xy[1])
            item=dict(feature=feature,iteration=iteration+1,observed_pose=observed,
                hit=hit,xy_error=error,
                hit_description=[s.strip() for s in lines if s.startswith('Hit:')])
            report['observations'].append(item);save()
            if error<=.02:
                # The next iteration repeats exactly this settled pose.
                if feature in endpoints:
                    if hit!=endpoints[feature]:
                        raise RuntimeError('Repeated endpoint changed; stop')
                    break
                endpoints[feature]=hit
            else:
                x-=hit[0]-a.xy[0];y-=hit[1]-a.xy[1]
        else:
            raise RuntimeError('Column failed to converge/repeat; stop')
    separation=None
    vertical=None
    if 'floor' in endpoints and 'ceiling' in endpoints:
        separation=math.hypot(endpoints['floor'][0]-endpoints['ceiling'][0],
                              endpoints['floor'][1]-endpoints['ceiling'][1])
        if separation>.04 or endpoints['floor'][2]>=endpoints['ceiling'][2]:
            raise RuntimeError('Endpoints do not define a valid column')
        vertical=endpoints['ceiling'][2]-endpoints['floor'][2]
    send(initial)
    restored,values=pose()
    if max(abs(values[i]-original[i]) for i in range(6))>.01:
        raise RuntimeError('Restore mismatch')
    report.update(endpoints=endpoints,endpoint_xy_separation=separation,
        native_vertical_separation=vertical,
        restored_pose=restored,status='complete; collision column only; inspect surface semantics')
    save()
    print(json.dumps({k:report[k] for k in ['endpoints','endpoint_xy_separation','native_vertical_separation']}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--session',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--area',required=True)
    p.add_argument('--build',required=True)
    p.add_argument('--xy',type=float,nargs=2,required=True)
    p.add_argument('--z',type=float,required=True)
    p.add_argument('--features',nargs='+',choices=['floor','ceiling'],default=['floor','ceiling'])
    survey(p.parse_args())
