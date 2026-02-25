#!/usr/bin/env python3
"""
Custom HTTP server for the Gmail Organize & Manage app.

Serves static files and exposes API endpoints:
  GET  /api/state  — Read the current application state (for verifiers)
  PUT  /api/state  — Update the server-side state copy (called by browser)
  POST /api/reset  — Reset the app state to seed data

Usage:
    python3 server.py [--port PORT]

Example (Python verifier):
    import requests
    state = requests.get('http://localhost:8000/api/state').json()
    assert state['settings']['theme'] == 'default'
"""

import http.server
import json
import queue
import socketserver
import sys
import threading


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


# SSE client queues — each connected browser tab gets one
_clients = []
_clients_lock = threading.Lock()

# Server-side copy of application state (pushed by browser on every mutation)
_app_state = None
_seed_state = None  # Snapshot of the first state push (seed data)
_state_lock = threading.Lock()


class AppHandler(http.server.SimpleHTTPRequestHandler):

    def do_PUT(self):
        if self.path == '/api/state':
            self._handle_put_state()
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/api/reset':
            self._handle_reset()
        else:
            self.send_error(404)

    def do_GET(self):
        if self.path == '/api/state':
            self._handle_get_state()
        elif self.path == '/api/events':
            self._handle_sse()
        else:
            super().do_GET()

    # ---- State sync ----

    def _handle_put_state(self):
        """Browser pushes its AppState here on every mutation."""
        global _app_state, _seed_state
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        try:
            parsed = json.loads(body)
            with _state_lock:
                _app_state = parsed
                # Capture the first push as seed state snapshot
                if _seed_state is None:
                    _seed_state = json.loads(json.dumps(parsed))  # deep copy
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
        except json.JSONDecodeError:
            self.send_error(400, 'Invalid JSON')

    def _handle_get_state(self):
        """Verifiers read the current application state from here."""
        with _state_lock:
            state = _app_state
        if state is None:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"error":"No state available. Open the app in a browser first."}')
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(state).encode())

    # ---- Reset ----

    def _handle_reset(self):
        """Reset server state to seed data and notify connected browsers."""
        global _app_state
        with _state_lock:
            if _seed_state is not None:
                _app_state = json.loads(json.dumps(_seed_state))  # deep copy
            else:
                _app_state = None
        with _clients_lock:
            for q in _clients:
                q.put('reset')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            'status': 'ok',
            'action': 'reset',
            'seed_restored': _seed_state is not None,
            'clients_notified': len(_clients)
        }).encode())

    # ---- SSE ----

    def _handle_sse(self):
        """Server-Sent Events stream for pushing commands to the browser."""
        self.send_response(200)
        self.send_header('Content-Type', 'text/event-stream')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Connection', 'keep-alive')
        self.end_headers()

        q = queue.Queue()
        with _clients_lock:
            _clients.append(q)

        try:
            self.wfile.write(b'data: connected\n\n')
            self.wfile.flush()

            while True:
                event = q.get()  # blocks until a signal arrives
                self.wfile.write(f'data: {event}\n\n'.encode())
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError, OSError):
            pass
        finally:
            with _clients_lock:
                if q in _clients:
                    _clients.remove(q)

    def log_message(self, format, *args):
        if args and '/api/' in str(args[0]):
            super().log_message(format, *args)


if __name__ == '__main__':
    port = 8000
    if '--port' in sys.argv:
        idx = sys.argv.index('--port')
        port = int(sys.argv[idx + 1])

    if '--test-mode' in sys.argv:
        import os as _os
        _app = _os.path.dirname(_os.path.abspath(__file__))
        _repo = _os.path.dirname(_os.path.dirname(_app))
        sys.path.insert(0, _os.path.join(_repo, 'evaluation'))
        from test_mode import patch_handler_for_test_mode
        patch_handler_for_test_mode(AppHandler, _app)

    server = ThreadedHTTPServer(('', port), AppHandler)
    print(f'Serving on http://localhost:{port}')
    print(f'  API:  GET  http://localhost:{port}/api/state')
    print(f'  API:  POST http://localhost:{port}/api/reset')
    print(f'  SSE:  GET  http://localhost:{port}/api/events')
    print()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down.')
        server.shutdown()
