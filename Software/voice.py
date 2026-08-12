import speech_recognition as sr
import pyttsx3

# NOTE: this uses whichever microphone your OS reports as default (sr.Microphone()).
# The glasses' INMP441 mic is NOT streamed over the WebSocket in the current
# firmware/console protocol (only camera frames + JSON telemetry are).
# Until audio streaming is added to xonframe.ino, this picks up your
# laptop's built-in/USB mic, not the glasses' mic.

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 165)


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except Exception:
            return ""


def speak(text):
    print(f"E.L.I.X: {text}")
    engine.say(text)
    engine.runAndWait()
