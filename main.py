import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = int(os.environ.get("PORT", "8000"))

PORTFOLIO = {
    "creator": {
        "name": "Christopher Francis P. De Vera",
        "github_url": "https://github.com/ICT-De-Vera",
    },
    "projects": [
        {
            "name": "Q2 Seatwork 1",
            "category": "ICT 10 · Seatwork",
            "description": "A live web project made for my ICT 10 Q2 seatwork.",
            "live_url": "https://ict-de-vera.github.io/Fairview_ICT10_Q2Seatwork1_De_Vera_Christopher_Francis_P./",
            "source_url": "https://github.com/ICT-De-Vera/Fairview_ICT10_Q2Seatwork1_De_Vera_Christopher_Francis_P..git",
        },
        {
            "name": "Q2 Skills Test",
            "category": "ICT 10 · Skills test",
            "description": "A live web project made for my ICT 10 Q2 skills test.",
            "live_url": "https://ict-de-vera.github.io/Fairview_ICT10_Q2SkillsTest_De_Vera_Christopher_Francis_P./",
            "source_url": "https://github.com/ICT-De-Vera/Fairview_ICT10_Q2SkillsTest_De_Vera_Christopher_Francis_P..git",
        },
        {
            "name": "Q2 Drill 2",
            "category": "ICT 10 · Drill",
            "description": "A live web project made for my ICT 10 Q2 Drill 2.",
            "live_url": "https://ict-de-vera.github.io/FV_ICT10S_Q2Drill2_De_Vera_Christopher_Francis_P./",
            "source_url": "https://github.com/ICT-De-Vera/FV_ICT10S_Q2Drill2_De_Vera_Christopher_Francis_P..git",
        },
    ],
}


class PortfolioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if urlsplit(self.path).path == "/api/portfolio":
            payload = json.dumps(PORTFOLIO).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(payload)
            return

        super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), PortfolioHandler)
    print(f"Portfolio running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping portfolio server.")
    finally:
        server.server_close()