"""Compare independently repeated first-hit route spans at two floor heights.

Input ROUTE_AXIS_SECTIONS.json. This tests height dependence, never certifies
minimum passable width, a playerclip ray mask or a continuous architectural wall.
"""
import csv,json,math
from pathlib import Path
from build_route_axis_sections import build as validate_sections

def build(root):
    ref=root/'reference';rows,opened=validate_sections(root)
    groups={}
    for row in rows:groups.setdefault(row['floor_report'],[]).append(row)
    comparison=[]
    for ident,sections in groups.items():
        if len(sections)!=2:continue
        lo,hi=sorted(sections,key=lambda r:r['height_above_floor_native'])
        assert lo['height_above_floor_native']==35 and hi['height_above_floor_native']==64 and lo['axis']==hi['axis'] and lo['route']==hi['route'] and lo['floor_native']==hi['floor_native']
        shifts=[math.dist(json.loads(lo[k])[:2],json.loads(hi[k])[:2])*2.54 for k in ['low_native','high_native']]
        comparison.append(dict(floor_report=ident,route=lo['route'],axis=lo['axis'],lower_report=lo['report'],upper_report=hi['report'],span_at_35_native_cm=lo['span_cm'],span_at_64_native_cm=hi['span_cm'],span_change_cm=round(hi['span_cm']-lo['span_cm'],4),low_endpoint_xy_change_cm=round(shifts[0],4),high_endpoint_xy_change_cm=round(shifts[1],4),lower_low_surface=lo['low_surface'],upper_low_surface=hi['low_surface'],lower_high_surface=lo['high_surface'],upper_high_surface=hi['high_surface'],limits='Two-height point diagnostic only; shifts may be cover, curve, grade, returns or cross-area first-hit changes. No whole-route minimum, swept body clearance or playerclip-mask acceptance.'))
    assert comparison
    with (ref/'ROUTE_AXIS_HEIGHT_COMPARISON.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=comparison[0]);w.writeheader();w.writerows(comparison)
    summary=dict(source_build='25640462',heights_above_measured_floor_native=[35,64],paired_floor_stations=len(comparison),both_endpoint_xy_agreement_within_02_native=sum(max(r['low_endpoint_xy_change_cm'],r['high_endpoint_xy_change_cm'])<=.0508 for r in comparison),open_directions=opened,maximum_absolute_span_change_cm=max(abs(r['span_change_cm']) for r in comparison),status='Validated height-dependence diagnostic; no complete route clearance acceptance',scope=comparison[0]['limits'])
    (ref/'ROUTE_AXIS_HEIGHT_COMPARISON.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary))

if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
