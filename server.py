import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def _h(self):
        out = {
            "headers": {k: v for k, v in self.headers.items()},
            "openhost_env": {k: v for k, v in os.environ.items() if k.startswith("OPENHOST")},
        }
        body = json.dumps(out, indent=2).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    do_GET = _h
    do_POST = _h
    def log_message(self, *a): pass
HTTPServer(("0.0.0.0", 8080), H).serve_forever()
