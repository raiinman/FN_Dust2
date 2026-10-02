"""Validate reviewed local camera matrices without refitting withheld markers.

Run: py -3.11 scripts/build_local_camera.py
Reads LOCAL_CAMERA_CALIBRATIONS.json, checks registered JPEG hashes, fits each
camera using only its fit group, validates independent groups and fixed-plane
inverse round trips. Pixel bounds cover localization at specified planes only;
they never establish wall identity, surface depth or hidden opening clearance.
Uses the standard library; no camera-eye or field-of-view hypothesis is fitted.
"""
import hashlib
import json
import math
from pathlib import Path
from build_plan_camera_model import basis, normalized
from build_pit_camera import line


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


def constrained_camera(anchors, pose):
    coordinates = [normalized(a['world'], pose)[0] for a in anchors]
    fx, cx = line([p[0] for p in coordinates], [a['pixel'][0] for a in anchors])
    fy, cy = line([p[1] for p in coordinates], [a['pixel'][1] for a in anchors])
    assert fx > 0 and fy > 0 and abs(fx/fy-1) < .005
    eye, right, up, forward = basis(pose)
    rows = [[fx*right[i]+cx*forward[i] for i in range(3)],
            [-fy*up[i]+cy*forward[i] for i in range(3)], list(forward)]
    matrix = [row+[-sum(x*y for x, y in zip(row, eye))] for row in rows]
    return matrix, dict(fx=fx, fy=fy, cx=cx, cy=cy)


def inverse_plane(matrix, u, v, coordinate, normal_axis=1):
    assert normal_axis in [0, 1, 2]
    i, j = [axis for axis in range(3) if axis != normal_axis]
    a, b = matrix[0][i]-u*matrix[2][i], matrix[0][j]-u*matrix[2][j]
    c, d = matrix[1][i]-v*matrix[2][i], matrix[1][j]-v*matrix[2][j]
    e = (u*matrix[2][normal_axis]-matrix[0][normal_axis])*coordinate+u*matrix[2][3]-matrix[0][3]
    f = (v*matrix[2][normal_axis]-matrix[1][normal_axis])*coordinate+v*matrix[2][3]-matrix[1][3]
    determinant = a*d-b*c
    assert abs(determinant) > 1e-12, 'Plane cannot be inverted'
    point = [0.0]*3
    point[normal_axis] = coordinate
    point[i], point[j] = (e*d-b*f)/determinant, (a*f-e*c)/determinant
    return point


def inverse_y(matrix, u, v, y):
    return inverse_plane(matrix, u, v, y, 1)


def build(root):
    path = root/'reference/LOCAL_CAMERA_CALIBRATIONS.json'
    register = json.loads(path.read_text())
    for camera in register['cameras']:
        for capture in camera['captures']:
            assert hashlib.sha256((root/capture['repository_image_path']).read_bytes()).hexdigest() == capture['jpeg_sha256']
        groups = camera['groups']
        normal_axis = camera.get('normal_axis', 1)
        fit = [g for g in groups if g['role'] == 'fit']
        assert len(fit) == 1 and len(fit[0]['anchors']) >= 6
        if camera.get('model') == 'constrained native pose':
            matrix, camera['intrinsics'] = constrained_camera(fit[0]['anchors'], camera['observed_pose'])
            camera['fit_algorithm'] = 'Native zero-roll pose +64 camera_up; only fx/fy/cx/cy fit from fit-group pixels. Independent groups excluded. Explicit native holdouts required at this exact pose.'
        else:
            matrix = fit_camera(fit[0]['anchors'])
            camera['fit_algorithm'] = 'Centered world linear least squares; denominator at fit centroid fixed to1. Independent groups excluded from fitting.'
        for group in groups:
            for anchor in group['anchors']:
                pixel = project(matrix, anchor['world'])
                anchor['projected_pixel'] = pixel
                anchor['residual_px'] = math.dist(pixel, anchor['pixel'])
                assert math.dist(inverse_plane(matrix, *pixel, anchor['world'][normal_axis], normal_axis), anchor['world']) < 1e-7
            group['maximum_residual_px'] = max(a['residual_px'] for a in group['anchors'])
            assert group['maximum_residual_px'] < 1, 'Independent calibration failed'
        camera['projection_matrix'] = matrix
        camera['sampled_pixel_localization_bounds'] = []
        planes = camera.get('bound_planes_native', camera.get('bound_planes_source_y'))
        assert planes, 'Declared independent depth planes required'
        for coordinate in planes:
            distances = []
            for anchor in groups[-1]['anchors']:
                point = list(anchor['world'])
                point[normal_axis] = coordinate
                u, v = project(matrix, point)
                for du, dv in [(1.5, 0), (-1.5, 0), (0, 1.5), (0, -1.5)]:
                    distances.append(math.dist(point, inverse_plane(matrix, u+du, v+dv, coordinate, normal_axis))*2.54)
            camera['sampled_pixel_localization_bounds'].append({f'source_{"xyz"[normal_axis]}':coordinate, 'maximum_axis_1_5_pixel_displacement_cm':max(distances)})
        print(camera['id'], [(g['role'], round(g['maximum_residual_px'], 4)) for g in groups])
    path.write_text(json.dumps(register, indent=2)+'\n')


if __name__ == '__main__':
    build(Path(__file__).resolve().parent.parent)
