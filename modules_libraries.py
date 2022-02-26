#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
from datetime import datetime 
import pyttsx3
import pywhatkit as kit
import speech_recognition as sr
import requests

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=2ca1d8fcbb354587b5fd92709b0c0217'
    news  = requests.get(main_url).json()
    # print(news)
    article = news["articles"]
    # print(article)

    headline = []
    for top_news in article:
        headline.append(top_news['title'])

    for i in range(5):
        print(1+i,headline[i])    

news()