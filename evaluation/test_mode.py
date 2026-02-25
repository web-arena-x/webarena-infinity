"""
In-browser test panel support.

Call ``patch_handler_for_test_mode(handler_class, app_dir)`` to add:
  GET  /api/tasks      — serves tasks.json
  POST /api/verify     — runs a verifier, returns {task_id, passed, message}
  GET  /test_panel.js  — serves the test-panel UI script
  GET  / | /index.html — injects the panel <script> tag before </body>
"""

import importlib.util
import json
import os
from pathlib import Path


_PANEL_JS_PATH = os.path.join(os.path.dirname(__file__), "test_panel.js")


def patch_handler_for_test_mode(handler_class, app_dir):
    """Monkey-patch *handler_class* to serve the test panel and verifier API."""

    app_dir = str(Path(app_dir).resolve())
    tasks_json_path = os.path.join(app_dir, "tasks.json")

    # Cache tasks.json contents
    with open(tasks_json_path) as f:
        tasks_payload = f.read().encode()

    # Cache panel JS contents
    with open(_PANEL_JS_PATH) as f:
        panel_js_payload = f.read().encode()

    # Read index.html and inject script tag
    index_path = os.path.join(app_dir, "index.html")
    with open(index_path) as f:
        original_html = f.read()
    injected_html = original_html.replace(
        "</body>", '<script src="/test_panel.js"></script></body>'
    )
    injected_html_bytes = injected_html.encode()

    _orig_do_GET = handler_class.do_GET
    _orig_do_POST = handler_class.do_POST

    def _server_url(self):
        host = self.headers.get("Host", f"localhost:{self.server.server_address[1]}")
        return f"http://{host}"

    def patched_do_GET(self):
        if self.path == "/api/tasks":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(tasks_payload)))
            self.end_headers()
            self.wfile.write(tasks_payload)
        elif self.path == "/test_panel.js":
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.send_header("Content-Length", str(len(panel_js_payload)))
            self.end_headers()
            self.wfile.write(panel_js_payload)
        elif self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(injected_html_bytes)))
            self.end_headers()
            self.wfile.write(injected_html_bytes)
        else:
            _orig_do_GET(self)

    def patched_do_POST(self):
        if self.path == "/api/verify":
            content_length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(content_length))
            task_id = body.get("task_id", "")

            # Find the task's verify script
            with open(tasks_json_path) as f:
                tasks = json.load(f)
            task = next((t for t in tasks if t["id"] == task_id), None)
            if not task:
                self._send_json(400, {"error": f"Unknown task: {task_id}"})
                return

            verify_path = os.path.join(app_dir, task["verify"])
            try:
                spec = importlib.util.spec_from_file_location("verifier", verify_path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                passed, message = mod.verify(_server_url(self))
            except Exception as e:
                passed, message = False, f"Verifier error: {e}"

            self._send_json(200, {
                "task_id": task_id,
                "passed": passed,
                "message": message,
            })
        else:
            _orig_do_POST(self)

    def _send_json(self, code, obj):
        payload = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    handler_class.do_GET = patched_do_GET
    handler_class.do_POST = patched_do_POST
    handler_class._send_json = _send_json
