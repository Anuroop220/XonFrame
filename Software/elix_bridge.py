"""
elix_bridge.py — runs on your LAPTOP as a separate process from main.py.

This is what the XonFrame Console's Settings -> Connection -> "Phone E.L.I.X
Bridge URL" field points at. It exposes /chat over HTTP so the browser-based
console can talk to E.L.I.X, using the same ask_elix() brain as main.py.

Run alongside main.py:
    python elix_bridge.py
Then set the console's bridge URL to http://<this-laptop-ip>:5001
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from elix import ask_elix

app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "no 'message' field in request"}), 400
    reply = ask_elix(message)
    return jsonify({"reply": reply})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "elix-bridge"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
