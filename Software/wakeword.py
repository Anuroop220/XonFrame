import speech_recognition as sr
import threading

recognizer = sr.Recognizer()
elix_wakeword = ["elix", "alex", "helix", "felix", "lix"]


def listen_for_wake_word(callback):
    """it listens continuously for wake words."""
    print("Wake word detection active say 'Hey ELIX'")

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.3)

            try:
                audio = recognizer.listen(
                    source, timeout=3, phrase_time_limit=3
                )
                text = recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")

                if any(word in text for word in elix_wakeword):
                    print("wake word detected")
                    callback()

            except sr.UnknownValueError:
                pass

            except sr.RequestError:
                print("No internet for wake word detection")
                break

            except Exception:
                pass


def start_wake_word(callback):
    """Start wake word detection in a background thread"""
    t = threading.Thread(
        target=listen_for_wake_word,
        args=(callback,),
        daemon=True,
    )
    t.start()