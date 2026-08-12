import speech_recognition as sr
import threading

# Same caveat as voice.py: listens on the laptop's default mic, not the
# glasses' INMP441, until firmware audio streaming is added.

recognizer = sr.Recognizer()
WAKE_WORDS = ["elix", "alex", "helix", "felix", "lix"]


def listen_for_wake_word(callback):
    print("Wake word detection active - say 'Hey E.L.I.X'")
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
            try:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                text = recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")
                if any(word in text for word in WAKE_WORDS):
                    print("Wake word detected!")
                    callback()
            except Exception:
                pass


def start_wake_word(callback):
    t = threading.Thread(target=listen_for_wake_word, args=(callback,), daemon=True)
    t.start()
