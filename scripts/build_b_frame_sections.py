"""Rebuild bounded B-door first-material sections, not a full opening model.

Inputs: B_FRAME_SECTIONS.json, repeated ARCHITECTURAL_ENDPOINTS reports and
independently checked local camera. Outputs: B_FRAME_SECTION_MEASUREMENTS.json,
CSV and native-image SVG. Run this script and render/inspect its SVG. Material
interfaces bound collision sections; no leaf clearance, hidden body, continuous
height interpolation or exact rendered/collision correspondence is implied.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path
from build_local_camera import project


def repeated(report, index):
    a,b=report['observations'][index-1:index+1]
    assert a['repeat']==1 and b['repeat']==2
    assert a['hit']==b['hit'] and a['surface']==b['surface'] and a['pose']==b['pose']
    v=[float(s) for s in re.findall(r'-?\d+(?:\.\d+)?',b['pose'])]
    eye=v[:2]+[v[2]+64]
    assert math.dist(eye,b['eye_origin'])<=.01 and abs(v[3])<=.01 and abs(v[5])<=.01
    distance=float(re.search(r'DISTANCE:\s+(-?\d+(?:\.\d+)?) inches',b['rangefinder_reply']).group(1))
    assert math.dist(eye,b['hit'])>.1 and abs(distance-math.dist(eye,b['hit']))<=.02
    assert abs(b['hit'][1]-eye[1])<=.02 and abs(b['hit'][2]-eye[2])<=.02
    assert abs((v[4]+180)%180)<=.01
    return b


def rows(ref):
    config=json.loads((ref/'B_FRAME_SECTIONS.json').read_text())
    reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']}
    transition=reports[config['transition_report']];check=reports[config['height_report']]
    for report in [transition,check]:
        assert report['source_build']==config['source_build'] and report['status'].startswith('complete;')
        assert max(report['restore_numeric_errors'])<=.01 and not report.get('restore_error')
    sections=[]
    for height in [40,80,140]:
        ends=[]
        for end in ['south','north']:
            intervals=[];faces={}
            for origin in ['B_INSIDE','CT_OUTSIDE']:
                if height==80:
                    bracket=next(b for b in transition['brackets'] if b['id']==end+'_masonry_to_timber' and b['origin_id']==origin)
                    on,off=[repeated(transition,bracket[role]['observation_index']) for role in ['on','off']]
                    interval=bracket['tangent_interval_native']
                    assert interval[1]-interval[0]<=.02
                else:
                    case=next(c for c in config['height_cases'] if c['height_native']==height and c['end_id']==end.upper() and c['origin_id']==origin)
                    selected=[]
                    for role in ['on','off']:
                        index=next(i for i,o in enumerate(check['observations']) if o['station_id']==case[role+'_station'] and o['repeat']==1)
                        selected.append(repeated(check,index+1))
                    on,off=selected;interval=sorted([on['eye_origin'][1],off['eye_origin'][1]])
                    assert max(abs(x-y) for x,y in zip(interval,case['requested_interval']))<=.00001
                assert 'surfaceprop concrete,' in str(on['surface']) and 'shape type: Mesh,' in str(on['surface'])
                assert 'surfaceprop Wood_Dense,' in str(off['surface']) and 'shape type: Hull,' in str(off['surface'])
                assert on['eye_origin'][2]==off['eye_origin'][2]==height
                assert (on['hit'][1]<off['hit'][1])==(end=='south')
                intervals.append(interval);faces[origin]={'masonry':on['hit'],'timber':off['hit']}
            assert max(i[0] for i in intervals)<=min(i[1] for i in intervals)
            # Retain the union, then expand by printed endpoint/pose rounding.
            interval=[min(i[0] for i in intervals)-.005,max(i[1] for i in intervals)+.005]
            ends.append(dict(end=end,tangent_interval_native=interval,opposing_intervals=intervals,faces=faces))
        width=[(ends[1]['tangent_interval_native'][0]-ends[0]['tangent_interval_native'][1])*2.54,
               (ends[1]['tangent_interval_native'][1]-ends[0]['tangent_interval_native'][0])*2.54]
        depths=[]
        for end in ends:
            for material in ['masonry','timber']:
                inside,outside=[end['faces'][o][material] for o in ['B_INSIDE','CT_OUTSIDE']]
                assert abs(inside[1]-outside[1])<=.01 and inside[0]<outside[0]
                value=(outside[0]-inside[0])*2.54
                depths.append(dict(end=end['end'],material=material,value_cm=value,interval_cm=[value-.0254,value+.0254],inside=inside,outside=outside))
        sections.append(dict(height_native=height,ends=ends,width_interval_cm=width,depths=depths))
    return config,sections


def measurement_rows(ref):
    config,sections=rows(ref);result=[]
    def add(id,feature,interval):
        result.append(dict(id=id,area='B Doors',feature=feature,value=round(sum(interval)/2,4),unit='cm',
            method='opposing repeated native first-material rays; independently repeated height checks; SCALE_CALIBRATION',
            source_id='B_FRAME_SECTIONS/'+config['transition_report']+';'+config['height_report'],
            confidence='bounded local collision-material section',tolerance=f'[{interval[0]:.4f},{interval[1]:.4f}]cm native numerical/transition bounds',
            notes=config['limits']))
    for section in sections:
        h=section['height_native']
        add(f'B_FRAME_Z{h}_MATERIAL_WIDTH',f'Masonry-to-timber lateral material-region span at native Z{h}',section['width_interval_cm'])
        for depth in section['depths']:
            add(f'B_FRAME_Z{h}_{depth["end"].upper()}_{depth["material"].upper()}_DEPTH',f'{depth["end"]} {depth["material"]} opposite first-face normal span at native Z{h}',depth['interval_cm'])
    return result


def build(root):
    ref=root/'reference';config,sections=rows(ref)
    cameras={c['id']:c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras']}
    camera=cameras[config['camera_id']]
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    image=root/config['clean_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==config['clean_jpeg_sha256']
    annotation=[]
    for section in sections:
        for end in section['ends']:
            for material,point in end['faces']['CT_OUTSIDE'].items():
                annotation.append(dict(height_native=section['height_native'],end=end['end'],material=material,point=point,pixel=project(camera['projection_matrix'],point)))
    (ref/'B_FRAME_SECTION_MEASUREMENTS.json').write_text(json.dumps(dict(source_build=config['source_build'],sections=sections,projected_native_points=annotation,limits=config['limits'],render_review=config['render_review'],gate1='FAIL'),indent=2)+'\n')
    measurements=measurement_rows(ref)
    with (ref/'B_FRAME_SECTION_MEASUREMENTS.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=measurements[0].keys());w.writeheader();w.writerows(measurements)
    data=base64.b64encode(image.read_bytes()).decode()
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1010">','<rect width="1280" height="1010" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">B doorway / opposing first-material sections at three measured heights</text>','<text x="25" y="65" font-size="17">Cyan: masonry / orange: timber. Calibrated native projection; source/render offsets remain separate.</text>']
    for item in annotation:
        u,v=item['pixel'];color='#39e5cd' if item['material']=='masonry' else '#ffb45e'
        svg.append(f'<circle cx="{u:.3f}" cy="{v+100:.3f}" r="4" fill="none" stroke="{color}" stroke-width="1.5"/>')
    for i,section in enumerate(sections):
        interval=section['width_interval_cm']
        svg.append(f'<text x="25" y="{850+i*27}" font-size="17">Native Z{section["height_native"]}: material-region lateral span [{interval[0]:.4f}, {interval[1]:.4f}] cm</text>')
    svg.extend(['<text x="25" y="950" font-size="16">Three sampled sections only; no continuous frame body, leaf gap, minimum clearance or full aperture acceptance.</text>','<text x="25" y="980" font-size="16">South visible edge has a separate unresolved few-pixel offset. Gate1 FAIL; production geometry has not started.</text></g></svg>'])
    (ref/'B_FRAME_SECTIONS.svg').write_text('\n'.join(svg)+'\n')
    print(f'{len(measurements)} bounded local material/face-span measurements; Gate1 FAIL')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
