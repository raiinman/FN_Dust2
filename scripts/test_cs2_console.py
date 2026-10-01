"""Transport regression: py -3.11 -m unittest discover -s scripts -p 'test_cs2_console.py'."""
import socket
import threading
import unittest
from cs2_console import HEADER, ConsoleSession, exchange


class WireRegression(unittest.TestCase):
    def test_two_commands_share_connection_and_partial_frame(self):
        errors = []
        with socket.socket() as listener:
            listener.bind(('127.0.0.1', 0))
            listener.listen(1)
            port = listener.getsockname()[1]
            def packet(line):
                body = b'\0' * 28 + line.encode() + b'\0'
                return HEADER.pack(b'PRNT', 0xD4, len(body) + 12, 0) + body
            def server():
                try:
                    with listener.accept()[0] as peer:
                        peer.settimeout(3)
                        self.assertIn(b'echo FIRST', peer.recv(1024))
                        # Incomplete next header survives the first exchange.
                        second = packet('SECOND\n')
                        peer.sendall(packet('FIRST\n') + second[:7])
                        self.assertIn(b'echo SECOND', peer.recv(1024))
                        peer.sendall(second[7:])
                        peer.recv(1024)  # EOF only when the session ends.
                except Exception as error:
                    errors.append(error)
            worker = threading.Thread(target=server)
            worker.start()
            session = ConsoleSession(port)
            try:
                self.assertTrue(session.exchange('echo FIRST', .3)['response_verified'])
                self.assertFalse(session.closed)
                self.assertTrue(session.exchange('echo SECOND', .3)['response_verified'])
            finally:
                session.close()
            worker.join(3)
        self.assertFalse(worker.is_alive())
        self.assertEqual(errors, [])

    def test_large_packet_fragmentation_replay_and_echo(self):
        def packet(kind, body, version=0xD4):
            return HEADER.pack(kind, version, len(body) + 12, 0) + body

        def prnt(line):
            return packet(b'PRNT', b'\0' * 28 + line.encode() + b'\0')

        errors = []
        with socket.socket() as listener:
            listener.bind(('127.0.0.1', 0))
            listener.listen(1)
            port = listener.getsockname()[1]

            def server():
                try:
                    with listener.accept()[0] as peer:
                        peer.settimeout(2)
                        peer.recv(1024)
                        data = (prnt('VConsole Buffered Messages')
                                + prnt('OLD_PRIVATE_REPLAY')
                                + packet(b'CVRB', b'x' * 746052, 2)
                                + prnt('End VConsole Buffered Messages')
                                + prnt('WIRE_REGRESSION\n'))
                        # Splits headers and bodies across arbitrary TCP writes.
                        for i in range(0, len(data), 997):
                            peer.sendall(data[i:i + 997])
                except Exception as error:
                    errors.append(error)

            worker = threading.Thread(target=server)
            worker.start()
            result = exchange('echo WIRE_REGRESSION', port, 2)
            worker.join(3)
        self.assertFalse(worker.is_alive())
        self.assertEqual(errors, [])
        self.assertTrue(result['response_verified'])
        self.assertEqual(result['received_prints'], ['WIRE_REGRESSION\n'])


if __name__ == '__main__':
    unittest.main()
