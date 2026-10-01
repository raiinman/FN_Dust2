"""Validate reviewed connector column samples and write calibrated point CSV.

Reads CONNECTOR_SURFACE_PROFILES.json and accepted scale. Floor rays can hit
cover/roof/parapet tops; surface_semantics is mandatory. No interpolation or
implicit minimum clearance. Accepted pair IDs are consumed by physical register.
"""
import csv,json,math
from pathlib import Path

def points(profile):
    result={}
    for r in profile['reports']:
        assert r['source_build']==profile['source_build'] and r['status'].startswith('complete;')
        endpoint=r['endpoints']['floor'];samples=[o for o in r['observations'] if o['feature']=='floor']
        assert len(samples)>=2 and samples[-1]['hit']==samples[-2]['hit']==endpoint
        assert all(s['xy_error']<=.02 for s in samples[-2:])
        assert math.dist(endpoint[:2],r['target_xy'])<=.02 and r['surface_semantics']
        assert r['id'] not in result;result[r['id']]=endpoint
    return result

def build(root):
    ref=root/'reference';profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text())
    p=points(profile);factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54
    rows=[dict(id=r['id'],area=r['area'],source_x=p[r['id']][0],source_y=p[r['id']][1],source_z=p[r['id']][2],x_cm=round(p[r['id']][0]*factor,4),y_cm=round(p[r['id']][1]*factor,4),z_cm=round(p[r['id']][2]*factor,4),surface_semantics=r['surface_semantics'],confidence='confirmed repeated collision point',limits='Point evidence; source axes; no interpolation or render accuracy certification') for r in profile['reports']]
    with (ref/'CONNECTOR_SURFACE_SAMPLES.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'{len(rows)} connector points; no continuous surface inferred')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
