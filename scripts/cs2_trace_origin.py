"""Diagnose cast_ray origin at the current pose; never converts units to cm.

Usage: py -3.11 scripts/cs2_trace_origin.py --session QUEUE --output JSON
Requires an existing persistent survey worker. Restores the initial pose.
Tests zero roll only. Hypothesis: origin = getpos + 64 * camera_up.
"""
import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
import re
from cs2_console import request_exchange

NUMBER = r'-?\d+(?:\.\d+)?'

def main(session, output):
    if output.exists():
        raise FileExistsError(output)
    def send(command):
        return request_exchange(session, command, 1.5)['received_prints']
    def pose():
        line = next((x.strip() for x in send('getpos_exact') if x.startswith('setpos_exact ')), None)
        if line is None:
            raise RuntimeError('No live pose; stop')
        return line, [float(x) for x in re.findall(NUMBER, line)]
    initial, values = pose()
    xyz = values[:3]
    report = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
                  source_map='de_dust2', source_build='25640462',
                  unit='source_units', initial_pose=initial,
                  hypothesis='trace_origin = getpos_xyz + 64 * camera_up; zero roll',
                  observations=[], accepted_for_production=False)
    def save():
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    save()
    for pitch, yaw in [(45,0),(-45,0),(45,90),(-45,90)]:
        for repeat in [1,2]:
            send(f'setpos_exact {xyz[0]} {xyz[1]} {xyz[2]}; setang_exact {pitch} {yaw} 0')
            observed, settled = pose()
            if max(abs(settled[i]-xyz[i]) for i in range(3)) > .01 or abs(settled[3]-pitch) > .01 or abs((settled[4]-yaw+180)%360-180) > .01:
                raise RuntimeError('Pose mismatch; inspect before retrying')
            lines = send('cast_ray')
            hits = [re.search(r'Hit position: ('+NUMBER+r'), ('+NUMBER+r'), ('+NUMBER+r')', x) for x in lines]
            hits = [h for h in hits if h]
            if len(hits) != 1:
                raise RuntimeError('No unique hit; stop')
            hit = [float(hits[0].group(i)) for i in (1,2,3)]
            p,y = math.radians(pitch), math.radians(yaw)
            forward = [math.cos(p)*math.cos(y), math.cos(p)*math.sin(y), -math.sin(p)]
            up = [math.sin(p)*math.cos(y), math.sin(p)*math.sin(y), math.cos(p)]
            delta = [hit[i]-xyz[i] for i in range(3)]
            offset = sum(delta[i]*up[i] for i in range(3))
            origin = [xyz[i]+64*up[i] for i in range(3)]
            distance = sum((hit[i]-origin[i])*forward[i] for i in range(3))
            residual = math.sqrt(sum((hit[i]-origin[i]-distance*forward[i])**2 for i in range(3)))
            report['observations'].append(dict(pitch=pitch,yaw=yaw,repeat=repeat,
                observed_pose=observed,hit=hit,implied_up_offset=offset,
                hypothesis_perpendicular_residual=residual,
                hit_description=[x.strip() for x in lines if x.startswith('Hit:')]))
            save()
    send(initial)
    restored, restored_values = pose()
    if max(abs(restored_values[i]-values[i]) for i in range(6)) > .01:
        raise RuntimeError('Restore pose mismatch')
    report['restored_pose']=restored
    report['status']='complete; empirical zero-roll model only; physical scale unresolved'
    save()
    print(json.dumps(dict(observations=len(report['observations']),
        max_residual=max(x['hypothesis_perpendicular_residual'] for x in report['observations']))))

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--session',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    main(a.session,a.output)
