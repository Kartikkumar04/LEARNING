import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
engine.setProperty("rate", 150)  # fixed typo: setproperty → setProperty


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            content = r.recognize_google(audio, language='en-in')
            print("You said:", content)
            return content.lower()
        except sr.UnknownValueError:
            print("Sorry, I can't understand.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

def main_process():
    speak("I am Codey, your voice assistant. How can I help you today?")
    while True:
        request = command()
        if request == "":
            continue

        if "hello" in request:
            speak("Welcome, how can I help you?")

        elif "playing music" in request:
            webbrowser.open("https://youtu.be/l2I6YClmhMA?si=NFS-vE3oEBohSNkX")

        elif "time" in request:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Current time is {current_time}")
            speak(f"Current time is {current_time}")

        elif "website" in request:
            speak("Opening Pisoft Informatics Private Limited")
            webbrowser.open("https://pisoftinformatics.com/")

        elif "exit" in request or "quit" in request or "stop" in request:
            speak("Thank you for using me, have a great day!")
            break

        else:
            search_url = f"https://www.google.com/search?q={request.replace(' ', '+')}"
            speak(f"Searching for {request}")
            webbrowser.open(search_url)

main_process()
