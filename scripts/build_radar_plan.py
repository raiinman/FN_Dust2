"""Rebuild calibrated HUD context plan; never infer architectural boundaries.

Run py -3.11 scripts/build_radar_plan.py. Reads RADAR_CALIBRATION.json and
hash-pinned native radar crops; places repeated floor samples in source axes.
"""
import base64,csv,hashlib,json,math
from pathlib import Path
root=Path(__file__).resolve().parent.parent
ref=root/'reference'
report=json.loads((ref/'RADAR_CALIBRATION.json').read_text())
for anchor in report['anchors']:
    assert hashlib.sha256((root/anchor['repository_crop']).read_bytes()).hexdigest()==anchor['crop_png_sha256']
t=report['pixel_transform']
sx,tx,sy,ty=[t[n] for n in ('x_scale','x_offset','y_scale','y_offset')]
assert max(a['residual_pixels'] for a in report['anchors'])<1
for anchor in report['anchors']:
    predicted=[sx*anchor['source_pose'][0]+tx,sy*anchor['source_pose'][1]+ty]
    assert math.dist(predicted,anchor['pixel'])<1
assert sx>0 and sy<0 and abs(abs(sx/sy)-1)<.01
base=root/next(a['repository_crop'] for a in report['anchors'] if a['id']=='QA_RADAR_TSPAWN_CAL_001')
image = base64.b64encode(base.read_bytes()).decode()
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1060" viewBox="0 0 1100 1060">', '<rect width="1100" height="1060" fill="#101923"/>', '<g fill="#edf3f8" font-family="Arial"><text x="40" y="40" font-size="25">Dust II — current-build calibrated HUD plan</text><text x="40" y="68" font-size="16">CS2 build 25640462 · source axes · 2.54 cm per native unit · Gate 1 remains FAIL</text></g>',f'<image x="40" y="95" width="900" height="900" href="data:image/png;base64,{image}"/>']
def pixel(x,y):
    return 40+3.6*(sx*x+tx),95+3.6*(sy*y+ty)
walks=json.loads((ref/'WALK_PROBES.json').read_text())
attempts={a['report']['id']:a['report'] for a in walks['attempts']}
import re
for route in walks['accepted_paths']:
    r=attempts[route['forward_report']]
    assert r['status']=='completed collision walk' and r['teleports_during_route']==0
    coordinates=[r['settled_start_pose']]+[o['after_pose'] for o in r['observations']]
    points=[]
    for pose in coordinates:
        values=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',pose)]
        px,py=pixel(*values[:2]);points.append(f'{px:.2f},{py:.2f}')
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="#f7a643" stroke-width="3" opacity=".85"><title>{route["id"]}: reviewed collision walk, both directions; player path, not wall boundary</title></polyline>')
for x in range(-2000,2001,500):
    px,_ = pixel(x,0)
    parts.append(f'<path d="M {px} 95 V 995" stroke="#a0bbd0" opacity=".25"/><text x="{px}" y="1017" text-anchor="middle" fill="#edf3f8" font-family="Arial" font-size="13">{x*2.54/100:.1f} m</text>')
for y in range(-1000,3001,500):
    _,py = pixel(0,y)
    parts.append(f'<path d="M 40 {py} H 940" stroke="#a0bbd0" opacity=".25"/><text x="950" y="{py+4}" fill="#edf3f8" font-family="Arial" font-size="13">Y {y*2.54/100:.1f} m</text>')
floors = list(csv.DictReader((ref/'FLOOR_DATUMS.csv').open()))
for i,row in enumerate(floors,1):
    x,y,z = [float(row[n]) for n in ('source_x','source_y','source_z')]
    px,py = pixel(x,y)
    parts.append(f'<circle cx="{px}" cy="{py}" r="8" fill="#24c8ed" stroke="#071018" stroke-width="2"/><text x="{px+11}" y="{py-9}" fill="#fff" font-family="Arial" font-size="13" stroke="#071018" stroke-width="3" paint-order="stroke">{i}: {z*2.54/100:+.2f} m</text>')
parts[0] = parts[0].replace('1060','1260')
parts[1] = parts[1].replace('1060','1260')
parts.append('<g font-family="Arial" fill="#edf3f8" font-size="14"><text x="40" y="1042">Grid: 12.7 m. Cyan labels: repeated collision-floor heights; source axes, not Unreal coordinates.</text>')
for i,row in enumerate(floors):
    x = 40 if i < 7 else 580
    y = 1080 + (i if i < 7 else i-7)*18
    parts.append(f'<text x="{x}" y="{y}">{i+1}: {row["area"]}</text>')
parts.append(f'<text x="40" y="1228">Orange: {len(walks["accepted_paths"])} reviewed paths, both directions. Player trajectories do not define wall boundaries.</text>')
parts.append('<text x="40" y="1248">Marker calibration fits within 0.20 pixels; allow 2 pixels (~92 cm). Radar outlines remain unsurveyed.</text></g></svg>')
(ref/'RADAR_PLAN.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
