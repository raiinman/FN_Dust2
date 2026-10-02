"""Derive calibrated centimeter evidence without inferring missing architecture."""
import csv
import json
import math
import re
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
        # Solid cover cannot be measured by casting outward from inside it.
        # Reviewed opposite outside-origin rays instead define a local extent.
        for span in report.get('accepted_endpoint_spans', []):
            axis=span['axis'];assert axis in (0,1)
            endpoints=[]
            for key in ['low','high']:
                selector=span[key]
                samples=[o for o in report['observations']
                    if o['station_id']==selector['station_id'] and o['yaw']==selector['yaw']]
                assert len(samples)==2 and samples[0]['hit']==samples[1]['hit']
                for sample in samples:
                    distance=re.search(r'DISTANCE:\s+(-?\d+(?:\.\d+)?) inches',sample['rangefinder_reply'])
                    assert distance and abs(float(distance.group(1))-math.dist(sample['eye_origin'],sample['hit']))<=.02
                    assert math.dist(sample['eye_origin'],sample['hit'])>=.1
                endpoints.append(samples[0]['hit'])
            low,high=endpoints
            assert all(low[i]==high[i] for i in range(3) if i!=axis)
            assert high[axis]>low[axis]
            assert span['low']['yaw']==(0 if axis==0 else 90)
            assert span['high']['yaw']==(180 if axis==0 else -90)
            measurements.append(dict(id=span['id'],area=report['area'],feature=span['feature'],
                value=round(math.dist(low,high)*factor,4),unit='cm',
                method='two repeated opposite outside-origin collision endpoints; native rangefinder crosscheck; SCALE_CALIBRATION',
                source_id='ARCHITECTURAL_ENDPOINTS/'+report['id']+'/'+span['id'],
                confidence=span['confidence'],
                tolerance='.0508 cm output rounding; sampled extent; render offsets separate',notes=span['notes']))
        for section in report.get('accepted_sections', []):
            observations = [o for o in report['observations'] if o['station_id'] == section['station_id']]
            axis = section.get('axis',0)
            assert axis in (0,1)
            positive = [o for o in observations if o['yaw'] == (0 if axis == 0 else 90)]
            negative = [o for o in observations if o['yaw'] == (180 if axis == 0 else -90)]
            assert len(positive) == len(negative) == 2
            assert positive[0]['hit'] == positive[1]['hit']
            assert negative[0]['hit'] == negative[1]['hit']
            assert all(positive[0]['hit'][i] == negative[0]['hit'][i] for i in range(3) if i != axis)
            assert positive[0]['hit'][axis] > negative[0]['hit'][axis]
            measurements.append(dict(id=section['id'],area=report['area'],
                feature=section['feature'],
                value=round(math.dist(positive[0]['hit'],negative[0]['hit'])*factor,4),unit='cm',
                method='two repeated collision endpoints; native rangefinder crosscheck; SCALE_CALIBRATION',
                source_id='ARCHITECTURAL_ENDPOINTS/'+report['id']+'/'+section['station_id'],
                confidence=section['confidence'],
                tolerance='.0508 cm output rounding; render/collision offset not independently bounded',
                notes=section['notes']))
        for column in report.get('accepted_columns', []):
            floor,overhead = [report['endpoints'][name] for name in ('floor','ceiling')]
            assert math.dist(floor[:2],overhead[:2]) <= .04 and overhead[2] > floor[2]
            for feature,endpoint in [('floor',floor),('ceiling',overhead)]:
                samples = [o for o in report['observations'] if o['feature'] == feature]
                assert len(samples) >= 2 and samples[-1]['hit'] == samples[-2]['hit'] == endpoint
                assert samples[-1]['xy_error'] <= .02
            measurements.append(dict(id=column['id'],area=report['area'],feature=column['feature'],
                value=round((overhead[2]-floor[2])*factor,4),unit='cm',
                method='repeated corrected floor/first-overhead endpoints within .04 native XY; SCALE_CALIBRATION',
                source_id='ARCHITECTURAL_ENDPOINTS/'+report['id'],confidence=column['confidence'],
                tolerance='.0508 cm output rounding; component interpretation bounded to first collision hull',
                notes=column['notes']))
    profile_path = ref / 'SHORT_STAIR_PROFILE.json'
    if profile_path.exists():
        profile = json.loads(profile_path.read_text())
        reports = {r['id']: r for r in profile['reports']}
        for interval in profile.get('accepted_intervals', []):
            points = []
            for key in ('from_report', 'to_report'):
                report = reports[interval[key]]
                endpoint = report['endpoints']['floor']
                samples = [o for o in report['observations'] if o['feature'] == 'floor']
                assert samples[-1]['hit'] == samples[-2]['hit'] == endpoint
                assert samples[-1]['xy_error'] <= .02
                points.append(endpoint)
            assert points[1][2] > points[0][2]
            measurements.append(dict(id=interval['id'], area=profile['area'],
                feature=interval['feature'], value=round((points[1][2]-points[0][2])*factor,4),
                unit='cm', method='repeated corrected floor point pair; SCALE_CALIBRATION',
                source_id='SHORT_STAIR_PROFILE/'+interval['from_report']+';'+interval['to_report'],
                confidence='confirmed sampled collision elevation difference',
                tolerance='.0508 cm output rounding; sample stations explicit', notes=interval['notes']))
        if 'accepted_flight' in profile:
            from build_stair_profile import flight_rows
            flight=flight_rows(profile,factor)
            for row in flight:
                for dimension in ('rise','run'):
                    measurements.append(dict(id=f'SHORT_RISER_{row["riser"]}_{dimension.upper()}',
                        area='Short Stairs',feature=f'Center collision section riser {row["riser"]} {dimension}',
                        value=row[dimension+'_cm'],unit='cm',
                        method='repeated riser-face rays and center floor columns; SCALE_CALIBRATION',
                        source_id='SHORT_STAIR_PROFILE/SHORT_CENTER_FLIGHT_001',
                        confidence=row['confidence'],
                        tolerance='.0508 cm output rounding; sampled center section; render offset unbounded',
                        notes=row['limits']))
            for dimension in ('rise','run'):
                measurements.append(dict(id='SHORT_FLIGHT_'+dimension.upper(),area='Short Stairs',
                    feature='Complete sampled center collision flight '+dimension,
                    value=round(sum(row[dimension+'_cm'] for row in flight),4),unit='cm',
                    method='outer repeated face/floor endpoints; SCALE_CALIBRATION',
                    source_id='SHORT_STAIR_PROFILE/SHORT_CENTER_FLIGHT_001',
                    confidence='confirmed repeated collision section',
                    tolerance='.0508 cm outer endpoint rounding; render offset unbounded',
                    notes=profile['accepted_flight']['limits']))
    connector_path = ref / 'CONNECTOR_SURFACE_PROFILES.json'
    if connector_path.exists():
        from build_connector_profile import points
        profile = json.loads(connector_path.read_text())
        point_by_id = points(profile)
        for pair in profile.get('accepted_pairs', []):
            assert pair['dimension'] in ('rise','horizontal_interval')
            first, last = [point_by_id[pair[k]] for k in ('from_report','to_report')]
            value = last[2]-first[2] if pair['dimension']=='rise' else math.dist(first[:2],last[:2])
            assert value > 0
            measurements.append(dict(id=pair['id'],area=pair['area'],feature=pair['feature'],
                value=round(value*factor,4),unit='cm',
                method='two reviewed repeated corrected collision points; SCALE_CALIBRATION',
                source_id='CONNECTOR_SURFACE_PROFILES/'+pair['from_report']+';'+pair['to_report'],
                confidence='confirmed sampled collision point-pair difference',
                tolerance='.0508 cm output rounding; samples explicit; render offset unbounded',notes=pair['notes']))
    tunnel_path=ref/'TUNNEL_STAIR_PROFILE.json'
    if tunnel_path.exists():
        from build_tunnel_stair_profile import section_rows,width_rows
        profile=json.loads(tunnel_path.read_text())
        if profile.get('accepted_center_sections'):
            flight=section_rows(profile,factor)
            for row in flight:
                for dimension,key in [('rise','rise_cm'),('inter-face run','run_to_next_face_cm')]:
                    if row[key]=='':continue
                    measurements.append(dict(id=row['id']+'_'+('RISE' if dimension=='rise' else 'RUN'),area='Tunnel Stairs',feature='Surveyed '+row['branch']+' section riser '+str(row['riser'])+' '+dimension,value=row[key],unit='cm',method='repeated vertical concrete face and adjacent corrected floor points; SCALE_CALIBRATION',source_id='TUNNEL_STAIR_PROFILE/'+row['id'],confidence='confirmed repeated collision section',tolerance='.0508 cm endpoint rounding; sampled axial section; rendered offsets separate',notes=row['limits']))
            measurements.append(dict(id='TUNNEL_SAMPLED_FLIGHT_RISE',area='Tunnel Stairs',feature='Full sampled stair collision rise between first lower adjacent floor and upper top tread',value=round(sum(r['rise_cm'] for r in flight),4),unit='cm',method='eighteen reviewed floor point-pair rises; SCALE_CALIBRATION',source_id='TUNNEL_STAIR_PROFILE/accepted_center_sections',confidence='confirmed sampled collision stair rise',tolerance='.0508 cm outer endpoint rounding; adjacent floor point identities explicit',notes='Lower sampleY1252 is just before first face1248.03; upper sampleX-1268 behind final face-1263.97. Curved stair run and side surfaces remain separate.'))
        measurements.extend(width_rows(profile,factor))
    if (ref / 'A_ENTRY_STAIR_PROFILE.json').exists():
        from build_a_entry_stairs import measurement_rows
        measurements.extend(measurement_rows(ref))
    if (ref / 'B_EXIT_STAIR_PROFILE.json').exists():
        from build_b_exit_stairs import measurement_rows
        measurements.extend(measurement_rows(ref))
    if (ref / 'ARCHITECTURAL_BOUNDARIES.json').exists():
        from build_architectural_boundaries import measurement_rows
        measurements.extend(measurement_rows(ref))
    if (ref / 'B_FRAME_SECTIONS.json').exists():
        from build_b_frame_sections import measurement_rows
        measurements.extend(measurement_rows(ref))
    if (ref / 'B_LEAF_PLANES.json').exists():
        from build_b_leaf_planes import measurement_rows
        measurements.extend(measurement_rows(ref))
    if (ref / 'B_POST_CAP_SECTIONS.json').exists():
        from build_b_post_caps import measurement_rows
        measurements.extend(measurement_rows(ref))
    with (ref / 'MEASUREMENTS.csv').open('w', newline='') as f:
        w = csv.DictWriter(f,fieldnames=measurements[0].keys())
        w.writeheader(); w.writerows(measurements)
    print(f'Converted {len(physical)} floor points and {len(measurements)} bounded-feature measurements; Gate 1 still incomplete')


if __name__ == '__main__':
    build(Path(__file__).resolve().parent.parent)
