"""Repeat configured native horizontal architectural rays on one verified worker.

--config JSON --session QUEUE --output PRIVATE_JSON. Config owns id, build,
area, stations=[{id,pose:[x,y,z],yaws:[...]}]. Each ray is repeated twice.
Records native endpoints, surface descriptions and rangefinder crosschecks.
Does not infer walls, authorize dimensions or convert units. Stops on missing
echo/pose/hit and preserves completed observations. Restores the original pose.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from cs2_console import request_exchange

NUMBER = r'-?\d+(?:\.\d+)?'


def probe(a):
    if a.output.exists():
        raise FileExistsError('Preserve earlier evidence; choose a new output')
    config = json.loads(a.config.read_text(encoding='utf-8'))
    report = dict(id=config['id'], source_build=config['build'], area=config['area'],
        source_map='de_dust2', timestamp_utc=datetime.now(timezone.utc).isoformat(),
        unit='source_units', config=config, observations=[], status='in progress')
    serial = 0
    def save():
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    def send(command, seconds=.35):
        nonlocal serial
        serial += 1
        marker = 'FN_ENDPOINT_'+str(serial)
        lines = request_exchange(a.session, command+'; echo '+marker, seconds)['received_prints']
        if not any(s.strip() == marker for s in lines):
            raise RuntimeError('Missing exact live echo; inspect before reuse')
        return lines
    def pose():
        lines = send('getpos_exact')
        poses = [s.strip() for s in lines if s.startswith('setpos_exact ')]
        if len(poses) != 1:
            raise RuntimeError('No unique settled pose')
        return poses[0]
    original = pose()
    report['original_pose'] = original
    save()
    try:
        for station in config['stations']:
            x, y, z = station['pose']
            for yaw in station['yaws']:
                for repeat in (1, 2):
                    send(f'setpos_exact {x} {y} {z}; setang_exact 0 {yaw} 0')
                    observed = pose()
                    values = [float(v) for v in re.findall(NUMBER, observed)]
                    if max(abs(values[i]-station['pose'][i]) for i in range(3)) > .01 or abs(values[3]) > .01 or abs((values[4]-yaw+180)%360-180) > .01:
                        raise RuntimeError('Requested endpoint station differs from settled pose')
                    lines = send('cast_ray; rangefinder', .6)
                    hits = [m for s in lines if (m := re.search(r'Hit position: ('+NUMBER+r'), ('+NUMBER+r'), ('+NUMBER+r')', s))]
                    distances = [s.strip() for s in lines if s.startswith('DISTANCE:')]
                    if len(hits) != 1 or len(distances) != 1:
                        no_hit = len(hits) == len(distances) == 0 and any(
                            s.strip() == "Rangefinder didn't hit anything" for s in lines)
                        if config.get('allow_open_rays', False) and no_hit:
                            report.setdefault('open_observations', []).append(dict(
                                station_id=station['id'], yaw=yaw, repeat=repeat,
                                pose=observed, eye_origin=[x,y,z+64],
                                semantic_reply=["Rangefinder didn't hit anything"]))
                            save()
                            continue
                        report['failed_ray'] = dict(station_id=station['id'], yaw=yaw,
                            repeat=repeat, pose=observed, eye_origin=[x,y,z+64],
                            semantic_reply=[s.strip() for s in lines if s.startswith(
                                ('Hit:', 'Hit position:', 'DISTANCE:', "Rangefinder didn't hit anything"))])
                        save()
                        raise RuntimeError('No unique ray hit/rangefinder crosscheck')
                    report['observations'].append(dict(station_id=station['id'], yaw=yaw,
                        repeat=repeat, pose=observed, eye_origin=[x,y,z+64],
                        hit=[float(hits[0].group(i)) for i in (1,2,3)],
                        surface=[s.strip() for s in lines if s.startswith('Hit:')],
                        rangefinder_reply=distances[0]))
                    save()
                    hit=report['observations'][-1]['hit']
                    if sum((a-b)**2 for a,b in zip(hit,[x,y,z+64])) < .01:
                        raise RuntimeError('Ray starts inside collision; own-origin hit is not an endpoint')
                opened = [o for o in report.get('open_observations', [])
                    if o['station_id'] == station['id'] and o['yaw'] == yaw]
                if opened and len(opened) != 2:
                    raise RuntimeError('Open/hit repeat inconsistency; preserve both and inspect')
        report['status'] = 'complete; architectural interpretation pending'
    except Exception as error:
        report.update(status='failed; inspect before continuing', error=str(error))
        raise
    finally:
        try:
            send(original)
            restored = pose()
            report['restored_pose'] = restored
            before_values = [float(v) for v in re.findall(NUMBER, original)]
            after_values = [float(v) for v in re.findall(NUMBER, restored)]
            errors = [abs(a-b) for a,b in zip(before_values, after_values)]
            errors[4] = abs((after_values[4]-before_values[4]+180)%360-180)
            report['restore_numeric_errors'] = errors
            if len(errors) != 6 or max(errors) > .01:
                raise RuntimeError('Restored pose differs')
        except Exception as error:
            report['restore_error'] = str(error)
        save()
    print(json.dumps(dict(id=report['id'], status=report['status'], observations=len(report['observations']))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--session', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    probe(parser.parse_args())
