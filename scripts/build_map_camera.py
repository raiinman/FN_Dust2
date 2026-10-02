"""Rebuild empirical native overhead calibration and annotated context.

Run py -3.11 scripts/build_map_camera.py. Uses standard-library least squares,
hash-pinned reviewed JPEGs and measured floor/path inputs. This is camera and
point evidence, never a surveyed continuous architectural footprint.
"""
import base64,csv,hashlib,json,math,re
from html import escape
from pathlib import Path
root=Path(__file__).resolve().parent.parent;ref=root/'reference'
r=json.loads((ref/'MAP_CAMERA_CALIBRATION.json').read_text())
for c in r['captures']:
    assert hashlib.sha256((root/c['repository_image_path']).read_bytes()).hexdigest()==c['jpeg_sha256']
groups=r['groups'];fit=next(g for g in groups if g['role']=='fit')['anchors']
assert len(fit)>=6
A=[];b=[]
for a in fit:
    X=[v/1000 for v in a['world']]+[1];u,v=a['pixel']
    A.extend([X+[0]*4+[-u*t for t in X[:3]], [0]*4+X+[-v*t for t in X[:3]]]);b.extend([u,v])
M=[[sum(row[i]*row[j] for row in A) for j in range(11)]+[sum(row[i]*y for row,y in zip(A,b))] for i in range(11)]
for i in range(11):
    pivot=max(range(i,11),key=lambda k:abs(M[k][i]));M[i],M[pivot]=M[pivot],M[i]
    assert abs(M[i][i])>1e-10,'Degenerate calibration anchors'
    d=M[i][i];M[i]=[v/d for v in M[i]]
    for j in range(11):
        if j!=i:
            d=M[j][i];M[j]=[v-d*w for v,w in zip(M[j],M[i])]
q=[row[-1] for row in M]+[1];P=[q[i:i+4] for i in [0,4,8]]
for row in P:
    for j in range(3):row[j]/=1000
def project(point):
    a=[sum(t*x for t,x in zip(row,point+[1])) for row in P]
    assert a[2]>0
    return [a[0]/a[2],a[1]/a[2]]
def inverse(u,v,z):
    a,b=P[0][0]-u*P[2][0],P[0][1]-u*P[2][1]
    c,d=P[1][0]-v*P[2][0],P[1][1]-v*P[2][1]
    e=(u*P[2][2]-P[0][2])*z+u*P[2][3]-P[0][3]
    f=(v*P[2][2]-P[1][2])*z+v*P[2][3]-P[1][3]
    det=a*d-b*c;assert abs(det)>1e-12
    return [(e*d-b*f)/det,(a*f-e*c)/det,z]
for g in groups:
    for a in g['anchors']:
        a['projected_pixel']=project(a['world']);a['residual_px']=math.dist(a['pixel'],a['projected_pixel'])
        assert math.dist(inverse(*a['projected_pixel'],a['world'][2]),a['world'])<1e-7
    g['maximum_residual_px']=max(a['residual_px'] for a in g['anchors']);assert g['maximum_residual_px']<1
r['projection_matrix']=P;r['fit_algorithm']='Normalized-world linear least squares, P[2][3]=1; sixteen holdouts excluded from fitting.'
bounds=[]
for z in [-100,0,100,300,600,1000]:
    delta=[]
    for a in groups[2]['anchors']:
        u,v=project([*a['world'][:2],z]);p=inverse(u,v,z)
        for du,dv in [(1.5,0),(-1.5,0),(0,1.5),(0,-1.5)]:delta.append(math.dist(p,inverse(u+du,v+dv,z))*2.54)
    bounds.append(dict(source_z=z,maximum_axis_1_5_pixel_displacement_cm=max(delta)))
