import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):

    engine.say(text)

    engine.runAndWait()


def listen():

    listener = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Listening...")

        listener.adjust_for_ambient_noise(source)

        voice = listener.listen(source)

    try:

        command = listener.recognize_google(voice)

        print("You said:", command)

        return command.lower()

    except:

        print("Sorry, samajh nahi aaya 😅")

        return ""