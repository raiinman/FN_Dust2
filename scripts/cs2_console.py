"""Loopback-only CS2 VConsole transport, standard library only.

Usage: py -3.11 scripts/cs2_console.py "echo FN_DUST2_PROBE" --output PATH
CS2 must already be running with -vconsole. Never launches a game, injects into
processes, or reads game packages. Protocol: https://github.com/oxijoined/vconsole-python
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import socket
import struct
import time

HEADER = struct.Struct('>4sIHH')

def command_packet(command: str) -> bytes:
    if any(c in command for c in '\x00\n\r'):
        raise ValueError('Use one command line without NUL or newline characters')
    body = command.encode('utf-8') + b'\0'
    if len(body) + HEADER.size > 65535:
        raise ValueError('Command exceeds protocol packet limit')
    return HEADER.pack(b'CMND', 0x00D40000, len(body) + HEADER.size, 0) + body

def exchange(command: str, port: int = 29000, seconds: float = 1.5) -> dict:
    records = []
    pending = b''
    with socket.create_connection(('127.0.0.1', port), timeout=2) as conn:
        conn.settimeout(0.15)
        conn.sendall(command_packet(command))
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            try:
                chunk = conn.recv(65536)
            except socket.timeout:
                continue
            if not chunk:
                break
            pending += chunk
            while len(pending) >= HEADER.size:
                kind, version, length, handle = HEADER.unpack_from(pending)
                if length < HEADER.size:
                    raise ValueError('Invalid VConsole packet length')
                if len(pending) < length:
                    break
                body, pending = pending[HEADER.size:length], pending[length:]
                if kind == b'PRNT':
                    records.append(body[28:].split(b'\0', 1)[0].decode('utf-8', errors='replace'))
    return {'transport': '127.0.0.1:' + str(port), 'command': command,
            'received_prints': records, 'response_verified': bool(records),
            'note': 'A sent packet does not establish that the command succeeded.'}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command')
    parser.add_argument('--port', type=int, default=29000)
    parser.add_argument('--seconds', type=float, default=1.5)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        result = exchange(args.command, args.port, args.seconds)
    except (OSError, ValueError) as error:
        result = {'command': args.command, 'response_verified': False, 'error': str(error)}
    rendered = json.dumps(result, indent=2, ensure_ascii=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + '\n', encoding='utf-8')
    print(rendered)
    return 0 if result.get('response_verified') else 2

if __name__ == '__main__':
    raise SystemExit(main())
