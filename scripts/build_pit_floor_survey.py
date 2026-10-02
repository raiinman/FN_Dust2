"""Evaluate a measured Pit multicolumn strip against independent point holdouts.

Run after PIT_FLOOR_SURVEY defines anchor_rows and holdout_reports. Output is
reference interpolation diagnostics only: no production mesh or acceptance by
default. Each triangle interpolates measured source XYZ; report observed error
separately from proposed tolerance and unseen-surface uncertainty.
"""
import json,math
from pathlib import Path
from build_connector_profile import points

def predict(triangle,point):
 a,b,c=triangle;xx,yy=point[:2];det=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1]);assert abs(det)>1e-6
 u=((b[1]-c[1])*(xx-c[0])+(c[0]-b[0])*(yy-c[1]))/det
 v=((c[1]-a[1])*(xx-c[0])+(a[0]-c[0])*(yy-c[1]))/det;w=1-u-v
 if min(u,v,w)<-.001:return None
 return u*a[2]+v*b[2]+w*c[2]

def build(root):
 ref=root/'reference';survey=json.loads((ref/'PIT_FLOOR_SURVEY.json').read_text());profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());p=points(profile)
 assert profile['source_build']==survey['source_build'];factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
 anchors=survey['anchor_rows'];columns=len(anchors[0]);assert len(anchors)>=2 and columns>=3 and all(len(a)==columns for a in anchors)
 excluded=set(survey['excluded_floor_reports']);assert not any(i in excluded for a in anchors for i in a)
 triangles=[]
 for lower,upper in zip(anchors,anchors[1:]):
  assert all(p[upper[i]][1]>p[lower[i]][1] for i in range(columns))
  assert all(p[row[i+1]][0]>p[row[i]][0] for row in [lower,upper] for i in range(columns-1))
  for i in range(columns-1):triangles.extend([[lower[i],lower[i+1],upper[i+1]],[lower[i],upper[i+1],upper[i]]])
 checks=[]
 for ident in survey['holdout_reports']:
  assert ident not in {i for a in anchors for i in a} and ident not in excluded
  choices=[(n,pred) for n,t in enumerate(triangles) if (pred:=predict([p[i] for i in t],p[ident])) is not None];assert choices,ident
  assert max(v for _,v in choices)-min(v for _,v in choices)<.05
  n,z=choices[0];checks.append(dict(id=ident,triangle=n,source_xyz=p[ident],predicted_z=z,residual_native=p[ident][2]-z,residual_cm=(p[ident][2]-z)*factor))
 maximum=max(abs(c['residual_native']) for c in checks)
 side_checks=[]
 side_ids=[s['holdout_id'] for s in survey.get('raised_strip_sections',[])]
 assert len(side_ids)==len(set(side_ids)) and set(side_ids)==set(survey.get('raised_strip_holdouts',[]))
 assert not set(side_ids).intersection(survey['holdout_reports'])
 side_fit_ids={s[k] for s in survey.get('raised_strip_sections',[]) for k in ['outer_id','inner_id']}
 assert not set(side_ids).intersection(side_fit_ids|excluded)
 for section in survey.get('raised_strip_sections',[]):
  outer,inner,hold=[p[section[key]] for key in ['outer_id','inner_id','holdout_id']]
  assert section['holdout_id'] not in {section['outer_id'],section['inner_id']}
  assert max(h[1] for h in [outer,inner,hold])-min(h[1] for h in [outer,inner,hold])<=.02
  u=(hold[0]-outer[0])/(inner[0]-outer[0]);assert 0<u<1
  z=outer[2]+u*(inner[2]-outer[2]);side_checks.append(dict(**section,source_xyz=hold,predicted_z=z,residual_cm=(hold[2]-z)*factor))
 result=dict(source_build=survey['source_build'],status='DIAGNOSTIC ONLY; explicit reviewed uncertainty acceptance required',triangles=[dict(id=n,point_ids=t,source_xyz=[p[i] for i in t]) for n,t in enumerate(triangles)],holdouts=checks,max_observed_residual_native=maximum,max_observed_residual_cm=maximum*factor,raised_strip_section_checks=side_checks,raised_strip_max_observed_residual_cm=max([abs(c['residual_cm']) for c in side_checks],default=None),limits='Checked-point error only; side checks are six independent local transverse checks, never continuous raised strips. Not universal unseen-surface bound, full Pit ends, near-wall excluded strips, rendered offset or whole-map truth acceptance.')
 (ref/'PIT_FLOOR_INTERPOLATION.json').write_text(json.dumps(result,indent=2)+'\n')
 xmin,xmax=min(p[i][0] for a in anchors for i in a),max(p[i][0] for a in anchors for i in a)
 ymin,ymax=min(p[i][1] for a in anchors for i in a),max(p[i][1] for a in anchors for i in a)
 zmin,zmax=min(p[i][2] for a in anchors for i in a),max(p[i][2] for a in anchors for i in a)
 sx=lambda x:160+(x-xmin)*1.2
 sy=lambda y:820-(y-ymin)*1.2
 svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1300" height="1050" viewBox="0 0 1300 1050">','<rect width="1300" height="1050" fill="#12202b"/>','<g fill="#edf4f8" font-family="sans-serif">','<text x="35" y="35" font-size="23">Pit measured floor strip — interpolation diagnostic</text>','<text x="35" y="65" font-size="16">Source X right / Y up; 2.54 cm/native unit. Sampling boundaries do not define full Pit ends.</text>']
 for t in triangles:
  coords=[p[i] for i in t];level=(sum(h[2] for h in coords)/3-zmin)/(zmax-zmin);colour=f'rgb({int(40+60*level)},{int(90+120*level)},180)'
  svg.append('<polygon points="'+' '.join(f'{sx(h[0]):.2f},{sy(h[1]):.2f}' for h in coords)+f'" fill="{colour}" stroke="#315263" stroke-width="1"/>')
 for a in anchors:
  for i in a:
   h=p[i];svg.append(f'<circle cx="{sx(h[0]):.2f}" cy="{sy(h[1]):.2f}" r="3" fill="#ffffff"><title>{i}: source {h}</title></circle>')
 for c in checks:
  h=c['source_xyz'];svg.append(f'<path d="M{sx(h[0])-4:.2f} {sy(h[1]):.2f}h8m-4 -4v8" stroke="#ffca77" stroke-width="2"><title>{c["id"]}: checked residual{c["residual_cm"]:.3f}cm</title></path>')
 for yy in [200,300,400,500,600,700]:svg.append(f'<text x="80" y="{sy(yy)+5:.2f}" font-size="14">Y{yy}</text>')
 svg += [f'<text x="160" y="860" font-size="15">X{xmin:g}..{xmax:g}; strip width varies near corners/caps.</text>',f'<text x="660" y="140" font-size="20">{len(anchors)*columns} anchors; {len(checks)} independent holdouts</text>',f'<text x="660" y="180" font-size="18">Maximum checked residual: {maximum*factor:.3f}cm</text>',f'<text x="660" y="225" font-size="16">Measured floor elevations: {zmin*factor:.2f}..{zmax*factor:.2f}cm</text>','<text x="660" y="265" font-size="16">White points: repeated anchors. Orange crosses: holdouts.</text>','<text x="660" y="305" font-size="16">Triangle shading shows sampled elevation and fit strips.</text>','<text x="660" y="355" font-size="16">Raised retaining-edge hits are excluded from the floor.</text>','<text x="660" y="395" font-size="16">Near-wall gaps and retaining ends need separate evidence.</text>','<text x="660" y="435" font-size="16">Observed holdout error is not a universal surface bound.</text>','<text x="660" y="475" font-size="16">No production mesh or full-map acceptance generated.</text>','<text x="35" y="940" font-size="17">Native collision floor reference only. Rendered surface accuracy, minimum body clearance and unsampled limits remain separate.</text>','<text x="35" y="980" font-size="17">Gate1 remains FAIL until critical dimensions, continuous layered whole-map footprint and bounded uncertainty are complete.</text>','</g></svg>']
 (ref/'PIT_FLOOR_SURVEY.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
 print(json.dumps(dict(anchor_rows=len(anchors),triangles=len(triangles),holdouts=len(checks),max_observed_residual_cm=maximum*factor,status=result['status'])))
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