r['sampled_pixel_localization_bounds']=bounds
(ref/'MAP_CAMERA_CALIBRATION.json').write_text(json.dumps(r,indent=2)+'\n')
clean=next(c for c in r['captures'] if c['id']=='QA_MAP_CAMERA_002_CLEAN')
im=base64.b64encode((root/clean['repository_image_path']).read_bytes()).decode()
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1150" viewBox="0 0 1440 1150">','<rect width="1440" height="1150" fill="#101923"/>','<g fill="#edf3f8" font-family="Arial"><text x="40" y="40" font-size="25">Dust II — calibrated native overhead context and elevation points</text><text x="40" y="68" font-size="16">Build 25640462 · 2.54 cm/native unit · camera projection validated · Gate 1 remains FAIL</text></g>',f'<image x="40" y="95" width="1280" height="720" href="data:image/jpeg;base64,{im}"/>']
def xy(p):
    u,v=project(p);return u+40,v+95
for x in range(-2000,2001,500):
    a=xy([x,-1000,0]);b=xy([x,3000,0]);parts.append(f'<path d="M {a[0]} {a[1]} L {b[0]} {b[1]}" stroke="#83bad0" opacity=".30"/><text x="{a[0]}" y="{a[1]+17}" fill="#fff" font-size="12">{x*2.54/100:.1f}m</text>')
for y in range(-1000,3001,500):
    a=xy([-2000,y,0]);b=xy([2000,y,0]);parts.append(f'<path d="M {a[0]} {a[1]} L {b[0]} {b[1]}" stroke="#83bad0" opacity=".30"/>')
walks=json.loads((ref/'WALK_PROBES.json').read_text());attempts={a['report']['id']:a['report'] for a in walks['attempts']}
for route in walks['accepted_paths']:
    w=attempts[route['forward_report']];assert w['status']=='completed collision walk' and w['teleports_during_route']==0
    poses=[w['settled_start_pose']]+[o['after_pose'] for o in w['observations']]
    points=[xy([float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',p)][:3]) for p in poses]
    parts.append(f'<polyline points="{" ".join(f"{x:.2f},{y:.2f}" for x,y in points)}" fill="none" stroke="#f7a643" stroke-width="2"><title>{escape(route["id"])}: accepted player path; may lie under roofs</title></polyline>')
floors=list(csv.DictReader((ref/'FLOOR_DATUMS.csv').open()))
for i,f in enumerate(floors,1):
    x,y,z=[float(f[k]) for k in ['source_x','source_y','source_z']];u,v=xy([x,y,z])
    parts.append(f'<circle cx="{u}" cy="{v}" r="5" fill="#24c8ed" stroke="#071018"/><text x="{u+7}" y="{v-5}" fill="#fff" stroke="#071018" stroke-width="3" paint-order="stroke" font-family="Arial" font-size="12">{i}</text>')
parts.append('<g fill="#edf3f8" font-family="Arial" font-size="16">')
for i,f in enumerate(floors):
    x=40+(i//7)*650;y=852+(i%7)*24
    parts.append(f'<text x="{x}" y="{y}">{i+1}. {escape(f["area"])}: {float(f["source_z"])*2.54/100:+.2f} m (source Z)</text>')
parts.extend([f'<text x="40" y="1038">Orange: {len(walks["accepted_paths"])} collision-enabled paths accepted both ways. Cyan: 13 repeated floor points.</text>','<text x="40" y="1062">Grid projected at source Z=0; spacing 12.7 m. Surface elevation must be known for inverse measurements.</text>','<text x="40" y="1086">Camera holdouts include Z=-100..1000; Pit floor -159.14 is extrapolated. Roofs hide interiors and layered floors.</text>','<text x="40" y="1110">1.5 px localization allowance does not bound wall edges. No continuous wall footprint is accepted here.</text>','</g></svg>'])
(ref/'MAP_CAMERA_PLAN.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Camera residuals:',[(g['role'],round(g['maximum_residual_px'],4)) for g in groups]);print('Context:',len(floors),'floor points;',len(walks['accepted_paths']),'paths')
