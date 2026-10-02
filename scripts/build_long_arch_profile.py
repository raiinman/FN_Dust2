"""Project reviewed recessed-arch collision samples onto a calibrated native view.

Run: py -3.11 scripts/build_long_arch_profile.py
Reads ARCHITECTURAL_ENDPOINTS and LOCAL_CAMERA_CALIBRATIONS; checks source JPEG
hash and repeated corrected endpoints. Outputs LONG_ARCH_PROFILE.csv and
LONG_ARCH_ANNOTATED.svg. Samples/chords are not interpolated into a full surface.
"""
import base64
import csv
import hashlib
import json
from pathlib import Path
from build_local_camera import project


def build(root):
    ref=root/'reference'
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='LONG_OUTER_FRONT_001')
    capture=next(c for c in camera['captures'] if c['id']=='QA_LONG_OUTER_CAMERA_003_CLEAN')
    image=(root/capture['repository_image_path']).read_bytes()
    assert hashlib.sha256(image).hexdigest()==capture['jpeg_sha256']
    reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports'] if 'id' in r}
    calibration=json.loads((ref/'SCALE_CALIBRATION.json').read_text())
    assert calibration['status'].startswith('ACCEPTED')
    factor=calibration['cm_per_source_unit'];assert factor==2.54
    rows=[]
    for x in [565,580,600,620,640,660,680,700,715]:
        suffix='002' if x<=660 else '003'
        name=f'LONG_OUTER_ARCH_X{x}_Y280_{suffix}'
        report=reports[name]
        for feature,point in report['endpoints'].items():
            observations=[o for o in report['observations'] if o['feature']==feature]
            assert observations[-1]['hit']==observations[-2]['hit']==point and observations[-1]['xy_error']<=.02
            assert any('concrete' in d for d in observations[-1]['hit_description']) if feature=='ceiling' else True
            rows.append(dict(report_id=name,feature=feature,source_x=point[0],source_y=point[1],source_z=point[2],x_cm=round(point[0]*factor,4),y_cm=round(point[1]*factor,4),z_cm=round(point[2]*factor,4),scope='Repeated collision point; no surface interpolation or rendered-edge acceptance'))
    with (ref/'LONG_ARCH_PROFILE.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1040">','<rect width="1440" height="1040" fill="#101923"/>','<g fill="#edf3f8" font-family="Arial"><text x="40" y="40" font-size="25">Long Doors — recessed collision arch sections</text><text x="40" y="68" font-size="16">Build25640462 · 2.54 cm/native unit · calibrated front camera · Gate1 remains FAIL</text></g>',f'<image x="40" y="95" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(image).decode()}"/>']
    for row in rows:
        u,v=project(camera['projection_matrix'],[row[k] for k in ['source_x','source_y','source_z']]);color='#ffd84b' if row['feature']=='ceiling' else '#32daf1'
        svg.append(f'<circle cx="{u+40}" cy="{v+95}" r="4" fill="{color}" stroke="#111"/><text x="{u+47}" y="{v+92}" fill="{color}" stroke="#111" stroke-width="3" paint-order="stroke" font-family="Arial" font-size="12">{row["source_x"]:.0f}</text>')
    section=reports['LONG_OUTER_ARCH_WIDTH_SECTIONS_001']
    labels=[]
    for z,color in [(164,'#fc9651'),(194,'#57e69c'),(244,'#75bfff'),(264,'#e3a0ff')]:
        samples=[o for o in section['observations'] if o['station_id']==f'Y280_RAYZ{z}' and o['repeat']==2]
        assert len(samples)==2
        pixels=[project(camera['projection_matrix'],s['hit']) for s in samples]
        svg.append(f'<path d="M {pixels[0][0]+40},{pixels[0][1]+95} L {pixels[1][0]+40},{pixels[1][1]+95}" stroke="{color}" stroke-width="2"/>')
        width=abs(samples[0]['hit'][0]-samples[1]['hit'][0])*factor
        labels.append(f'Z{z}: {width:.2f}cm '+('leaf-to-concrete local chord' if z==164 else 'concrete intrados chord'))
    svg.append('<g fill="#edf3f8" font-family="Arial" font-size="16">')
    for i,label in enumerate(labels):svg.append(f'<text x="40" y="{850+i*24}">{label}</text>')
    svg.extend(['<text x="40" y="956">Gold: nine repeated intrados points. Cyan: six unobstructed floor points. Labels show native X.</text>','<text x="40" y="982">These are collision samples at Y280. Decorative stone/wood render edges and leaf clearance differ.</text>','<text x="40" y="1008">No floor below the right leaf is interpolated. Chords are sections; no full or minimum opening is certified.</text>','</g></svg>'])
    (ref/'LONG_ARCH_ANNOTATED.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
    print(len(rows),'repeated points; four annotated chords')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
