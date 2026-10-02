"""Record a configured collision jump/drop attempt through the existing worker.

Inputs: --config JSON --session PRIVATE_QUEUE --output NEW_JSON. Config includes
id/build/start[x,y,z,pitch,yaw], expected_start{xy_radius,z_min,z_max}, actions
[{command,seconds,label,stop_before_pose?}]. Commands are limited to movement input; each action
is followed by timestamped pose telemetry. Start is the only teleport. Settled
start must match its configured region before any traversal input. A completed
attempt requires independent review; it never grants topology acceptance.
"""
import argparse,json,math,re
from datetime import datetime,timezone
from pathlib import Path
from cs2_console import request_exchange

ALLOWED={'+forward','-forward','+back','-back','+left','-left','+right','-right','+jump','-jump','+duck','-duck'}
NUMBER=r'-?\d+(?:\.\d+)?'
def run(a):
    if a.output.exists():raise FileExistsError(a.output)
    config=json.loads(a.config.read_text());start=config['start'];bounds=config['expected_start']
    partner=config.get('partner_setup_evidence')
    allowed=ALLOWED|({'bot_crouch 0','bot_crouch 1'} if partner else set())
    if partner:
        assert partner.get('type')=='stationary local practice bot' and partner.get('capture_id')
    assert len(start)==5 and 0<bounds['xy_radius']<=25 and bounds['z_min']<=bounds['z_max']
    for action in config['actions']:
        assert all(c.strip() in allowed for c in action['command'].split(';'))
        if action.get('stop_before_pose'):
            assert all(c.strip() in ALLOWED and c.strip().startswith('-') for c in action['stop_before_pose'].split(';'))
        assert .05<=action['seconds']<=2
    now=lambda:datetime.now(timezone.utc).isoformat()
    r=dict(id=config['id'],source_build=config['build'],source_map='de_dust2',unit='source_units',config=config,timestamp_utc=now(),teleports_during_route=0,commands=[],observations=[],status='in progress')
    def save():
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(r,indent=2)+'\n')
    def send(cmd,seconds=.15):
        marker=f"FN_TRAV_{len(r['commands'])+1}";sent=now()
        lines=request_exchange(a.session,cmd+'; echo '+marker,seconds)['received_prints']
        r['commands'].append(dict(command=cmd,requested_hold_seconds=seconds,sent_utc=sent,returned_utc=now(),received_prints=lines));save()
        if not any(s.strip()==marker for s in lines):raise RuntimeError('Missing live marker; inspect queue')
        return lines
    def pose(label):
        lines=send('getpos_exact');line=next((s.strip() for s in lines if s.startswith('setpos_exact ')),None)
        if not line:raise RuntimeError('Missing pose')
        values=[float(v) for v in re.findall(NUMBER,line)]
        r['observations'].append(dict(label=label,timestamp_utc=now(),pose=line));save();return values
    try:
        send('-forward; -back; -left; -right; -jump; -duck; noclip 1',.3)
        send('sv_gravity; sv_jump_impulse; sv_maxspeed',.3)
        if partner:
            lines=send('bot_stop; bot_dont_shoot; bot_crouch',.3)
            for expected in ['bot_stop = 1','bot_dont_shoot = true','bot_crouch = true']:
                assert any(s.strip()==expected for s in lines),'Partner setup not verified: '+expected
            r['partner_preflight']='stationary/non-shooting/crouched cvars verified; capture requires visual review'
        send(f'setpos_exact {start[0]} {start[1]} {start[2]}; setang_exact {start[3]} {start[4]} 0',.3)
        lines=send('noclip 0',.7)
        if not any('noclip OFF' in s for s in lines):raise RuntimeError('Collision not verified')
        p=pose('settled start')
        if math.dist(p[:2],start[:2])>bounds['xy_radius'] or not bounds['z_min']<=p[2]<=bounds['z_max']:
            raise RuntimeError('Settled start outside reviewed region; no traversal input sent')
        r['collision_mode_reply']='noclip OFF'
        for action in config['actions']:
            send(action['command'],action['seconds'])
            # Optional release prevents telemetry latency extending a short input.
            # Preserve the release and actual timestamps as part of the evidence.
            if action.get('stop_before_pose'):
                send(action['stop_before_pose'],.05)
            pose(action['label'])
        send('-forward; -back; -left; -right; -jump; -duck',.3)
        pose('landing check 1');send('-forward',1);pose('landing check 2')
        r['status']='completed attempt; landing and traversal require review';save()
    except Exception as e:
        r.update(status='failed; inspect attempt and queue',error=str(e));save();raise
    finally:
        try:
            lines=send('-forward; -back; -left; -right; -jump; -duck; noclip 1',.3)
            if not any('noclip ON' in s for s in lines):raise RuntimeError('Noclip cleanup not verified')
            r['cleanup']='movement released; noclip ON verified';save()
            if partner:
                send('bot_crouch 1',.3)
                r['partner_cleanup']='crouch restored for local repeated test; bot removal/global originals remain caller responsibility';save()
        except Exception as e:r['cleanup_error']=str(e);save()
    print(json.dumps(dict(id=r['id'],status=r['status'])))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config',type=Path,required=True);p.add_argument('--session',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    run(p.parse_args())
