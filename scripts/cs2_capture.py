"""Capture one existing local CS2 camera; keep output outside the repository.

Usage: py -3.11 scripts/cs2_capture.py ID --addon PATH --output PATH
Optional --pose X Y Z PITCH YAW moves the survey camera (requires local cheats).
Output: original TGA, PNG preview and JSON provenance/pose/hashes. No packages
are read. Only relative screenshot basenames are sent to the game.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct
import zlib
from cs2_console import exchange


def preview_tga(source, target):
    data = source.read_bytes()
    ident, cmap, kind, _, _, _, _, _, width, height, bits, desc = struct.unpack(
        '<BBBHHBHHHHBB', data[:18])
    if cmap or kind != 2 or bits not in (24, 32) or desc & 16:
        raise ValueError('Only uncompressed left-origin 24/32-bit game TGA supported')
    step = bits // 8
    pixels = data[18 + ident:]
    if len(pixels) < width * height * step:
        raise ValueError('Truncated TGA')
    rows = []
    for y in range(height):
        sy = y if desc & 32 else height - 1 - y
        row = pixels[sy * width * step:(sy + 1) * width * step]
        rows.append(b'\0' + b''.join(row[x + 2:x + 3] + row[x + 1:x + 2]
                                     + row[x:x + 1] for x in range(0, len(row), step)))

    def chunk(kind, body):
        return (struct.pack('>I', len(body)) + kind + body
                + struct.pack('>I', zlib.crc32(kind + body) & 0xffffffff))
    target.write_bytes(b'\x89PNG\r\n\x1a\n'
                      + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
                      + chunk(b'IDAT', zlib.compress(b''.join(rows))) + chunk(b'IEND', b''))
    return width, height


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('id')
    p.add_argument('--addon', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--pose', type=float, nargs=5)
    a = p.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_]{1,64}', a.id):
        p.error('ID must be a safe short basename')
    out = a.output.resolve()
    repo = Path(__file__).resolve().parent.parent
    if out == repo or repo in out.parents:
        p.error('Reference media must remain outside Git')
    out.mkdir(parents=True, exist_ok=True)
    target = out / (a.id + '.tga')
    if target.exists() or (out / (a.id + '.json')).exists():
        raise FileExistsError('Use a new ID; existing evidence must not be overwritten')
    if a.pose:
        x, y, z, pitch, yaw = a.pose
        exchange(f'setpos_exact {x} {y} {z}; setang_exact {pitch} {yaw} 0', seconds=3)
    pose_reply = exchange('getpos_exact', seconds=3)['received_prints']
    pose = [line.strip() for line in pose_reply if line.startswith('setpos_exact ')]
    if len(pose) != 1:
        raise RuntimeError('No unique live pose; capture aborted')
    # Keep engine-facing resource names lowercase; metadata IDs may be uppercase.
    response = exchange('screenshot ' + a.id.lower(), seconds=3)['received_prints']
    names = [re.search(r'Screenshot written to: (.+)', line) for line in response]
    names = [m.group(1).strip() for m in names if m]
    if len(names) != 1:
        raise RuntimeError('No unique screenshot result; inspect game before retrying')
    addon = a.addon.resolve()
    src = (addon / names[0]).resolve()
    if addon not in src.parents or src.suffix.lower() != '.tga':
        raise ValueError('Screenshot returned an unexpected path')
    shutil.copyfile(src, target)
    png = out / (a.id + '.png')
    width, height = preview_tga(target, png)
    result = dict(id=a.id, timestamp_utc=datetime.now(timezone.utc).isoformat(),
                  pose_command=pose[0], pose_unit='source_units', width=width,
                  height=height, requested_pose=a.pose,
                  tga_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                  png_sha256=hashlib.sha256(png.read_bytes()).hexdigest(),
                  status='captured; requires visual area/direction review')
    (out / (a.id + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
