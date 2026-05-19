from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket

PORT = int(os.environ.get("APP_PORT", "8000"))
APP_NAME = os.environ.get("APP_NAME", "Clouds service")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"{APP_NAME} is running on {socket.gethostname()}\n".encode("utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = f"""<!doctype html>
<html lang=\"ru\">
<head><meta charset=\"UTF-8\"><title>{APP_NAME}</title></head>
<body>
<h1>{APP_NAME}</h1>
<p>Контейнер запущен успешно.</p>
<p>Hostname: {socket.gethostname()}</p>
</body>
</html>"""
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        print("%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), format % args))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Starting {APP_NAME} on port {PORT}")
    server.serve_forever()
