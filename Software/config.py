"""
configuration settings\
API keys will be taken from .env file
Do not put real API keys in this file bcs it should be put in the .env file
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# this is for Loading .env file from the software folder
env_file = Path(__file__).resolve().parent / ".env"
load_dotenv(env_file)


# Paste the esp32 ip address down here
esp32_ip = os.getenv("esp32_ip", "put esp32 ip address printed in terminal/sl monitor here")
esp32_ws_port = int(os.getenv("esp32_ws_port", "81"))
# don't put the ip address down it will automatically take the ip address from above code 
esp_ws_url = f"ws://{esp32_ip}:{esp32_ws_port}/ws"


path_of_yolo_model = os.getenv("path_of_yolo_model", "yolo11n.pt")
yolo_confidence = float(os.getenv("yolo_confidence", "0.45"))


tts_voice_rate = int(os.getenv("tts_voice_rate", "175"))


elix_wakeword = ["elix", "alex", "helix", "felix", "lix"]


# API will be automatically taken from the env file with the down code
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
ORS_API_KEY = os.getenv("ORS_API_KEY", "")
PUSHBULLET_API_KEY = os.getenv("PUSHBULLET_API_KEY", "")


bridge_host = os.getenv("bridge_host", "0.0.0.0")
bridge_port = int(os.getenv("bridge_port", "5001"))
gemini_model = os.getenv("gemini_model", "gemini-3.6-flash")