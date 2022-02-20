from datetime import datetime
import pyttsx3
import speech_recognition as sr
import os    # To get the access to our windows application like notepad
import wikipedia    
import webbrowser
import pywhatkit as kit
from pywhatkit.remotekit import start_server
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak (audio):          #Function that will convert text to speech
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....") 
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Please say that again...") 
        return "None"
    return query          

def intro():


    hour  = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir.. Jarvis at your service!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir.. Jarvis at your service!")

    else:
        speak("Good Evening sir.. Jarvis at your service!")    

    


if __name__ =="__main__":
    intro()
    
    # if 1:  
    while True:
        query = takecommand().lower()

        #logic building tasks

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results  = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            speak(results)
            

        elif "open notepad" in query:
            notepath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(notepath)
        
        elif "open youtube" in query:
            url1 = "youtube.com"
            chrome_path = r'C:\Program Files\Google\\Chrome\Application\chrome.exe'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url1)

        elif "open chrome" in query:
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            os.startfile(chrome_path)
          
        elif "open stack overflow" in query:
              url2 = "stackoverflow.com"
              chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
              webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
              webbrowser.get('chrome').open_new_tab(url2)

        # elif 'open music' in query:
        #     music_directory

        elif ".com" in query:
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(query)

        elif "time" in query:
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {current_time}")

        elif "search" in query:
             query = query.replace("search", "")
             url = "https://www.google.com/search?q="
             search_url = url+query
             chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
             webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
             webbrowser.get('chrome').open(search_url)

        elif "send a whatsapp message" in query:
             hour_time = int(datetime.now().strftime("%H")) 
             minute_time = int(datetime.now().strftime("%M")) +2
             speak("What is the message you want me to send?")
             message = takecommand()
             kit.sendwhatmsg("+919372036044",f"{message}",hour_time,minute_time)
             

       
        elif "no thanks" in query:
            speak("Pleasure to be at your service")
            sys.exit()


        speak("Do you want me to do something else for you")    