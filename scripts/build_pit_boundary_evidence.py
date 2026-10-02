"""Join measured Pit closing faces, nearby ground and existing wall checks.

Rebuild/render/inspect PIT_BOUNDARY_EVIDENCE JSON/SVG. Native XY is a measured
point plan with separate elevations, not a closed architectural polygon.
"""
import hashlib,json,math,re
from pathlib import Path

def repeated_south(report,index):
    a,o=report['observations'][index-1:index+1]
    assert a['repeat']==1 and o['repeat']==2 and a['hit']==o['hit'] and a['surface']==o['surface'] and a['pose']==o['pose']
    v=[float(s) for s in re.findall(r'-?\d+(?:\.\d+)?',o['pose'])];eye=v[:2]+[v[2]+64]
    assert len(v)==6 and math.dist(eye,o['eye_origin'])<=.01 and abs(v[3])<=.01 and abs(v[5])<=.01 and abs(v[4]+90)<=.01
    distance=float(re.search(r'DISTANCE:\s+([0-9.]+) inches',o['rangefinder_reply']).group(1));assert math.dist(eye,o['hit'])>.1 and abs(distance-math.dist(eye,o['hit']))<.02
    assert abs(o['hit'][0]-eye[0])<=.02 and abs(o['hit'][2]-eye[2])<=.02
    return o

