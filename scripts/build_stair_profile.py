"""Validate repeated Short floor samples and derive a calibrated CSV/plot.

Run with Python and matplotlib available. Samples remain points: this does not
infer tread edges, continuous slopes, or a uniform stair mesh.
"""
import csv
import json
from pathlib import Path


def build(root):
    ref = root / 'reference'
    profile = json.loads((ref / 'SHORT_STAIR_PROFILE.json').read_text())
    calibration = json.loads((ref / 'SCALE_CALIBRATION.json').read_text())
    assert profile['source_build'] == calibration['source_build']
    factor = calibration['cm_per_source_unit']
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
