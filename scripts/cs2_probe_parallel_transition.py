"""Bracket first-hit material transitions with parallel native rays.

Config contains fixed height, normal axis, opposite safe normal origins and
on-masonry/off-timber tangent intervals. Preserve every repeat and component;
a material interface can be occlusion, never automatic structural opening,
minimum passage or a shared wall-body extent. One persistent worker/controller.
Optional normal_band_is_classifier explicitly distinguishes same-material
first faces by their measured normal coordinates; such an interface can still
be a leaf occlusion, not an exact fixed-post edge without independent review.
Optional tangent_axis=2 varies ray height while the camera remains horizontal;
each origin must declare fixed_lateral_native. The default tangent axis and
fixed-height behavior are unchanged. First-material height bounds likewise
require opposed-origin/component review; they are not hidden full-body tops.
"""
import argparse,json,math,re
from datetime import datetime,timezone
from pathlib import Path
from cs2_console import request_exchange

NUMBER=r'-?\d+(?:\.\d+)?'


def probe(a):
    assert not a.output.exists(), 'Preserve partial/completed reports before separately named resume'
    config=json.loads(a.config.read_text());axis=config['normal_axis'];assert axis in [0,1]
    tangent=config.get('tangent_axis',1-axis);assert tangent in [1-axis,2]
    if tangent!=2:height=config['height_native']
    assert 0<config['maximum_bracket_native']<=.1
    report=dict(id=config['id'],source_build=config['build'],source_map='de_dust2',timestamp_utc=datetime.now(timezone.utc).isoformat(),config=config,unit='source_units',observations=[],brackets=[],status='in progress',scope=__doc__)
    serial=0
    def save():a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n')
    def send(command,seconds=.35):
        nonlocal serial
        serial+=1;marker=f'FN_PARALLEL_TRANSITION_{serial}';lines=request_exchange(a.session,command+'; echo '+marker,seconds)['received_prints'];assert any(s.strip()==marker for s in lines),'Missing live echo; inspect queue before input';return lines
    def pose():
        lines=[s.strip() for s in send('getpos_exact') if s.startswith('setpos_exact ')];assert len(lines)==1;return lines[0]
    def values(text):return [float(v) for v in re.findall(NUMBER,text)]
    def sample(origin,coordinate):
        ray_height=coordinate if tangent==2 else height
        xyz=[0,0,ray_height-64];xyz[axis]=origin['normal_coordinate']
        xyz[1-axis]=origin['fixed_lateral_native'] if tangent==2 else coordinate
        yaw=origin['yaw']
        assert yaw in ([0,180] if axis==0 else [90,-90]);pair=[]
        for repeat in [1,2]:
            send(f'setpos_exact {xyz[0]} {xyz[1]} {xyz[2]}; setang_exact 0 {yaw} 0');p=pose();v=values(p)
            assert len(v)==6 and max(abs(v[i]-xyz[i]) for i in range(3))<=.01 and abs(v[3])<=.01 and abs(v[5])<=.01 and abs((v[4]-yaw+180)%360-180)<=.01
            lines=send('cast_ray; rangefinder',.6);hits=[m for s in lines if (m:=re.search(r'Hit position: ('+NUMBER+r'), ('+NUMBER+r'), ('+NUMBER+r')',s))];surfaces=[s.strip() for s in lines if s.startswith('Hit:')];distances=[s.strip() for s in lines if s.startswith('DISTANCE:')];assert len(hits)==len(distances)==1 and surfaces
            hit=[float(hits[0].group(i)) for i in [1,2,3]];eye=xyz[:2]+[ray_height];distance=re.search(r'DISTANCE:\s+('+NUMBER+') inches',distances[0]);assert distance
            observation=dict(origin_id=origin['id'],requested_tangent=coordinate,repeat=repeat,pose=p,eye_origin=eye,hit=hit,surface=surfaces,rangefinder_reply=distances[0]);report['observations'].append(observation);pair.append(observation);save()
            assert math.dist(eye,hit)>.1, 'Own-origin collision; no endpoint accepted'
            assert abs(float(distance.group(1))-math.dist(eye,hit))<=.02 and abs(hit[1-axis]-eye[1-axis])<=.02 and abs(hit[2]-ray_height)<=.02
        assert pair[0]['hit']==pair[1]['hit'] and pair[0]['surface']==pair[1]['surface']
        description=str(pair[-1]['surface']);on='surfaceprop '+config['on_material']+',' in description and 'shape type: '+config['on_shape']+',' in description
        if config.get('normal_band_is_classifier'):
            on=on and origin['on_normal_band'][0]<=pair[-1]['hit'][axis]<=origin['on_normal_band'][1]
        if on:assert origin['on_normal_band'][0]<=pair[-1]['hit'][axis]<=origin['on_normal_band'][1], 'Unexpected masonry depth; inspect component'
        else:
            assert 'surfaceprop '+config['off_material']+',' in description, 'Unexpected off-component; no interface classification'
            if config.get('off_shape'):
                assert 'shape type: '+config['off_shape']+',' in description, 'Unexpected off-component shape'
        return dict(coordinate=coordinate,on_component=on,observation_index=len(report['observations'])-1)
    original=pose();report['original_pose']=original;save()
    try:
        for origin in config['origins']:
            for case in config['brackets']:
                on,off=[sample(origin,case[key]) for key in ['on_coordinate','off_coordinate']];assert on['on_component'] and not off['on_component']
                history=[on,off]
                for iteration in range(24):
                    if abs(on['coordinate']-off['coordinate'])<=config['maximum_bracket_native']:break
                    point=sample(origin,(on['coordinate']+off['coordinate'])/2);history.append(point)
                    if point['on_component']:on=point
                    else:off=point
                else:raise RuntimeError('Material transition failed to converge')
                report['brackets'].append(dict(id=case['id'],origin_id=origin['id'],on=on,off=off,tangent_interval_native=sorted([on['coordinate'],off['coordinate']]),history=history,limits='Parallel first-hit material interval only; component occlusion and actual structural end require independent geometric/render review.'));save()
        report['status']='complete; material interfaces only; structural review pending'
    except BaseException as error:report.update(status='failed; preserve partial observations and inspect before resume',error=str(error));raise
    finally:
        try:
            send(original);restored=pose();before,after=values(original),values(restored);errors=[abs(x-y) for x,y in zip(before,after)];assert len(errors)==6;errors[4]=abs((after[4]-before[4]+180)%360-180);assert max(errors)<=.01;report.update(restored_pose=restored,restore_numeric_errors=errors)
        except BaseException as error:report['restore_error']=str(error)
        save()
    print(json.dumps(dict(id=report['id'],status=report['status'],brackets=[{k:b[k] for k in ['id','origin_id','tangent_interval_native']} for b in report['brackets']])))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['config','session','output']:p.add_argument('--'+name,type=Path,required=True)
    probe(p.parse_args())
