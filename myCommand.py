#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import pyttsx3
import webbrowser
from weather import Weather, Unit


def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis:")
        speak("I'm listening!.....")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def getWeather(location):
    weather = Weather(unit=Unit.CELSIUS)
    lookup = weather.lookup_by_location(location)
    condition = lookup.condition
    speak(condition.text)

def jarvis(data):
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    if "how are you" in data:
        speak("Hey, I am fine")

    if "name" in data or "call you" in data or "you have a name" in data:
        speak("Hey Dharam, I am designed to serve you. You named me Jarvis")

    if "time now" in data:
        speak("The current time: " + ctime())

    if "current weather in" in data:
        data = data.split(" ")
        location = data[3]
        getWeather(location)

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is.")
        webbrowser.get(chrome_path).open("https://www.google.nl/maps/place/" + location)

    if "what is" in data:
        data = data.split(" ")
        keyword = data[2]
        speak("Hold on, lemme find this on the internet....")
        webbrowser.get(chrome_path).open("https://www.google.com/search?source=hp&ei=WocPXaNW6fWrAcm1i5AO&q=" + keyword + "&oq=" + keyword)

# initialization
time.sleep(2)
print('Jarvis:')
speak("Hi, what can I do for you?")

while 1:
    data = recordAudio()
    jarvis(data)

    if 'exit' in data or 'abort' in data or 'stop' in data:
        break
