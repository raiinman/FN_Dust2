"""Validate repeated Short floor samples and derive a calibrated CSV/plot.

Run with Python and matplotlib available. Samples remain points: this does not
infer tread edges, continuous slopes, or a uniform stair mesh.
"""
import csv
import json
import base64
import hashlib
from pathlib import Path


def flight_rows(profile, factor):
    flight = profile['accepted_flight']
    reports = {r['id']: r for r in profile['reports']}
    heights = []
    for identifier in flight['floor_column_ids']:
        r = reports[identifier]
        hit = r['endpoints']['floor']
        obs = [o for o in r['observations'] if o['feature'] == 'floor']
        assert obs[-1]['hit'] == obs[-2]['hit'] == hit and hit[0] == flight['source_x']
        assert obs[-1]['xy_error'] <= .02
        heights.append(hit[2])
    endpoints = profile['riser_endpoint_report']
    assert endpoints['id'] == flight['endpoint_report'] and endpoints['status'].startswith('complete;')
    assert 'restore_error' not in endpoints
    faces = []
    for station in [f'NEXT_RISER_{i}' for i in range(1, flight['count']+1)] + ['UPPER_TREAD_END']:
        obs = [o for o in endpoints['observations'] if o['station_id'] == station]
        assert len(obs) == 2 and obs[0]['hit'] == obs[1]['hit']
        assert obs[0]['hit'][0] == flight['source_x']
        faces.append(obs[0]['hit'][1])
    assert len(heights) == len(faces) == flight['count']+1
    assert all(b > a for a, b in zip(faces, faces[1:]))
    assert all(b > a for a, b in zip(heights, heights[1:]))
    return [dict(riser=i+1, source_x=flight['source_x'], source_y_face=faces[i],
        source_y_tread_end=faces[i+1], source_z_bottom_sample=heights[i],
        source_z_top_sample=heights[i+1], run_cm=round((faces[i+1]-faces[i])*factor,4),
        rise_cm=round((heights[i+1]-heights[i])*factor,4),
        confidence='confirmed repeated collision section',
        limits=flight['limits']) for i in range(flight['count'])]


def build(root):
    ref = root / 'reference'
    profile = json.loads((ref / 'SHORT_STAIR_PROFILE.json').read_text())
    calibration = json.loads((ref / 'SCALE_CALIBRATION.json').read_text())
    assert profile['source_build'] == calibration['source_build']
    factor = calibration['cm_per_source_unit']
    if 'accepted_flight' in profile:
        flight = flight_rows(profile, factor)
        with (ref/'SHORT_STAIR_FLIGHT.csv').open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=flight[0]);writer.writeheader();writer.writerows(flight)
    if 'rendered_riser_review' in profile:
        review=profile['rendered_riser_review']
        native=(root/review['image_path']).read_bytes()
        assert hashlib.sha256(native).hexdigest()==review['jpeg_sha256']
        assert sorted(a['number'] for a in review['labels'])==list(range(1,review['count']+1))
        svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="840" viewBox="0 0 1280 840">',
            '<rect width="1280" height="840" fill="#101923"/>',
            '<g font-family="Arial" fill="#fff"><text x="25" y="30" font-size="22">Short Stairs — twelve visually counted risers</text><text x="25" y="55" font-size="15">CS2 build25640462 · native pixels and pose retained · exact rise/run documented separately</text></g>',
            f'<image x="0" y="70" width="1280" height="720" href="data:image/jpeg;base64,{base64.b64encode(native).decode()}"/>']
        for a in review['labels']:
            y=a['y']+70
            label_y=662.5-24*(a['number']-1)
            svg.append(f'<path d="M430 {label_y} L{a["x"]} {y}" stroke="#24c8ed" stroke-width="2"/><circle cx="415" cy="{label_y}" r="10" fill="#101923" stroke="#24c8ed"/><text x="415" y="{label_y+5}" text-anchor="middle" fill="#fff" font-family="Arial" font-size="14">{a["number"]}</text>')
        svg.append('<text x="25" y="820" fill="#fff" font-family="Arial" font-size="15">Count matches twelve elevated collision levels; annotation does not assume uniform dimensions or exact render/collision alignment.</text></svg>')
        (ref/'SHORT_STAIR_ANNOTATED.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
    rows = []
    for report in profile['reports']:
        assert report['status'].startswith('complete;')
        floor = report['endpoints']['floor']
        samples = [o for o in report['observations'] if o['feature'] == 'floor']
        assert samples[-1]['hit'] == samples[-2]['hit'] == floor
        assert samples[-1]['xy_error'] <= .02
        rows.append(dict(id=report['id'], source_x=floor[0], source_y=floor[1],
            source_z=floor[2], x_cm=round(floor[0]*factor, 4),
            y_cm=round(floor[1]*factor, 4), z_cm=round(floor[2]*factor, 4),
            surface='; '.join(samples[-1]['hit_description']),
            confidence='confirmed repeated collision point',
            limits='Rounded ray endpoint; not player standing height or a tread boundary'))
    rows.sort(key=lambda r: (r['source_x'], r['source_y'], r['id']))
    with (ref / 'SHORT_STAIR_SAMPLES.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0])
        writer.writeheader(); writer.writerows(rows)
    import matplotlib
    matplotlib.use('Agg')
    matplotlib.rcParams['svg.hashsalt'] = 'FN_Dust2_Short_Profile'
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.subplots_adjust(bottom=.20, top=.90, left=.11, right=.98)
    for x in sorted({r['source_x'] for r in rows}):
        points = [r for r in rows if r['source_x'] == x]
        ax.scatter([(r['source_y']-1500)*factor for r in points],
            [r['z_cm'] for r in points], s=24, label=f'Source X={x:g}')
    ax.set(xlabel='Northward distance from source Y=1500 (cm)',
        ylabel='Collision surface elevation above source Z=0 (cm)',
        title='Short stair floor samples — CS2 build 25640462')
    ax.grid(alpha=.25); ax.legend()
    fig.text(.01, .03, 'Repeated corrected rays; 2.54 cm/source unit. Points do not certify tread edges or uniform rise/run.', fontsize=9)
    fig.savefig(ref / 'SHORT_STAIR_PROFILE.svg', metadata={'Date': None})
    plt.close(fig)
    print(f'Validated {len(rows)} repeated floor points; stair geometry acceptance remains separate')


if __name__ == '__main__':
    build(Path(__file__).resolve().parent.parent)
