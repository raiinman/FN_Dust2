"""Loopback-only CS2 VConsole transport, standard library only.

Start once: py -3.11 scripts/cs2_console.py --serve OUTSIDE_REPO_QUEUE
Request: py -3.11 scripts/cs2_console.py "echo FN_DUST2_PROBE" --session OUTSIDE_REPO_QUEUE
Keep worker running until the game exits; do not close/reopen it per command.
CS2 must already be running with -tools -vconsole. Never launches a game, injects into
processes, or reads game packages. Protocol: https://github.com/oxijoined/vconsole-python
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import socket
import struct
import time
import uuid

HEADER = struct.Struct('>4sHIH')
# Current-build wire observations: uint16 version, uint32 total length, uint16
# handle. Legacy uint16 length readers lose alignment on large CVRB packets.
MAX_PACKET_BYTES = 4 * 1024 * 1024

def command_packet(command: str) -> bytes:
    if any(c in command for c in '\x00\n\r'):
        raise ValueError('Use one command line without NUL or newline characters')
    body = command.encode('utf-8') + b'\0'
    if len(body) + HEADER.size > 65535:
        raise ValueError('Command exceeds protocol packet limit')
    return HEADER.pack(b'CMND', 0x00D4, len(body) + HEADER.size, 0) + body

class ConsoleSession:
    """One connection per game session; retain partial frames between commands."""
    def __init__(self, port=29000):
        self.port = port
        self.conn = socket.create_connection(('127.0.0.1', port), timeout=2)
        self.conn.settimeout(0.15)
        self.pending = b''
        self.replaying = False
        self.closed = False

    def close(self):
        self.conn.close()
        self.closed = True

    def receive(self):
        records = []
        try:
            chunk = self.conn.recv(65536)
        except socket.timeout:
            return records
        if not chunk:
            self.closed = True
            return records
        self.pending += chunk
        while len(self.pending) >= HEADER.size:
            kind, version, length, handle = HEADER.unpack_from(self.pending)
            if length < HEADER.size or length > MAX_PACKET_BYTES:
                raise ValueError('Invalid VConsole packet length')
            if len(self.pending) < length:
                break
            body, self.pending = self.pending[HEADER.size:length], self.pending[length:]
            if kind == b'PRNT':
                line = body[28:].split(b'\0', 1)[0].decode('utf-8', errors='replace')
                if 'End VConsole Buffered Messages' in line:
                    self.replaying = False
                    records.clear()
                elif 'VConsole Buffered Messages' in line:
                    self.replaying = True
                    records.clear()
                elif not self.replaying:
                    records.append(line)
        return records

    def exchange(self, command, seconds=1.5):
        if self.closed:
            raise ConnectionError('Game connection ended; do not reconnect blindly')
        records = []
        self.conn.sendall(command_packet(command))
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline and not self.closed:
            records.extend(self.receive())
        return result(command, self.port, records)


def result(command, port, records):
    return {'transport': '127.0.0.1:' + str(port), 'command': command,
            'received_prints': records, 'response_received': bool(records),
            'response_verified': command.startswith('echo ') and any(
                line.strip() == command[5:].strip() for line in records),
            'note': 'A sent packet does not establish that the command succeeded.'}


def exchange(command: str, port: int = 29000, seconds: float = 1.5) -> dict:
    """One-shot transport for synthetic tests; use persistent worker in CS2."""
    session = ConsoleSession(port)
    try:
        return session.exchange(command, seconds)
    finally:
        session.close()


def local_directory(path):
    path = Path(path).resolve()
    repo = Path(__file__).resolve().parent.parent
    if path == repo or repo in path.parents:
        raise ValueError('Private console queue must remain outside Git')
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_json(path, value):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)


def serve(path, port=29000):
    """Drain idle traffic, serialize requests, never automatically reconnect."""
    path = local_directory(path)
    # Exclusive lock prevents two workers opening competing game sockets.
    with (path / 'worker.lock').open('x'):
        pass
    session = None
    try:
        session = ConsoleSession(port)
        write_json(path / 'status.json', {'state': 'connected'})
        while not session.closed:
            requests = sorted(path.glob('*.request.json'))
            if not requests:
                session.receive()  # Discard idle output; retain framing state.
                continue
            for request in requests:
                data = json.loads(request.read_text(encoding='utf-8'))
                seconds = float(data.get('seconds', 1.5))
                if not 0 < seconds <= 30:
                    raise ValueError('Request duration must be 0 < seconds <= 30')
                reply = session.exchange(data['command'], seconds)
                write_json(request.with_name(request.name.replace('.request.', '.response.')), reply)
                request.unlink()
                if session.closed:
                    break
        write_json(path / 'status.json', {'state': 'game_disconnected'})
    except Exception as error:
        write_json(path / 'status.json', {'state': 'failed', 'error': str(error)})
        raise
    finally:
        if session:
            session.close()
        (path / 'worker.lock').unlink(missing_ok=True)


def request_exchange(path, command, seconds=1.5):
    command_packet(command)  # Validate before creating a request.
    path = local_directory(path)
    state = json.loads((path / 'status.json').read_text())
    if state.get('state') != 'connected' or not (path / 'worker.lock').exists():
        raise ConnectionError('Persistent worker is not connected')
    token = uuid.uuid4().hex
    request = path / (token + '.request.json')
    response = path / (token + '.response.json')
    write_json(request, {'command': command, 'seconds': seconds})
    deadline = time.monotonic() + seconds + 5
    while time.monotonic() < deadline:
        if response.exists():
            return json.loads(response.read_text(encoding='utf-8'))
        time.sleep(0.1)
    raise TimeoutError('No worker reply; inspect game and queue before continuing')

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--serve', type=Path)
    mode.add_argument('--session', type=Path)
    parser.add_argument('--port', type=int, default=29000)
    parser.add_argument('--seconds', type=float, default=1.5)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.serve:
        serve(args.serve, args.port)
        return 0
    if not args.command:
        parser.error('A command is required with --session')
    try:
        result = request_exchange(args.session, args.command, args.seconds)
    except (OSError, ValueError) as error:
        result = {'command': args.command, 'response_verified': False, 'error': str(error)}
    rendered = json.dumps(result, indent=2, ensure_ascii=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + '\n', encoding='utf-8')
    print(rendered)
    return 0 if result.get('response_received') else 2

if __name__ == '__main__':
    raise SystemExit(main())
