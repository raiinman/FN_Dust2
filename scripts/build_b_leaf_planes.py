"""Validate sampled B-door leaf faces against independent height/tangent rays.

Run to rebuild B_LEAF_PLANE_CHECKS.json/CSV/SVG; render and inspect the SVG.
Fit two Z80 points per face, withhold two original points and four fresh
height/tangent points. Normal separation is a sampled parallel-plane model,
never complete body thickness, leaf ends, rendered accuracy or clearance.
"""
import base64,csv,hashlib,json,math
from pathlib import Path
from build_b_frame_sections import repeated
from build_local_camera import project


def checked(ref):
    config=json.loads((ref/'B_LEAF_PLANES.json').read_text())
    reports={r['id']:r for r in json.loads((ref/'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']}
    baseline=reports[config['baseline_report']];fresh=reports[config['independent_report']]
    for report in [baseline,fresh]:
        assert report['source_build']==config['source_build'] and report['status'].startswith('complete;')
        assert max(report['restore_numeric_errors'])<=.01 and not report.get('restore_error')
    def point(report,id):
        index=next(i for i,o in enumerate(report['observations']) if o['station_id']==id and o['repeat']==1)
        observation=repeated(report,index+1)
        assert 'surfaceprop Wood_Dense,' in str(observation['surface']) and 'shape type: Hull,' in str(observation['surface'])
        return observation['hit']
    results=[]
    for leaf in config['leaves']:
        faces=[]
        for origin in ['B_INSIDE','CT_OUTSIDE']:
            fit=[point(baseline,id) for id in leaf['fit'][origin]]
            assert len(fit)==2 and fit[0][2]==fit[1][2]==80
            delta=fit[1][1]-fit[0][1];assert delta>0
            slope=(fit[1][0]-fit[0][0])/delta;intercept=fit[0][0]-slope*fit[0][1]
            checks=[]
            for id in leaf['baseline_holds'][origin]:
                p=point(baseline,id);checks.append(dict(report=baseline['id'],station_id=id,point=p,predicted_x_native=slope*p[1]+intercept,residual_native=p[0]-slope*p[1]-intercept))
            selected=[p for p in fresh['predictions_fixed_before_capture']['predictions'] if p['leaf']==leaf['id'] and p['origin_id']==origin]
            assert len(selected)==4 and {p['height_native'] for p in selected}=={40,140}
            for prediction in selected:
                p=point(fresh,prediction['station_id']);expected=slope*p[1]+intercept
                assert abs(expected-prediction['predicted_first_x_native'])<1e-7
                checks.append(dict(report=fresh['id'],station_id=prediction['station_id'],point=p,predicted_x_native=expected,residual_native=p[0]-expected))
            maximum=max(abs(c['residual_native']) for c in checks);assert maximum<=.02
            faces.append(dict(origin_id=origin,fit=fit,slope=slope,intercept=intercept,slope_interval=[slope-.01/delta,slope+.01/delta],checks=checks,maximum_held_residual_native=maximum))
        inside,outside=faces
        assert abs(inside['slope']-outside['slope'])<1e-9
        gaps=[b[0]-a[0] for a,b in zip(inside['fit'],outside['fit'])]
        assert min(gaps)>0 and max(gaps)-min(gaps)<1e-8
        slope=inside['slope'];gap=sum(gaps)/2
        slopes=[s for f in faces for s in f['slope_interval']];assert min(slopes)>0
        # Native printer rounding plus the observed independent point residual;
        # this bound applies to the sampled plane comparison, not unseen surfaces.
        padding=.01+2*max(f['maximum_held_residual_native'] for f in faces)
        interval=[(gap-padding)/math.sqrt(1+max(slopes)**2)*2.54,(gap+padding)/math.sqrt(1+min(slopes)**2)*2.54]
        results.append(dict(id=leaf['id'],faces=faces,normal_separation_cm=gap/math.sqrt(1+slope*slope)*2.54,normal_separation_interval_cm=interval,source_angle_deg=math.degrees(math.atan(slope)),limits=config['limits']))
    return config,results


def measurement_rows(ref):
    config,results=checked(ref)
    return [dict(id='B_'+r['id'].upper()+'_LEAF_SAMPLED_NORMAL_SEPARATION',area='B Doors',feature=r['id']+' leaf sampled opposed parallel collision-face normal separation',value=round(r['normal_separation_cm'],4),unit='cm',method='two native Z80 fit endpoints per face;24 withheld baseline/independent height points total; SCALE_CALIBRATION',source_id='B_LEAF_PLANES/'+config['baseline_report']+';'+config['independent_report'],confidence='triangulated sampled parallel collision-face separation',tolerance=f'[{r["normal_separation_interval_cm"][0]:.4f},{r["normal_separation_interval_cm"][1]:.4f}]cm sampled-model numerical/observed residual bounds',notes=config['limits']) for r in results]


def build(root):
    ref=root/'reference';config,results=checked(ref)
    (ref/'B_LEAF_PLANE_CHECKS.json').write_text(json.dumps(dict(source_build=config['source_build'],leaves=results,gate1='FAIL'),indent=2)+'\n')
    measurements=measurement_rows(ref)
    with (ref/'B_LEAF_PLANE_CHECKS.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=measurements[0].keys());w.writeheader();w.writerows(measurements)
    camera=next(c for c in json.loads((ref/'LOCAL_CAMERA_CALIBRATIONS.json').read_text())['cameras'] if c['id']==config['camera_id'])
    assert max(g['maximum_residual_px'] for g in camera['groups'][1:])<1
    image=root/config['clean_image_path'];assert hashlib.sha256(image.read_bytes()).hexdigest()==config['clean_jpeg_sha256']
    data=base64.b64encode(image.read_bytes()).decode()
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="980">','<rect width="1280" height="980" fill="#14202e"/>',f'<image x="0" y="100" width="1280" height="720" href="data:image/jpeg;base64,{data}"/>','<g font-family="sans-serif" fill="white"><text x="25" y="32" font-size="23">B slanted leaf faces / independently checked collision-plane samples</text>','<text x="25" y="65" font-size="17">Outside first faces: circles=fit / diamonds=withheld. Projection is separate from rendered-surface accuracy.</text>']
    for i,r in enumerate(results):
        face=r['faces'][1];color=['#39e5cd','#ffb45e'][i]
        for p in face['fit']:
            u,v=project(camera['projection_matrix'],p);svg.append(f'<circle cx="{u}" cy="{v+100}" r="5" fill="none" stroke="{color}" stroke-width="2"/>')
        for check in face['checks']:
            u,v=project(camera['projection_matrix'],check['point']);v+=100;svg.append(f'<path d="M{u},{v-4} L{u+4},{v} L{u},{v+4} L{u-4},{v} Z" fill="none" stroke="{color}" stroke-width="1.5"/>')
        interval=r['normal_separation_interval_cm']
        svg.append(f'<text x="25" y="{850+i*30}" font-size="17">{r["id"]}: sampled normal separation [{interval[0]:.4f}, {interval[1]:.4f}]cm; angle {r["source_angle_deg"]:.4f}deg; twelve checks</text>')
    svg.extend(['<text x="25" y="930" font-size="16">Measured local face samples only; no complete body, unseen plane continuity, leaf ends, vertical height or minimum clearance.</text>','<text x="25" y="960" font-size="16">Independent native ray heights40/140, fit at80; source printing and observed check residuals explicit. Gate1 FAIL.</text></g></svg>'])
    (ref/'B_LEAF_PLANES.svg').write_text('\n'.join(svg)+'\n')
    print([(r['id'],r['normal_separation_interval_cm'],max(f['maximum_held_residual_native'] for f in r['faces'])) for r in results])


if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
