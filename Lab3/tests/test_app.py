import json
import threading
import time
import urllib.request
from app import create_server

def test_health_endpoint_returns_ok():
    server = create_server(8765)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        time.sleep(0.2)
        with urllib.request.urlopen("http://127.0.0.1:8765/health", timeout=3) as response:
            body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["status"] == "ok"
    finally:
        server.shutdown()
        thread.join(timeout=2)
