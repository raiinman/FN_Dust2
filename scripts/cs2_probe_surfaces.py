"""Repeat six collision rays from a recorded CS2 pose through an existing worker.

Usage: py -3.11 scripts/cs2_probe_surfaces.py --session QUEUE --output JSON
Output is source-unit collision evidence, not physical-scale calibration.
Requires an already loaded local survey session with cheats. Restores orientation.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from cs2_console import request_exchange

NUMBER = r'-?\d+(?:\.\d+)?'

def survey(session, output):
    if output.exists():
        raise FileExistsError('Preserve existing observations; choose a new file')
    def send(command, seconds=1):
        return request_exchange(session, command, seconds)['received_prints']
    pose_lines = send('getpos_exact')
    pose = next((line.strip() for line in pose_lines if line.startswith('setpos_exact ')), None)
    if pose is None:
        raise RuntimeError('No live pose; stop survey')
    xyz = [float(v) for v in re.findall(NUMBER, pose)[:3]]
    observations = []
    report = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(), source_build='25640462',
                  source_map='de_dust2', area='CT Spawn', origin_pose=pose,
                  unit='source_units', physical_scale='unresolved', observations=observations)
    def save():
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    save()
    for direction, pitch, yaw in [('plus_x',0,0),('minus_x',0,180),
                                 ('plus_y',0,90),('minus_y',0,-90),
                                 ('floor',90,0),('ceiling',-90,0)]:
        for repeat in range(2):
            command = f'setpos_exact {xyz[0]} {xyz[1]} {xyz[2]}; setang_exact {pitch} {yaw} 0'
            send(command, 1)
            # Pose output in the same command line can precede client updates.
            pose_reply = send('getpos_exact', 1)
            observed_pose = next((line.strip() for line in pose_reply if line.startswith('setpos_exact ')), None)
            if observed_pose is None:
                raise RuntimeError('No settled pose; stop survey')
            values = [float(v) for v in re.findall(NUMBER, observed_pose)]
            expected_pitch = max(-89, min(89, pitch))
            yaw_error = abs((values[4]-yaw+180)%360-180)
            if max(abs(values[i]-xyz[i]) for i in range(3)) > .01 or abs(values[3]-expected_pitch) > .01 or yaw_error > .01:
                report['status']='pose mismatch; stop'; save()
                raise RuntimeError('Settled pose differs from requested camera')
            lines = send('cast_ray', 1.5)
            hits = [re.search(r'Hit position: ('+NUMBER+r'), ('+NUMBER+r'), ('+NUMBER+r')', line) for line in lines]
            hits = [m for m in hits if m]
            if len(hits) != 1 or observed_pose is None:
                report['status']='incomplete; inspect console before retrying'; save()
                raise RuntimeError('No unique hit and pose; stop survey')
            observations.append(dict(direction=direction, repeat=repeat+1,
                                     requested_angles=[pitch,yaw,0],
                                     hit=[float(hits[0].group(i)) for i in (1,2,3)],
                                     observed_pose=observed_pose,
                                     hit_description=[s.strip() for s in lines if s.startswith('Hit:')]))
            save()
    send(pose+'; echo FN_DUST2_PROBE_RESTORED', 1.5)
    report['status']='complete; requires surface/axis review'
    save()
    print(json.dumps(report))

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--session',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    survey(a.session,a.output)
