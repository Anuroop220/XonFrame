import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 165)


def listen():
    """it records the audio first then converts it to text"""
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=8
            )
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()

        except sr.UnknownValueError:
            print("Couldn't hear please repeat")
            return ""

        except sr.RequestError:
            print("No internet connection for speech recognition")
            return ""

        except Exception as error:
            print(f"Microphone error: {error}")
            return ""


def speak(text):
    """Read text aloud."""
    print(f"E.L.I.X: {text}")

    try:
        engine.say(text)
        engine.runAndWait()

    except Exception as error:
        print(f"Text-to-speech error: {error}")