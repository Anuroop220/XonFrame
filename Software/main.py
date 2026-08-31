""" This is the main program for connecting XonFrame to elix """
import json
import threading
import time
import cv2
import numpy as np
import pygame
import websocket

from config import esp_ws_url
from motion import detect_motion
from vision import detect_objects
from voice import listen, speak
from elix import ask_elix
from wakeword import start_wake_word
from notifications import start_notifications
from navigation import parse_nav_command, get_directions
import hud


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

latest_frame = None
frame_lock = threading.Lock()


def receive_message(ws, message):
    """Save camera frames and read battery information."""
    global latest_frame

    if isinstance(message, bytes):
        image_data = np.frombuffer(message, dtype=np.uint8)
        frame = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

        if frame is not None:
            with frame_lock:
                latest_frame = frame
        return

    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        return

    if "battery" in data:
        state["battery_percent"] = data["battery"]

    state["connected"] = True


def websocket_error(ws, error):
    print(f"WebSocket error: {error}")
    state["connected"] = False


def websocket_closed(ws, *args):
    print("Connection closed. Trying again in 3 seconds.")
    state["connected"] = False
    time.sleep(3)
    connect_to_glasses()


def websocket_opened(ws):
    print(f"Connected to glasses at {esp_ws_url}")
    state["connected"] = True
    state["notification"] = "Glasses connected"


def connect_to_glasses():
    """Start the WebSocket connection in the background."""
    connection = websocket.WebSocketApp(
        esp_ws_url,
        on_open=websocket_opened,
        on_message=receive_message,
        on_error=websocket_error,
        on_close=websocket_closed,
    )

    thread = threading.Thread(
        target=connection.run_forever,
        daemon=True,
    )
    thread.start()


def handle_wake_word():
    """Listen for a question after the wake word is detected."""
    state["elix_active"] = True
    state["notification"] = "E.L.I.X listening..."
    speak("Yes?")

    user_input = listen()

    if user_input:
        destination = parse_nav_command(user_input)

        if destination:
            handle_navigation(destination)
        else:
            state["notification"] = f"You: {user_input[:40]}"
            answer = ask_elix(user_input, state["detections"])
            speak(answer)
            state["notification"] = f"ELIX: {answer[:40]}"

    state["elix_active"] = False


def handle_navigation(destination):
    speak(f"Getting directions to {destination}")
    state["notification"] = f"Navigating to {destination}..."

    directions, summary = get_directions(destination)

    if not directions:
        speak(summary)
        state["notification"] = summary
        return

    speak(summary)
    state["notification"] = summary
    state["nav_active"] = True
    state["nav_steps"] = directions
    state["nav_current"] = 0

    first_step = directions[0]
    speak(
        f"First, {first_step['instruction']} "
        f"in {first_step['distance']} meters"
    )


def run_vision():
    """Check new frames for movement and objects."""
    previous_frame = None
    last_detection_time = 0
    detection_delay = 3

    while True:
        with frame_lock:
            frame = (
                latest_frame.copy()
                if latest_frame is not None
                else None
            )

        if frame is None:
            time.sleep(0.05)
            continue

        if (
            previous_frame is not None
            and previous_frame.shape == frame.shape
            and detect_motion(previous_frame, frame)
        ):
            current_time = time.time()

            if current_time - last_detection_time > detection_delay:
                state["detections"] = detect_objects(frame)
                last_detection_time = current_time

        previous_frame = frame
        time.sleep(0.03)


def main():
    pygame.init()
    screen, clock = hud.init_hud()
    start_time = time.time()

    connect_to_glasses()
    start_wake_word(handle_wake_word)
    start_notifications(state)

    vision_thread = threading.Thread(target=run_vision, daemon=True)
    vision_thread.start()

    print("XonFrame is running.")
    print(f"Glasses address: {esp_ws_url}")
    print("Say 'Hey E.L.I.X' to begin.")

    running = True

    while running:
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        hud.draw_hud(screen, clock, elapsed_time, state)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    

if __name__ == "__main__":
    main()
