"""
config.py — shared settings for the XonFrame laptop-side pipeline.
Edit these to match your setup, then every other file reads from here.
"""

# ── Glasses connection ──
GLASSES_IP = "192.168.1.42"          # ESP32-S3FH4R2 IP on your WiFi
GLASSES_WS_PORT = 81                  # matches console's ws://<ip>:81/ws
GLASSES_WS_URL = f"ws://{GLASSES_IP}:{GLASSES_WS_PORT}/ws"

# ── Vision ──
YOLO_MODEL_PATH = "yolo11n.pt"
YOLO_CONFIDENCE = 0.45

# ── Voice ──
TTS_VOICE_RATE = 175                  # words per minute, for pyttsx3

# ── Wake word ──
WAKE_WORD = "elix"

# ── Navigation ──
ORS_API_KEY = ""                      # OpenRouteService key — set in .env instead, see navigation.py

# ── Notifications ──
PUSHBULLET_API_KEY = ""               # set in .env instead, see notifications.py

# ── E.L.I.X bridge (Gemini) ──
BRIDGE_HOST = "0.0.0.0"
BRIDGE_PORT = 5001
GEMINI_MODEL = "gemini-2.0-flash"
