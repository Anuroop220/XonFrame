import speech_recognition as sr
import pyttsx3

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
        except:
            return ""

def speak(text):
    print(f"E.L.I.X: {text}")
    engine.say(text)
    engine.runAndWait()