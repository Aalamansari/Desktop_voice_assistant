import pyttsx3
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty("rate", 197)

def speak (audio):          #Function that will convert text to speech
    engine.say(audio)
    print("Zion : ",audio)
    engine.runAndWait()


def mylocation():
    speak("wait sir, let me check")
    try:
         ip = requests.get('https://api.ipify.org').content.decode('utf8')     #requesting my ip address from the ip-api site and decoding it to utf8 format
         get_response =  requests.get("http://ip-api.com/json/"+ip).json()    #requesting my location info in byte string format from ip-api server and converting it into str dict type using json() method
         speak(f"Sir, we are currently in {get_response['city']} of {get_response['regionName']} having postal code {get_response['zip']}")
    except Exception as e:
            speak("Sir due to network issue I am not able to request data from server")
            speak("Please try again sometime later")         