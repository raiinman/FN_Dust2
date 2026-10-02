"""Derive a bounded local B plaster corner and projected stone sample context.

Keep depth-classifier thresholds separate from architectural corner selection.
The reviewed corner uses measured nonflat front depths and calibrated pixels;
independent side rays describe only the sampled return at native Z160.
"""
import base64,csv,hashlib,json,math
from pathlib import Path
from build_local_camera import inverse_plane,project


def build(root):
    ref=root/'reference';spec=json.loads((ref/'B_COURTYARD_RETURN_REVIEW.json').read_text())
    reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']}
    selected=[reports[i] for i in spec['diagnostic_reports']]
    assert all(r['source_build']==spec['source_build'] and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01 for r in selected)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']==spec['camera_id'])
    assert camera['normal_axis']==1 and max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    image=root/spec['clean_image_path'];capture=next(c for c in camera['captures'] if c['repository_image_path']==spec['clean_image_path'])
    assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    side=selected[2];points=[]
    for y in [1780,1760,1720]:
        origins=[]
        for x in [-1700,-1680]:
            pair=[o for o in side['observations'] if o['eye_origin']==[x,y,160]]
            assert len(pair)==2 and pair[0]['repeat']==1 and pair[1]['repeat']==2 and pair[0]['hit']==pair[1]['hit'] and pair[0]['surface']==pair[1]['surface']
            assert 'surfaceprop concrete,' in str(pair[1]['surface']) and 'shape type: Mesh,' in str(pair[1]['surface'])
            assert abs(float(pair[1]['rangefinder_reply'].split()[1])-math.dist(pair[1]['eye_origin'],pair[1]['hit']))<=.02
            origins.append(pair[1]['hit'])
        assert origins[0]==origins[1];points.append(dict(native=origins[0],pixel=project(camera['projection_matrix'],origins[0])))
    # Original narrow-band control and later near-corner points: observed relief,
    # never a refitted plane or arbitrary widening of failed depth guards.
    controls=[]
    for selection in spec['front_depth_control_selections']:
        report=reports[selection['report']];tangents=selection['tangents']
        for tangent in tangents:
            obs=[o for o in report['observations'] if o['requested_tangent']==tangent]
            assert len(obs)==4 and len({tuple(o['hit']) for o in obs})==1
            controls.append(obs[0]['hit'])
    depth=[min(p[1] for p in controls)-.01,max(p[1] for p in controls)+.01]
    review=spec['rendered_corner_review'];u,v=review['pixel'];radius=review['pixel_radius'];assert radius==1.5
    corners=[inverse_plane(camera['projection_matrix'],u+du,v+dv,y,1) for y in depth for du in [-radius,radius] for dv in [-radius,radius]]
    bounds=[[min(p[i] for p in corners),max(p[i] for p in corners)] for i in range(3)]
    assert bounds[0][0]<=controls[-1][0]<=bounds[0][1] and bounds[2][0]<=160<=bounds[2][1]
    result=dict(source_build=spec['source_build'],camera_id=spec['camera_id'],front_depth_controls_native=controls,front_normal_interval_native=depth,rendered_corner_box_native=bounds,rendered_corner_box_cm=[[v*2.54 for v in b] for b in bounds],confidence='triangulated estimated local architectural corner; pixel selection and observed front relief bounded',independent_side_points=points,rejected_corner_thresholds=[dict(report=r['id'],intervals=[b['tangent_interval_native'] for b in r['brackets']],review=r['review']) for r in selected[:2]],scope=spec['scope'],gate1='FAIL')
    (ref/'B_COURTYARD_RETURN_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ref/'B_COURTYARD_RETURN_CHECKS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['axis','corner_low_native','corner_high_native','corner_low_cm','corner_high_cm','confidence'])
        for axis,b in zip('XYZ',bounds):w.writerow([axis,*b,*[v*2.54 for v in b],result['confidence']])
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="980" viewBox="0 0 1280 980">','<rect width="1280" height="980" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(image.read_bytes()).decode()}"/>','<g fill="white" font-family="Arial">','<text x="25" y="32" font-size="24">B courtyard south / bounded local return and existing stone samples</text>','<text x="25" y="66" font-size="17">Exact checked camera; main plaster relief and tapered side stay separate. Gate1 FAIL.</text>']
    svg.append(f'<rect x="{u-radius}" y="{v+100-radius}" width="{2*radius}" height="{2*radius}" fill="none" stroke="#ffbb63" stroke-width="2"/><text x="{u+12}" y="{v+94}" fill="#ffbb63" font-size="16">estimated local corner</text>')
    for n,p in enumerate(points):
        px,py=p['pixel'];svg.append(f'<circle cx="{px}" cy="{py+100}" r="4" fill="#60e4cb"/><text x="{px-112}" y="{py+120+n*18}" fill="#60e4cb" font-size="14">side Y{p["native"][1]}</text>')
    portal=json.loads((ref/'STONE_PORTAL_PROFILES.json').read_text())['portals'][0];assert portal['id']=='B'
    for ident in portal['columns']:
        r=reports[ident];assert r.get('accepted_columns')
        p=r['endpoints']['ceiling'];assert camera['tested_marker_z_range'][0]<=p[2]<=camera['tested_marker_z_range'][1]
        px,py=project(camera['projection_matrix'],p);svg.append(f'<circle cx="{px}" cy="{py+100}" r="3" fill="#bb9cff"><title>{ident}; collision intrados atY1780, not selected rendered arch edge</title></circle>')
    svg.extend([f'<text x="25" y="855" font-size="16">Local corner X[{bounds[0][0]:.3f},{bounds[0][1]:.3f}]native; Y[{depth[0]:.3f},{depth[1]:.3f}]native, at eye Z160.</text>','<text x="25" y="884" font-size="16">Gold: reviewed rendered corner box. Green: independently repeated tapered side hits.</text>','<text x="25" y="913" font-size="16">Purple: existing stone collision intrados points; depth/render offset remains separate.</text>','<text x="25" y="944" font-size="16">No full-height extrusion, exact bevel intersection, complete portal or continuous courtyard footprint.</text></g></svg>'])
    (ref/'B_COURTYARD_RETURN_CHECKS.svg').write_text('\n'.join(svg)+'\n')
    print('B local return corner bounds',bounds,'three independent side points; diagnostic thresholds excluded')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
