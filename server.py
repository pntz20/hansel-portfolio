import json
import os
from datetime import datetime, timezone
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SUBMISSIONS_FILE = os.path.join(REPO_DIR, "submissions.json")


class FormHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != "/submit":
            self.send_error(404, "Not found")
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return

        entry = {
            "received_at": datetime.now(timezone.utc).isoformat(),
            "name": data.get("name", ""),
            "email": data.get("email", ""),
            "subject": data.get("subject", ""),
            "message": data.get("message", ""),
            "source": data.get("source", "portfolio"),
        }

        submissions = []
        if os.path.exists(SUBMISSIONS_FILE):
            try:
                with open(SUBMISSIONS_FILE, "r", encoding="utf-8") as f:
                    submissions = json.load(f)
            except json.JSONDecodeError:
                submissions = []

        submissions.append(entry)

        with open(SUBMISSIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(submissions, f, indent=2, ensure_ascii=False)

        response = json.dumps({"ok": True, "saved": True})
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response.encode("utf-8"))))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def run(port=8000):
    os.chdir(REPO_DIR)
    server = HTTPServer(("0.0.0.0", port), FormHandler)
    print(f"Serving {REPO_DIR}")
    print(f"Form endpoint: http://localhost:{port}/submit")
    print(f"Submissions file: {SUBMISSIONS_FILE}")
    print("Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
