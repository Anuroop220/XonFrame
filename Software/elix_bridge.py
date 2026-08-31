"""
This file starts like a separate server for the xosoftware to talk with elix
keep this program running while using the xosoftware

start it in another terminal by typing - python elix_bridge.py

use this bridge URL in the xosoftware settings tab
    http://<paste_laptop_ip_here>:5001 (like this http://111.111.1.11:5001) 

    if it is running in the same computer where the xosofware is running 
    use this ip  http://localhost:5001
     it will be already there so no need to change
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
        return jsonify({"error": "no 'message' field in this request"}), 400
    reply = ask_elix(message)
    return jsonify({"reply": reply})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "elix-bridge"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
