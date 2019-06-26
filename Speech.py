import pyttsx3
from weather import Weather, Unit

engine = pyttsx3.init()
# weather = Weather(unit=Unit.CELSIUS)
# lookup = weather.lookup_by_location('krakow')
# condition = lookup.condition
# engine.say(condition.text)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
# engine.say('Google Speech API v2 is limited to 50 queries per day. Make sure you have a good microphone. Are you are looking for text to speech instead? This is the installation guide for Ubuntu Linux. ')
