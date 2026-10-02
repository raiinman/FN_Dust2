"""Validate reviewed local camera matrices without refitting withheld markers.

Run: py -3.11 scripts/build_local_camera.py
Reads LOCAL_CAMERA_CALIBRATIONS.json, checks registered JPEG hashes, fits each
camera using only its fit group, validates independent groups and fixed-Y
inverse round trips. Pixel bounds cover localization at specified planes only;
they never establish wall identity, surface depth or hidden opening clearance.
Uses the standard library; no camera-eye or field-of-view hypothesis is fitted.
"""
import hashlib
import json
import math
from pathlib import Path


def fit_camera(anchors):
    center = [sum(a['world'][i] for a in anchors)/len(anchors) for i in range(3)]
    rows, values = [], []
    for a in anchors:
        x = [(a['world'][i]-center[i])/100 for i in range(3)]+[1]
        u, v = a['pixel']
        rows.extend([x+[0]*4+[-u*t for t in x[:3]],
                     [0]*4+x+[-v*t for t in x[:3]]])
        values.extend([u, v])
    matrix = [[sum(row[i]*row[j] for row in rows) for j in range(11)]
              +[sum(row[i]*v for row, v in zip(rows, values))] for i in range(11)]
    for i in range(11):
        pivot = max(range(i, 11), key=lambda k: abs(matrix[k][i]))
        matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
        assert abs(matrix[i][i]) > 1e-10, 'Degenerate fit anchors'
        divisor = matrix[i][i]
        matrix[i] = [v/divisor for v in matrix[i]]
        for j in range(11):
            if j != i:
                multiplier = matrix[j][i]
                matrix[j] = [v-multiplier*w for v, w in zip(matrix[j], matrix[i])]
    coefficients = [row[-1] for row in matrix]+[1]
    projection = [coefficients[i:i+4] for i in [0, 4, 8]]
    for row in projection:
        row[:3] = [v/100 for v in row[:3]]
        row[3] -= sum(v*x for v, x in zip(row[:3], center))
    return projection


def project(matrix, point):
    values = [sum(v*x for v, x in zip(row, point+[1])) for row in matrix]
    assert values[2] > 0, 'Point behind calibrated camera'
    return [values[0]/values[2], values[1]/values[2]]


def inverse_y(matrix, u, v, y):
    a, b = matrix[0][0]-u*matrix[2][0], matrix[0][2]-u*matrix[2][2]
    c, d = matrix[1][0]-v*matrix[2][0], matrix[1][2]-v*matrix[2][2]
    e = (u*matrix[2][1]-matrix[0][1])*y+u*matrix[2][3]-matrix[0][3]
    f = (v*matrix[2][1]-matrix[1][1])*y+v*matrix[2][3]-matrix[1][3]
    determinant = a*d-b*c
    assert abs(determinant) > 1e-12, 'Plane cannot be inverted'
    return [(e*d-b*f)/determinant, y, (a*f-e*c)/determinant]


def build(root):
    path = root/'reference/LOCAL_CAMERA_CALIBRATIONS.json'
    register = json.loads(path.read_text())
    for camera in register['cameras']:
        for capture in camera['captures']:
            assert hashlib.sha256((root/capture['repository_image_path']).read_bytes()).hexdigest() == capture['jpeg_sha256']
        groups = camera['groups']
        fit = [g for g in groups if g['role'] == 'fit']
        assert len(fit) == 1 and len(fit[0]['anchors']) >= 6
        matrix = fit_camera(fit[0]['anchors'])
        for group in groups:
            for anchor in group['anchors']:
                pixel = project(matrix, anchor['world'])
                anchor['projected_pixel'] = pixel
                anchor['residual_px'] = math.dist(pixel, anchor['pixel'])
                assert math.dist(inverse_y(matrix, *pixel, anchor['world'][1]), anchor['world']) < 1e-7
            group['maximum_residual_px'] = max(a['residual_px'] for a in group['anchors'])
            assert group['maximum_residual_px'] < 1, 'Independent calibration failed'
        camera['projection_matrix'] = matrix
        camera['fit_algorithm'] = 'Centered world linear least squares; denominator at fit centroid fixed to1. Independent groups excluded from fitting.'
        camera['sampled_pixel_localization_bounds'] = []
        for y in camera['bound_planes_source_y']:
            distances = []
            for anchor in groups[-1]['anchors']:
                point = [anchor['world'][0], y, anchor['world'][2]]
                u, v = project(matrix, point)
                for du, dv in [(1.5, 0), (-1.5, 0), (0, 1.5), (0, -1.5)]:
                    distances.append(math.dist(point, inverse_y(matrix, u+du, v+dv, y))*2.54)
            camera['sampled_pixel_localization_bounds'].append(dict(source_y=y, maximum_axis_1_5_pixel_displacement_cm=max(distances)))
        print(camera['id'], [(g['role'], round(g['maximum_residual_px'], 4)) for g in groups])
    path.write_text(json.dumps(register, indent=2)+'\n')


if __name__ == '__main__':
    build(Path(__file__).resolve().parent.parent)