def leaf_section(ref):
    spec=json.loads((ref/'PIT_LOW_LEAF_REVIEW.json').read_text())
    r=next(r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports'] if r['id']==spec['report'])
    assert r['source_build']==spec['source_build']=='25640462' and r['status'].startswith('complete;') and max(r['restore_numeric_errors'])<=.01
    assert r['config']['normal_axis']==1 and r['config']['height_native']==-160 and len(r['brackets'])==4
    assert len({o['normal_coordinate'] for o in r['config']['origins']})==2
    ends={};points={}
    for end in ['west','east']:
        brackets=[b for b in r['brackets'] if b['id']==spec[end+'_bracket']];assert len(brackets)==2
        assert brackets[0]['tangent_interval_native']==brackets[1]['tangent_interval_native'];interval=brackets[0]['tangent_interval_native'];assert interval[1]-interval[0]<=.1
        samples=[]
        for b in brackets:
            on,off=[repeated_south(r,b[k]['observation_index']) for k in ['on','off']]
            assert 'surfaceprop Wood_Dense,' in str(on['surface']) and 'surfaceprop concrete,' in str(off['surface']) and all('shape type: Hull,' in str(o['surface']) for o in [on,off])
            assert abs(on['hit'][1]-170.93)<=.02 and on['hit'][2]==off['hit'][2]==-160
            samples.append([on['hit'],off['hit']])
        assert samples[0]==samples[1];ends[end]=interval;points[end]=samples[0]
    padding=spec['numerical_allowance_native'];assert padding==.01
    bounds=[(ends['east'][0]-ends['west'][1]-2*padding)*2.54,(ends['east'][1]-ends['west'][0]+2*padding)*2.54]
    return dict(source_build=spec['source_build'],report=spec['report'],ends_native_x=ends,points=points,width_interval_cm=bounds,value_cm=sum(bounds)/2,scope=spec['scope'])

def measurement_rows(ref):
    r=leaf_section(ref);bounds=r['width_interval_cm']
    return [dict(id='PIT_CLOSED_WOOD_Z160LOW_WIDTH',area='Pit',feature='Lower closed timber facing material width at nativeZ-160',value=round(r['value_cm'],4),unit='cm',method='two independent outside origins, repeated firstWood/concrete Hull tangent brackets; SCALE_CALIBRATION',source_id='PIT_LOW_LEAF_REVIEW/'+r['report'],confidence='confirmed bounded local collision-facing width',tolerance=f'Interval[{bounds[0]:.5f},{bounds[1]:.5f}]cm including .01native per-end allowance; render seams separate',notes=r['scope'])]

def build(root):
    ref=root/'reference';arch=json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())
    south=next(r for r in arch['reports'] if r['id']=='PIT_SOUTH_LOW_FACE_001')
    assert south['source_build']=='25640462' and south['status'].startswith('complete;') and max(south['restore_numeric_errors'])<=.01
    profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());review=profile['pit_south_ground_review'];assert max(review['driver_recovery']['restore_numeric_errors'])<=.01
    reports={r['id']:r for r in profile['reports']};rows=[]
    for x,material,normal in [(1306,'concrete',175.93),(1400,'Wood_Dense',170.93),(1542,'concrete',176.03)]:
        faces=[]
        for y in [200,220]:
            index=next(i for i,o in enumerate(south['observations']) if o['station_id']==f'X{x}_Y{y}_Z160LOW' and o['repeat']==2)
            o=repeated_south(south,index)
            assert f'surfaceprop {material},' in str(o['surface']) and 'shape type: Hull,' in str(o['surface']);faces.append(o['hit'])
        assert faces[0]==faces[1]==[x,normal,-160]
        r=reports[f'PIT_SOUTH_GROUND_X{x}_002'];pair=[o for o in r['observations'] if o['feature']=='floor'][-2:]
        assert pair[0]['hit']==pair[1]['hit']==r['endpoints']['floor'] and all(o['xy_error']<=.02 for o in pair)
        point=r['endpoints']['floor'];assert point[0]==x and abs(point[1]-normal-2)<=.01 and 'surfaceprop sand,' in str(pair[1]['hit_description'])
        rows.append(dict(x=x,closed_face=faces[0],closed_face_material=material,adjacent_floor=point,floor_z_cm=point[2]*2.54,scope='Floor point2native before measured face; exact contact and unsampled corner returns separate.'))
    candidates=json.loads((ref/'WALL_BOUNDARY_CHECKS.json').read_text())
    walls=[c for c in candidates['candidates'] if c['area']=='PIT'];assert len(walls)==16
    for c in walls:
        assert c['result']=='agrees at checked point only' and c['check_axis_error_native']<=.02 and c['axis']==0
        assert 'surfaceprop concrete,' in str(c['check']['surface']) and 'shape type: Mesh,' in str(c['check']['surface'])
        assert all(p[0] in [1272,1592] and p[2]==-66 for p in [c['from_point'],c['to_point'],c['check']['hit']])
    first=reports['PIT_SOUTH_GROUND_X1400_002']['endpoints']['floor'];last=reports['PIT_CENTER_X1400_Y750_001']['endpoints']['floor'];interval=math.dist(first[:2],last[:2])*2.54;rise=(last[2]-first[2])*2.54
    image_ids=['QA_PIT_REVERSE_RECOVERY_001','QA_PIT_BOTTOM_RECOVERY_001','QA_PIT_FORWARD_RECOVERY_001']
    registry=json.loads((ref/'IMAGE_REVIEW.json').read_text());captures=[c for name in registry['capture_registers'] for c in json.loads((ref/name).read_text())['captures']]
    component_captures=[]
    for id in image_ids:
        capture=next(c for c in captures if c['id']==id)
        assert hashlib.sha256((root/capture['repository_image_path']).read_bytes()).hexdigest()==capture['jpeg_sha256']
        component_captures.append({k:capture[k] for k in ['id','repository_image_path','jpeg_sha256','pose_command']})
    leaf=leaf_section(ref) if (ref/'PIT_LOW_LEAF_REVIEW.json').exists() else None
    result=dict(source_build='25640462',south_sections=rows,lower_closed_leaf=leaf,side_wall_checks=walls,near_back_to_street=dict(first=first,last=last,horizontal_interval_cm=interval,rise_cm=rise),reviewed_component_captures=component_captures,scope='Closed southern timber leaf and flanking masonry identified in reviewed ground views. Wall checks coincide with visible opposite plaster retaining walls, but only checked points are accepted. Roof/cap hides southern floor in calibrated overhead. No straight south wall, full terminal/curved corner, full Pit polygon or entire graded floor inferred.',gate1='FAIL')
    (ref/'PIT_BOUNDARY_EVIDENCE.json').write_text(json.dumps(result,indent=2)+'\n')
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1100">','<rect width="1400" height="1100" fill="#14202e"/><g font-family="Arial" fill="white"><text x="30" y="40" font-size="25">Pit / measured closing boundary and side-wall evidence</text><text x="30" y="75" font-size="17">Native XY point plan. Opposite walls atX1272/1592; back timber recess and side masonry stay separate. Gate1 FAIL.</text>']
    sx=lambda x:140+(x-1250)*1.6;sy=lambda y:840-(y-160)*1.1
    for y in [180,200,350,500,650,750]:svg.append(f'<path d="M120,{sy(y)}H720" stroke="#506477"/><text x="30" y="{sy(y)+5}" font-size="15">Y{y}</text>')
    for x in [1272,1306,1400,1542,1592]:svg.append(f'<path d="M{sx(x)},175V850" stroke="#506477"/><text x="{sx(x)-27}" y="880" font-size="15">X{x}</text>')
    seen=set()
    for c in walls:
        for point in [c['from_point'],c['to_point'],c['check']['hit']]:
            key=tuple(point)
            if key in seen:continue
            seen.add(key);svg.append(f'<circle cx="{sx(point[0])}" cy="{sy(point[1])}" r="3" fill="#ca92ff"/>')
    for row in rows:
        for key,color in [('closed_face','#ffc75d'),('adjacent_floor','#49f6e0')]:
            p=row[key];svg.append(f'<circle cx="{sx(p[0])}" cy="{sy(p[1])}" r="4" fill="{color}" stroke="#14202e"/>')
    if leaf:
        for samples in leaf['points'].values():
            for p in samples:svg.append(f'<circle cx="{sx(p[0])}" cy="{sy(p[1])}" r="4" fill="#f9f9f9" stroke="#14202e"/>')
        low,high=leaf['width_interval_cm'];svg.append(f'<text x="790" y="818" font-size="17">White: low closedWood width[{low:.3f},{high:.3f}]cm.</text>')
    for p,color in [(first,'#49f6e0'),(last,'#49f6e0')]:svg.append(f'<circle cx="{sx(p[0])}" cy="{sy(p[1])}" r="6" fill="{color}"/>')
    svg.extend(['<text x="790" y="175" font-size="20">Amber: two-origin low faceZ-160</text>','<text x="790" y="208" font-size="17">X1306 masonryY175.93</text>','<text x="790" y="241" font-size="17">X1400 closedWoodY170.93</text>','<text x="790" y="274" font-size="17">X1542 masonryY176.03</text>','<text x="790" y="327" font-size="20">Cyan: nearby sand floor points</text>'])
    for n,row in enumerate(rows):svg.append(f'<text x="790" y="{365+n*33}" font-size="17">X{row["x"]}: Z{row["adjacent_floor"][2]:.2f} / {row["floor_z_cm"]:.4f}cm</text>')
    svg.extend(['<text x="790" y="495" font-size="18">Floor points2native before face.</text>','<text x="790" y="528" font-size="17">Offsets are not exact contact measurements.</text>',f'<text x="790" y="592" font-size="18">Selected nearback-to-street rise{rise:.4f}cm</text>',f'<text x="790" y="625" font-size="18">Horizontal interval{interval:.4f}cm</text>','<text x="790" y="658" font-size="17">Point-pair run, not walkingdistance or exact ramp ends.</text>','<text x="790" y="722" font-size="18">Purple:16 independent wall-line checks.</text>','<text x="790" y="755" font-size="17">Points atZ-66; full wall ends/heights unaccepted.</text>','<text x="30" y="940" font-size="17">Back ground is graded; three native elevations differ. Frame/door depth changes cannot become one flat southern wall.</text>','<text x="30" y="976" font-size="17">Existing80 anchor /35 independent floor checks support sampled road strip; curb/cap/near-wall gaps remain separate.</text>','<text x="30" y="1012" font-size="17">Ground views reveal the closed doors and side returns. Overhead cap hides these points; do not infer rendered visibility.</text>','<text x="30" y="1060" font-size="19">Full curved returns, exact floor-wall contacts, complete footprint and overlapping whole-map layers remain open.</text></g></svg>'])
    (ref/'PIT_BOUNDARY_EVIDENCE.svg').write_text('\n'.join(svg)+'\n')
    print('Three independently checked closing sections;',len(walls),'side-wall checks; rise/run',rise,interval)

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
