"""Rebuild sampled flat B-post collision-cap extents and their separation.

Opposing Z80 normal-band transitions plus independent Z40/140 checks delimit
flat caps. Off hits include inset hinge timber; they are not central leaf
planes. Outputs JSON/CSV/SVG; render and inspect. No full post body, continuous
height extent, exact rendered edge or minimum aperture clearance is accepted.
"""
import base64,csv,hashlib,json
from pathlib import Path
from build_b_frame_sections import repeated,rows as frame_rows
from build_local_camera import project


def sections(ref):
    config=json.loads((ref/'B_POST_CAP_SECTIONS.json').read_text())
    reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']}
    transition,heights=[reports[config[key]] for key in ['transition_report','height_report']]
    for report in [transition,heights]:
        assert report['source_build']==config['source_build'] and report['status'].startswith('complete;')
        assert max(report['restore_numeric_errors'])<=.01 and not report.get('restore_error')
    assert transition['config']['normal_band_is_classifier'] and transition['config']['on_material']=='Wood_Dense'
    outer_config,outer=frame_rows(ref);result=[]
    for section in outer:
        height=section['height_native'];inner=[]
        for end in section['ends']:
            assert abs(end['faces']['B_INSIDE']['timber'][0]+1345.78)<=.01
            assert abs(end['faces']['CT_OUTSIDE']['timber'][0]+1294.22)<=.01
        for end in ['south','north']:
            intervals=[]
            for origin,expected_normal in [('B_INSIDE',-1345.78),('CT_OUTSIDE',-1294.22)]:
                if height==80:
                    bracket=next(b for b in transition['brackets'] if b['id']==end+'_post_to_leaf' and b['origin_id']==origin)
                    on,off=[repeated(transition,bracket[role]['observation_index']) for role in ['on','off']]
                    interval=bracket['tangent_interval_native'];assert interval[1]-interval[0]<=.02
                else:
                    case=next(c for c in heights['cases_fixed_before_capture']['cases'] if c['height_native']==height and c['origin_id']==origin and c['end_id']==end.upper())
                    observations=[]
                    for role in ['on','off']:
                        index=next(i for i,o in enumerate(heights['observations']) if o['station_id']==case[role+'_station'] and o['repeat']==1)
                        observations.append(repeated(heights,index+1))
                    on,off=observations;interval=sorted([on['eye_origin'][1],off['eye_origin'][1]])
                    assert max(abs(x-y) for x,y in zip(interval,case['requested_interval']))<=.00001
                for observation in [on,off]:
                    assert observation['eye_origin'][2]==height and 'surfaceprop Wood_Dense,' in str(observation['surface']) and 'shape type: Hull,' in str(observation['surface'])
                assert abs(on['hit'][0]-expected_normal)<=.01 and abs(off['hit'][0]-expected_normal)>1
                assert (on['hit'][1]<off['hit'][1])==(end=='south')
                intervals.append(interval)
            assert max(i[0] for i in intervals)<=min(i[1] for i in intervals)
            inner.append(dict(end=end,interval_native=[min(i[0] for i in intervals)-.005,max(i[1] for i in intervals)+.005],opposed_raw_intervals=intervals))
        result.append(dict(height_native=height,outer=section['ends'],inner=inner))
    # Enclose every independently observed height instead of treating their
    # overlap as a precision improvement. No interpolation between heights.
    bounds={}
    for role in ['outer','inner']:
        bounds[role]={}
        for i,end in enumerate(['south','north']):
            intervals=[s[role][i]['tangent_interval_native' if role=='outer' else 'interval_native'] for s in result]
            bounds[role][end]=[min(b[0] for b in intervals),max(b[1] for b in intervals)]
    south,north=[bounds['inner'][end] for end in ['south','north']]
    measurements=[dict(id='B_FLAT_POST_CAP_SEPARATION',feature='Separation between inner flat post collision-cap terminations at sampled heights',interval_cm=[(north[0]-south[1])*2.54,(north[1]-south[0])*2.54])]
    for end in ['south','north']:
        outer,inner=[bounds[role][end] for role in ['outer','inner']]
        first,last=(outer,inner) if end=='south' else (inner,outer)
        assert last[0]>first[1]
        measurements.append(dict(id='B_'+end.upper()+'_FLAT_POST_CAP_WIDTH',feature=end+' flat post collision-cap lateral extent at sampled heights',interval_cm=[(last[0]-first[1])*2.54,(last[1]-first[0])*2.54]))
    return config,result,bounds,measurements


def measurement_rows(ref):
    config,_,_,measurements=sections(ref)
    return [dict(id=m['id'],area='B Doors',feature=m['feature'],value=round(sum(m['interval_cm'])/2,4),unit='cm',method='opposing first-face normal-band transitions; independent Z40/140 brackets; SCALE_CALIBRATION',source_id='B_POST_CAP_SECTIONS/'+config['transition_report']+';'+config['height_report'],confidence='bounded sampled flat collision-cap sections',tolerance=f'[{m["interval_cm"][0]:.4f},{m["interval_cm"][1]:.4f}]cm enclosing all sampled heights',notes=config['limits']) for m in measurements]


def build(root):
    ref=root/'reference';config,result,bounds,measurements=sections(ref)
    (ref/'B_POST_CAP_MEASUREMENTS.json').write_text(json.dumps(dict(source_build=config['source_build'],sections=result,enclosing_sampled_bounds=bounds,measurements=measurements,limits=config['limits'],gate1='FAIL'),indent=2)+'\n')
    rows=measurement_rows(ref)
    with (ref/'B_POST_CAP_MEASUREMENTS.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']==config['camera_id'])
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    image=root/config['clean_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==config['clean_jpeg_sha256']
    data=base64.b64encode(image.read_bytes()).decode()
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1010">','<rect width="1280" height="1010" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">B flat post collision caps / independent opposing sections</text>','<text x="25" y="65" font-size="17">Native projected cap terminations at Z40/80/140. Inset hinge timber and leaf faces are separate.</text>']
    for height in [40,80,140]:
        for end in ['south','north']:
            pixels=[]
            for role in ['outer','inner']:
                y=sum(bounds[role][end])/2;u,v=project(camera['projection_matrix'],[-1294.22,y,height]);pixels.append((u,v+100));svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="none" stroke="#39e5cd" stroke-width="1.5"/>')
            svg.append(f'<line x1="{pixels[0][0]}" y1="{pixels[0][1]}" x2="{pixels[1][0]}" y2="{pixels[1][1]}" stroke="#39e5cd" stroke-width="2"/>')
    for i,m in enumerate(measurements):
        interval=m['interval_cm'];svg.append(f'<text x="25" y="{850+i*27}" font-size="17">{m["id"]}: [{interval[0]:.4f}, {interval[1]:.4f}]cm</text>')
    svg.extend(['<text x="25" y="950" font-size="16">Flat cap sections only; separation is not inner aperture or minimum leaf clearance. No full post body accepted.</text>','<text x="25" y="980" font-size="16">Bounds enclose all sampled heights; no unseen height interpolation or exact rendered edge agreement. Gate1 FAIL.</text></g></svg>'])
    (ref/'B_POST_CAP_SECTIONS.svg').write_text('\n'.join(svg)+'\n')
    print(measurements)


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
