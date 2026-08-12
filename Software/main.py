"""
main.py — XonFrame orchestrator.

Architecture change from your original: the camera feed now comes from the
ESP32-S3FH4R2 glasses over the same WebSocket protocol the console uses
(ws://<glasses-ip>:81/ws — binary = JPEG frame, text = JSON telemetry),
instead of a local cv2.VideoCapture(0) webcam. This means main.py and the
XonFrame Console can both be connected to the glasses at the same time.

Set GLASSES_IP in config.py before running.
"""

import io
import json
import time
import threading

import cv2
import numpy as np
import pygame
import websocket  # pip install websocket-client

from config import GLASSES_WS_URL
from motion import detect_motion
from vision import detect_objects
from voice import listen, speak
from elix import ask_elix
from wakeword import start_wake_word
from notifications import start_notifications
from navigation import parse_nav_command, get_directions
import hud

# ---------------- SHARED STATE ----------------
state = {
    "battery_percent": 0,
    "connected": False,
    "detections": [],
    "elix_active": False,
    "notification": "Connecting to glasses...",
    "nav_active": False,
    "nav_steps": [],
    "nav_current": 0,
}

latest_frame = None            # decoded BGR numpy frame, updated by the WS thread
_frame_lock = threading.Lock()


# ---------------- GLASSES WEBSOCKET CLIENT ----------------
def on_ws_message(ws, message):
    global latest_frame
    if isinstance(message, bytes):
        # Binary = JPEG camera frame
        arr = np.frombuffer(message, dtype=np.uint8)
        frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        if frame is not None:
            with _frame_lock:
                latest_frame = frame
    else:
        # Text = JSON telemetry
        try:
            data = json.loads(message)
        except json.JSONDecodeError:
            return
        if "battery" in data:
            state["battery_percent"] = data["battery"]
        state["connected"] = True


def on_ws_error(ws, error):
    print(f"Glasses WebSocket error: {error}")
    state["connected"] = False


def on_ws_close(ws, *_):
    print("Glasses WebSocket closed — retrying in 3s")
    state["connected"] = False
    time.sleep(3)
    start_glasses_ws()


def on_ws_open(ws):
    print(f"Connected to glasses at {GLASSES_WS_URL}")
    state["connected"] = True
    state["notification"] = "Glasses connected"


def start_glasses_ws():
    ws = websocket.WebSocketApp(
        GLASSES_WS_URL,
        on_open=on_ws_open,
        on_message=on_ws_message,
        on_error=on_ws_error,
        on_close=on_ws_close,
    )
    t = threading.Thread(target=ws.run_forever, daemon=True)
    t.start()


# ---------------- WAKE WORD CALLBACK ----------------
def on_wake_word():
    state["elix_active"] = True
    state["notification"] = "E.L.I.X listening..."
    speak("Yes?")
    user_input = listen()

    if user_input:
        destination = parse_nav_command(user_input)

        if destination:
            speak(f"Getting directions to {destination}")
            state["notification"] = f"Navigating to {destination}..."
            directions, summary = get_directions(destination)

            if directions:
                speak(summary)
                state["notification"] = summary
                state["nav_active"] = True
                state["nav_steps"] = directions
                state["nav_current"] = 0
                first = directions[0]
                speak(f"First, {first['instruction']} in {first['distance']} meters")
            else:
                speak(summary)
                state["notification"] = summary
        else:
            state["notification"] = f"You: {user_input[:40]}"
            response = ask_elix(user_input, state["detections"])
            speak(response)
            state["notification"] = f"ELIX: {response[:40]}"

    state["elix_active"] = False


# ---------------- VISION PIPELINE THREAD ----------------
def vision_pipeline():
    """Runs motion detection + (throttled) YOLO on frames pulled from the
    glasses' WebSocket stream, rather than a local webcam."""
    prev_frame = None
    last_yolo_time = 0
    YOLO_COOLDOWN = 3

    while True:
        with _frame_lock:
            frame = latest_frame.copy() if latest_frame is not None else None

        if frame is None:
            time.sleep(0.05)
            continue

        if prev_frame is not None and prev_frame.shape == frame.shape:
            if detect_motion(prev_frame, frame):
                now = time.time()
                if now - last_yolo_time > YOLO_COOLDOWN:
                    state["detections"] = detect_objects(frame)
                    last_yolo_time = now

        prev_frame = frame
        time.sleep(0.03)


# ---------------- RUN ----------------
def main():
    pygame.init()
    screen, clock = hud.init_hud()
    start_time = time.time()

    start_glasses_ws()
    start_wake_word(on_wake_word)
    start_notifications(state)
    threading.Thread(target=vision_pipeline, daemon=True).start()

    running = True
    print("XonFrame LIVE system running")
    print(f"Connecting to glasses at {GLASSES_WS_URL}")
    print("Say 'Hey E.L.I.X' to activate")

    while running:
        t = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        hud.draw_hud(screen, clock, t, state)
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
