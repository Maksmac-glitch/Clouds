from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

APP_NAME = os.getenv("APP_NAME", "Clouds CI/CD Demo")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, payload: dict):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok", "service": APP_NAME})
            return
        self._send(200, {
            "message": "CI/CD pipeline demo application",
            "service": APP_NAME,
            "version": APP_VERSION,
        })

def create_server(port: int = 8000):
    return HTTPServer(("0.0.0.0", port), Handler)

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "8000"))
    server = create_server(port)
    print(f"{APP_NAME} started on port {port}")
    server.serve_forever()
