"""Derive calibrated centimeter evidence without inferring missing architecture."""
import csv
import json
import math
from pathlib import Path


def build(root):
    ref = root / 'reference'
    calibration = json.loads((ref / 'SCALE_CALIBRATION.json').read_text())
    assert calibration['status'].startswith('ACCEPTED')
    factor = calibration['cm_per_source_unit']
    anchors = calibration['anchors']
    assert len({a['id'] for a in anchors}) >= 2
    assert all(abs(a['inch_length'] - a['native_length']) <= .02 for a in anchors)
    assert factor == 2.54
    floors = list(csv.DictReader((ref / 'FLOOR_DATUMS.csv').open()))
    physical = []
    for row in floors:
        physical.append(dict(id=row['id'], area=row['area'],
            x_cm=round(float(row['source_x'])*factor, 4),
            y_cm=round(float(row['source_y'])*factor, 4),
            z_cm=round(float(row['source_z'])*factor, 4),
            coordinate_frame='source axes; calibrated centimeters',
            source_build=row['source_build'], source_id=row['id'],
            confidence='confirmed repeated collision endpoint',
            rounding_bound_cm=.0254,
            limits='Point sample; not continuous floor or rendered-surface certification'))
    with (ref / 'PHYSICAL_FLOOR_DATUMS.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=physical[0].keys())
        w.writeheader(); w.writerows(physical)
    endpoint_reports = json.loads((ref / 'ARCHITECTURAL_ENDPOINTS.json').read_text())['reports']
    report = endpoint_reports[0]
    obs = report['observations']
    east = [o['hit'] for o in obs if o['side'] == 'east']
    west = [o['hit'] for o in obs if o['side'] == 'west']
    assert len(east) == len(west) == 2 and east[0] == east[1] and west[0] == west[1]
    assert east[0][1:] == west[0][1:]
    measurements = [dict(id='PIT_WALL_SECTION_350', area='Pit',
        feature='Opposing side-wall collision faces at source y350 z-90',
        value=round(math.dist(east[0],west[0])*factor, 4), unit='cm',
        method='two repeated architectural endpoints; native rangefinder crosscheck; SCALE_CALIBRATION',
        source_id='ARCHITECTURAL_ENDPOINTS/PIT_WALL_ENDPOINTS_001',
        confidence='confirmed collision cross-section', tolerance='.0508 cm output rounding; render/collision offset not independently bounded',
        notes='Visible retaining walls corroborated by Pit side/reverse views; not minimum route clearance or entire Pit width.')]
    by_id = {r['id']: r for r in physical}
    if 'FLOOR_PIT_LOWER_001' in by_id and 'FLOOR_PIT_UPPER_001' in by_id:
        lo, hi = by_id['FLOOR_PIT_LOWER_001'], by_id['FLOOR_PIT_UPPER_001']
        measurements.append(dict(id='PIT_SAMPLE_RISE', area='Pit',
            feature='Vertical difference between ramp sample stations source y350 and y700',
            value=round(hi['z_cm']-lo['z_cm'], 4),unit='cm',
            method='repeated offset-corrected floor endpoints; SCALE_CALIBRATION',
            source_id='ELEVATION_PROBES/FLOOR_PIT_LOWER_001;FLOOR_PIT_UPPER_001',
            confidence='confirmed sampled collision elevation difference',
            tolerance='.0508 cm output rounding; render/collision offset not independently bounded',
            notes='Sample interval, not complete ramp endpoints or total Pit rise. Horizontal sample interval 889 cm.'))
    for report in endpoint_reports[1:]:
        for section in report.get('accepted_sections', []):
            observations = [o for o in report['observations'] if o['station_id'] == section['station_id']]
            positive = [o for o in observations if o['yaw'] == 0]
            negative = [o for o in observations if o['yaw'] == 180]
            assert len(positive) == len(negative) == 2
            assert positive[0]['hit'] == positive[1]['hit']
            assert negative[0]['hit'] == negative[1]['hit']
            assert positive[0]['hit'][1:] == negative[0]['hit'][1:]
            assert positive[0]['hit'][0] > negative[0]['hit'][0]
            measurements.append(dict(id=section['id'],area=report['area'],
                feature=section['feature'],
                value=round(math.dist(positive[0]['hit'],negative[0]['hit'])*factor,4),unit='cm',
                method='two repeated collision endpoints; native rangefinder crosscheck; SCALE_CALIBRATION',
                source_id='ARCHITECTURAL_ENDPOINTS/'+report['id']+'/'+section['station_id'],
                confidence=section['confidence'],
                tolerance='.0508 cm output rounding; render/collision offset not independently bounded',
                notes=section['notes']))
    with (ref / 'MEASUREMENTS.csv').open('w', newline='') as f:
        w = csv.DictWriter(f,fieldnames=measurements[0].keys())
        w.writeheader(); w.writerows(measurements)
    print(f'Converted {len(physical)} floor points and {len(measurements)} bounded-feature measurements; Gate 1 still incomplete')


if __name__ == '__main__':
    build(Path(__file__).resolve().parent.parent)
