"""Rebuild reviewed Tunnel stair floor points and two sampled profile charts.

Run: py -3.11 scripts/build_tunnel_stair_profile.py
Reads TUNNEL_STAIR_PROFILE.json and accepted scale. Verifies repeated corrected
floor hits and reviewed surface identity. Produces TUNNEL_STAIR_SAMPLES.csv and
TUNNEL_STAIR_PROFILE.svg. Counts, face positions and full rise/run need separate
review; chart lines show sample order only, never a continuous floor surface.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path


def points(profile):
    result={}
    for report in profile['reports']:
        assert report['source_build']==profile['source_build'] and report['status'].startswith('complete;')
        point=report['endpoints']['floor'];observations=[a for a in report['observations'] if a['feature']=='floor']
        assert len(observations)>=2 and observations[-1]['hit']==observations[-2]['hit']==point
        assert all(o['xy_error']<=.02 for o in observations[-2:])
        assert math.dist(point[:2],report['target_xy'])<=.02 and report['surface_semantics']
        assert -120<point[2]<40,'Point outside independently observed floor range; inspect identity'
        assert report['id'] not in result;result[report['id']]=point
    return result


def section_rows(profile,factor):
    """Reviewed riser point-pair rises and same-axis inter-face intervals only."""
    by_id=points(profile);faces=profile['center_riser_faces']['observations'];result=[]
    for section in profile['accepted_center_sections']:
        samples=[o for o in faces if o['station_id']==section['face_station_id']]
        assert len(samples)==2 and samples[0]['hit']==samples[1]['hit']
        before,after=[by_id[section[k]] for k in ['before_report','after_report']]
        face=samples[0]['hit'];axis=section['axis']
        assert before[axis]>face[axis]>after[axis] and before[2]<face[2]<after[2]
        rise=(after[2]-before[2])*factor
        next_section=next((s for s in profile['accepted_center_sections'] if s['branch']==section['branch'] and s['index']==section['index']+1),None)
        interval=None
        if next_section:
            next_face=next(o['hit'] for o in faces if o['station_id']==next_section['face_station_id'])
            interval=(face[axis]-next_face[axis])*factor;assert interval>0
        result.append(dict(id=section['id'],branch=section['branch'],riser=section['index'],rise_cm=round(rise,4),run_to_next_face_cm=round(interval,4) if interval is not None else '',face_x=face[0],face_y=face[1],face_z=face[2],before_report=section['before_report'],after_report=section['after_report'],limits=section['limits']))
    assert len(result)==18 and len({r['id'] for r in result})==18
    return result


def width_rows(profile,factor):
    result=[]
    for key in profile.get('accepted_width_reports',[]):
        report=profile[key];assert report['status'].startswith('complete;')
        for station in report['config']['stations']:
            assert len(station['yaws'])==2 and abs((station['yaws'][1]-station['yaws'][0])%360-180)<.001
            hits=[]
            for yaw in station['yaws']:
                samples=[o for o in report['observations'] if o['station_id']==station['id'] and o['yaw']==yaw]
                assert len(samples)==2 and samples[0]['hit']==samples[1]['hit']
                for sample in samples:
                    assert 'concrete' in str(sample['surface']) and math.dist(sample['eye_origin'],sample['hit'])>.1
                    distance=float(re.search(r'DISTANCE:\s+([0-9.]+) inches',sample['rangefinder_reply']).group(1))
                    assert abs(math.dist(sample['eye_origin'],sample['hit'])-distance)<.02
                hits.append(samples[0]['hit'])
            assert hits[0][2]==hits[1][2]
            result.append(dict(id=report['id']+'_'+station['id'],area='Tunnel Stairs',feature='Concrete wall/retaining-face tread section '+station['id'],value=round(math.dist(hits[0],hits[1])*factor,4),unit='cm',method='two repeated opposite native rays; rangefinder crosscheck; SCALE_CALIBRATION',source_id='TUNNEL_STAIR_PROFILE/'+report['id']+'/'+station['id'],confidence='confirmed repeated tread-level collision chord',tolerance='.0508 cm endpoint rounding; ray height and radial/axial direction explicit',notes='Radial curved-winder or axial straight section4 native units above sampled tread. No minimum body clearance, handrail clearance or surface interpolation inferred.'))
    return result


def plane_rows(profile):
    """Independent offset points validate each local vertical face orientation."""
    center={o['station_id']:o['hit'] for o in profile['center_riser_faces']['observations'] if o['repeat']==2}
    offset={o['station_id']:o['hit'] for o in profile['offset_riser_faces']['observations'] if o['repeat']==2}
    rows=[];pivot=[center['WEST_FACE_6'][0],center['SOUTH_FACE_3'][1]]
    for branch,labels in [('SOUTH',['X-1084','X-1116']),('WEST',['Y1064','Y1096'])]:
        for n in range(1,10):
            c=center[f'{branch}_FACE_{n}'];a,b=[offset[f'{branch}_{label}_FACE_{n}'] for label in labels]
            assert a[2]==b[2]==c[2]
            dx,dy=a[0]-c[0],a[1]-c[1];length=math.hypot(dx,dy)
            if dx<0 or (abs(dx)<1e-10 and dy>0):dx,dy=-dx,-dy
            tx,ty=dx/length,dy/length;nx,ny=-ty,tx;d=nx*c[0]+ny*c[1]
            residual=abs(nx*b[0]+ny*b[1]-d);assert residual<.02
            pivot_residual=abs(nx*pivot[0]+ny*pivot[1]-d)
            # Extrapolating a line fitted over a16-unit strip amplifies .01-unit
            # endpoint rounding at the pivot. Keep this separate from the local
            # withheld-point residual and from full-width plane certification.
            if (branch=='SOUTH' and n>=3) or (branch=='WEST' and n<=6):assert pivot_residual<.1
            rows.append(dict(id=f'{branch}_FACE_{n}',source_face_x=c[0],source_face_y=c[1],source_sample_z=c[2],tangent_bearing_degrees=math.degrees(math.atan2(ty,tx)),normal_x=nx,normal_y=ny,plane_d_source_units=d,withheld_offset_residual_source_units=residual,winder_pivot_residual_source_units=pivot_residual,scope='Local vertical face plane within32 native sampled strip; full-width extrapolation not independently certified'))
    return rows


def build(root):
    ref=root/'reference';profile=json.loads((ref/'TUNNEL_STAIR_PROFILE.json').read_text());by_id=points(profile)
    calibration=json.loads((ref/'SCALE_CALIBRATION.json').read_text());assert calibration['status'].startswith('ACCEPTED')
    factor=calibration['cm_per_source_unit'];assert factor==2.54
    rows=[dict(id=r['id'],branch=r['branch'],source_x=by_id[r['id']][0],source_y=by_id[r['id']][1],source_z=by_id[r['id']][2],x_cm=round(by_id[r['id']][0]*factor,4),y_cm=round(by_id[r['id']][1]*factor,4),z_cm=round(by_id[r['id']][2]*factor,4),surface_semantics=r['surface_semantics'],confidence='confirmed repeated collision floor point',limits='Sample points; no tread/face interpolation or render accuracy certification') for r in profile['reports']]
    with (ref/'TUNNEL_STAIR_SAMPLES.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1300" height="770">','<rect width="1300" height="770" fill="#101923"/>','<g font-family="Arial" fill="#edf3f8"><text x="40" y="40" font-size="26">Tunnel Stairs — repeated native floor sections</text><text x="40" y="69" font-size="16">Build25640462 · 2.54cm/native unit · sampled L-shaped bend · Gate1 remains FAIL</text></g>']
    for branch,x0,y0,axis,origin in [('south',70,130,1,1300),('west',70,395,0,-1100)]:
        samples=sorted([r for r in rows if r['branch']==branch],key=lambda r:-r['source_y' if axis==1 else 'source_x'])
        coords=[]
        for row in samples:
            run=(origin-row['source_y' if axis==1 else 'source_x'])*factor/100
            u=x0+run*180;v=y0+185-(row['z_cm']/100+3)*45;coords.append((u,v))
        svg.append(f'<polyline points="{" ".join(f"{u:.2f},{v:.2f}" for u,v in coords)}" fill="none" stroke="#f2ab55" opacity=".65"/>')
        for u,v in coords:svg.append(f'<circle cx="{u}" cy="{v}" r="3" fill="#35d6ed"/>')
        svg.extend([f'<path d="M {x0},{y0+205} h1050 M{x0},{y0+205} v-190" stroke="#718591" fill="none"/>',f'<text x="70" y="{y0-10}" fill="#edf3f8" font-family="Arial" font-size="18">{branch.title()} branch — {len(samples)} repeated points</text>'])
        for height in [-3,-2,-1,0,1]:
            v=y0+185-(height+3)*45
            svg.append(f'<path d="M{x0},{v} h1050" stroke="#718591" opacity=".2"/><text x="12" y="{v+4}" fill="#edf3f8" font-family="Arial" font-size="12">{height:+}m</text>')
        for meter in range(6):svg.append(f'<text x="{x0+meter*180}" y="{y0+228}" fill="#edf3f8" font-family="Arial" font-size="14">{meter}m</text>')
    svg.extend(['<g font-family="Arial" fill="#edf3f8" font-size="16">','<text x="40" y="668">Horizontal axis: distance from branch station. Vertical: source datum elevations, plotted at45px/m.</text>','<text x="40" y="696">Cyan: repeated concrete/sand/tile floor hits. Orange: sample order guides, not continuous floor geometry.</text>','<text x="40" y="724">Exact corner(-1100,1100) is rejected; adjacent1102/1098 stations retain distinct riser levels.</text>','<text x="40" y="752">Two first attempts started inside collision and are excluded; lower entry resampled safely. Face/count review pending.</text>','</g></svg>'])
    (ref/'TUNNEL_STAIR_PROFILE.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
    if profile.get('accepted_center_sections'):
        flight=section_rows(profile,factor)
        planes=plane_rows(profile)
        with (ref/'TUNNEL_RISER_PLANES.csv').open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=planes[0]);writer.writeheader();writer.writerows(planes)
        with (ref/'TUNNEL_STAIR_FLIGHT.csv').open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=flight[0]);writer.writeheader();writer.writerows(flight)
        render=profile['rendered_count_review'];register=json.loads((ref/'CAPTURE_CRASH_RECOVERY.json').read_text())
        labels=['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1780">','<rect width="1440" height="1780" fill="#101923"/>','<text x="40" y="42" fill="#edf3f8" font-family="Arial" font-size="26">Tunnel Stairs — eighteen individually corroborated riser faces</text>']
        for i,branch in enumerate(render['branches']):
            capture=next(c for c in register['captures'] if c['id']==branch['image_id']);image=(root/capture['repository_image_path']).read_bytes();assert hashlib.sha256(image).hexdigest()==capture['jpeg_sha256']
            top=95+i*795
            labels.append(f'<image x="40" y="{top}" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(image).decode()}"/>')
            labels.append(f'<text x="40" y="{top-15}" fill="#edf3f8" font-family="Arial" font-size="19">{branch["branch"].title()} section: nine visible faces; native floor/face evidence independently measured</text>')
            for n,(u,v) in enumerate(branch['pixel_centers'],1):
                pitch=40 if branch['branch']=='south' else 32
                label_y=top+max(p[1] for p in branch['pixel_centers'])+10-(n-1)*pitch
                labels.append(f'<path d="M{u+40},{v+top} L1220,{label_y}" fill="none" stroke="#ffd64f" opacity=".75"/><circle cx="{u+40}" cy="{v+top}" r="3" fill="#ffd64f"/><text x="1230" y="{label_y+5}" fill="#ffd64f" stroke="#111" stroke-width="2" paint-order="stroke" font-family="Arial" font-size="18">{n}</text>')
        labels.extend(['<text x="40" y="1705" fill="#edf3f8" font-family="Arial" font-size="16">Count annotations use inspected native image centers; they are not camera calibration anchors.</text>','<text x="40" y="1734" fill="#edf3f8" font-family="Arial" font-size="16">Side context leaves frame; terminal geometry and full side surfaces need separate review. Gate1 remains FAIL.</text>','</svg>'])
        (ref/'TUNNEL_STAIR_ANNOTATED.svg').write_text('\n'.join(labels)+'\n',encoding='utf-8')
    print(len(rows),'reviewed Tunnel stair floor points')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
