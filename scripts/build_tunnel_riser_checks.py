"""Rebuild fresh near-side Tunnel riser-plane checks.

Input: TUNNEL_RISER_LATERAL_CHECKS_004 in ARCHITECTURAL_ENDPOINTS and original
TUNNEL_RISER_PLANES.csv. Output: TUNNEL_RISER_LATERAL_CHECKS JSON/CSV/SVG.
Run, render and inspect. Chords join actual sampled endpoints, never exact
full-width riser endpoints or certified unseen plane continuation.
"""
import base64,csv,hashlib,json,math,re
from pathlib import Path
from build_local_camera import project


def build(root):
    ref=root/'reference'
    report=next(r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports'] if r['id']=='TUNNEL_RISER_LATERAL_CHECKS_004')
    assert report['status'].startswith('complete;') and max(report['restore_numeric_errors'])<=.01
    planes={r['id']:r for r in csv.DictReader((ref/'TUNNEL_RISER_PLANES.csv').open())}
    rows=[]
    for p in report['predictions_fixed_before_capture']['predictions']:
        plane=planes[p['face']]
        assert p['normal_xy']==[float(plane['normal_x']),float(plane['normal_y'])] and p['plane_d']==float(plane['plane_d_source_units'])
        samples=[o for o in report['observations'] if o['station_id']==p['station_id']]
        assert len(samples)==2 and samples[0]['hit']==samples[1]['hit'] and samples[0]['surface']==samples[1]['surface']
        o=samples[0]
        assert abs(math.dist(o['eye_origin'],o['hit'])-float(re.search(r'DISTANCE:\s+([0-9.]+) inches',o['rangefinder_reply']).group(1)))<.02
        residual=sum(o['hit'][i]*p['normal_xy'][i] for i in range(2))-p['plane_d']
        match='surfaceprop concrete,' in str(o['surface']) and 'shape type: Hull,' in str(o['surface'])
        stored=next(c for c in report['independent_plane_check_review']['checks'] if c['station_id']==p['station_id'])
        assert abs(residual-stored['signed_plane_residual_native'])<.000001 and match==stored['component_match']
        rows.append(dict(station=p['station_id'],face=p['face'],side=p['side'],source_x=o['hit'][0],source_y=o['hit'][1],source_z=o['hit'][2],signed_residual_native=residual,residual_cm=residual*2.54,predeclared_threshold_cm=p['maximum_predicted_plane_error_native']*2.54,component_match=match,status='point pass' if match and abs(residual)<=p['maximum_predicted_plane_error_native'] else 'rejected'))
    assert len(rows)==36
    spans=[]
    for id in planes:
        pair=[r for r in rows if r['face']==id];assert len(pair)==2
        a,b=pair;assert a['source_z']==b['source_z']
        span=math.dist([a['source_x'],a['source_y']],[b['source_x'],b['source_y']])*2.54
        spans.append(dict(face=id,sampled_endpoint_span_cm=span,scope='Chord between two near-side checked points; not entire riser width/endpoints or certified unseen continuation.'))
    result=dict(source_build=report['source_build'],checks=rows,sampled_chords=spans,maximum_residual_cm=max(abs(r['residual_cm']) for r in rows),scope=__doc__,gate1='FAIL')
    (ref/'TUNNEL_RISER_LATERAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ref/'TUNNEL_RISER_LATERAL_CHECKS.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']=='TUNNEL_STAIR_OVERHEAD_001')
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    capture=next(c for c in camera['captures'] if c['id']=='QA_TUNSTAIR_CAMERA_FIT_001_CLEAN')
    image=root/capture['repository_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==capture['jpeg_sha256']
    data=base64.b64encode(image.read_bytes()).decode()
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="960">','<rect width="1280" height="960" fill="#14202e"/>','<defs><clipPath id="frame"><rect x="0" y="100" width="1280" height="720"/></clipPath></defs>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">Tunnel stairs /36 fresh near-side riser-plane checks</text>','<text x="25" y="66" font-size="17">Green=inner / orange=outer; dashed lines join tested points only. Full-width endpoint bounds remain separate.</text>','<g clip-path="url(#frame)">']
    outside=0
    for id in planes:
        pair=[r for r in rows if r['face']==id];uv=[project(camera['projection_matrix'],[r['source_x'],r['source_y'],r['source_z']]) for r in pair]
        svg.append(f'<line x1="{uv[0][0]}" y1="{uv[0][1]+100}" x2="{uv[1][0]}" y2="{uv[1][1]+100}" stroke="#70df77" stroke-dasharray="5 5" stroke-width="1.5"/>')
        for r,(u,v) in zip(pair,uv):
            if not (4<=u<=1276 and 4<=v<=716):outside+=1;continue
            color='#70df77' if r['side']=='INNER' else '#ffb45e'
            svg.append(f'<circle cx="{u}" cy="{v+100}" r="4" fill="{color}" stroke="#14202e"/>')
    svg.extend(['</g>',f'<text x="25" y="856" font-size="17">36 fresh checks; max measured plane residual {result["maximum_residual_cm"]:.4f}cm. {outside} off-frame points retained numerically.</text>','<text x="25" y="889" font-size="16">Original local32native-strip plane fits unchanged; predictions fixed before native capture. Repeated concrete Hull hits.</text>','<text x="25" y="923" font-size="16">No full riser endpoints, unseen continuous planes, complete side/terminal or rendered-offset acceptance. Gate1 FAIL.</text></g></svg>'])
    (ref/'TUNNEL_RISER_LATERAL_CHECKS.svg').write_text('\n'.join(svg)+'\n')
    print('36 fresh plane checks; max residual',result['maximum_residual_cm'],'cm;',sum(r['status']=='rejected' for r in rows),'rejected')


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
