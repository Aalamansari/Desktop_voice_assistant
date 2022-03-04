#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
# from datetime import datetime 
import pyttsx3
# import pywhatkit as kit
# import speech_recognition as sr
# import requests
# import webbrowser
# from geopy.geocoders import Nominatim
# from numpy import place
from requests import get

engine = pyttsx3.init()
engine.setProperty("rate", 190)
engine.say("I am the text spoken after changing the speech rate.")
engine.runAndWait()

# ip = get('https://api.ipify.org').content.decode('utf8')
# get_response =  get("http://ip-api.com/json/"+ip).json()   #If we don't use json() it will be byte string not a dictionary so to convert it to from byte string to str then use .json() method
# print(get_response)
# print(f"Sir, we are currently in {get_response['city']} of {get_response['regionName']} having postal code {get_response['zip']}")
# data = pgeocode.Nominatim('IN')
# print(data.query_postal_code(get_response['zip']))

# print(type(format(ip)))
# g = geocoder.ip(format(ip))
# myAddress = g.latlng
# print(g)
# my_map1 = folium.Map(location=myAddress,zoom_start=12)
# folium.CircleMarker(location=myAddress,radius=50).add_to(my_map1)

# my_map1.save("my_map.html")
# webbrowser.open_new_tab("my_map.html")    #used webbrowser to open the html page containing the location

# geolocator = Nominatim(user_agent="geoapiExercises")
# place = "Mankhurd"
# location = geolocator.geocode(place)
# print(location)