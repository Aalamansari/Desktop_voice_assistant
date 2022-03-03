from datetime import datetime
import pyttsx3
import speech_recognition as sr
import os    # To get the access to our windows application like notepad
import wikipedia    
import webbrowser
import pywhatkit as kit
import sys
import smtplib
import pyautogui
import time
import requests 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak (audio):          #Function that will convert text to speech
    engine.say(audio)
    print("Zion : ",audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing....") 
        query = r.recognize_google(audio,language='en-in')
        print(f"User : {query}\n")

    except Exception as e:
        speak("Please say that again...") 
        return "None"
    
    return query          

def intro():


    hour  = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
        speak("Zion at your service")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
        speak("Zion at your service")

    else:
        speak("Good Evening sir")    
        speak("Zion at your service")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aalamansari1712@gmail.com','ShadowFight3@')
    server.sendmail('aalamansari1712@gmail.com',to,content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=2ca1d8fcbb354587b5fd92709b0c0217'
    news  = requests.get(main_url).json()
    # print(news)
    article = news["articles"]
    # print(article)
    
    number = ['First','Second','Third','Fourth','Fifth']
    headline = []
    for top_news in article:
        headline.append(top_news['title'])

    for i in range(5):
        speak(f"{number[i]} news is that {headline[i]}")    



if __name__ =="__main__":
    intro()
    
    # if 1:  
    while True:
        query = takecommand().lower()

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
             
        elif "on youtube" in query:
            query = query.replace("on youtube","")
            query = query.replace("play","")
            kit.playonyt(query)

        elif "email" in query:
          try:    
            # speak("To whom you want to send email?\n")
            # to = takecommand().lower()
            # to =  to.replace(" ","").replace("attherate","@")
            to = "001.ksharif@gmail.com"
            speak("What would you like to send?\n")
            content = takecommand().lower()
            sendEmail(to,content)
            speak(f"email has been sent to {to}")
          except Exception as e:
              speak(f"sorry sir, I am not able to sent email to {to}\n")  

        elif "close" in query:
           if "notepad" in query:
               speak("Okay sir, closing notepad")
               os.system("taskkill /f /im notepad.exe") 
        
        elif "shutdown the system" in query:
            speak("Sir do you want me to shutdown the system ?")
            check = takecommand().lower()
            if "yes" in check:
             os.system("shutdown /s /t 5")          

        elif "restart the system" in query:
            speak("Sir do you want me to restart the system ?")
            check = takecommand().lower()
            if "yes" in check:
             os.system("shutdown /r /t 5")

        elif "go to sleep" in query:
            speak("Sir do you want me to go to sleep ?")
            check = takecommand().lower()
            if "yes" in check:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "news" in query:
            speak("Please wait sir, fetching the hottest news of the day")
            news()

        elif "switch window" in query:
            pyautogui.keyDown("alt")  #keeeps pressing the alt key
            pyautogui.press("tab")
            # time.sleep(1)
            pyautogui.keyUp("alt")

        elif "my location" in query:
            speak("wait sir, let me check")
            try:
                 ip = requests.get('https://api.ipify.org').content.decode('utf8')     #requesting my ip address from the ip-api site and decoding it to utf8 format
                 get_response =  requests.get("http://ip-api.com/json/"+ip).json()    #requesting my location info in byte string format from ip-api server and converting it into str dict type using json() method
                 speak(f"Sir, we are currently in {get_response['city']} of {get_response['regionName']} having postal code {get_response['zip']}")
            except Exception as e:
                speak("Sir due to network issue I am not able to request data from server")
                speak("Please try again sometime later")       

        elif "screenshot" in query:
            try:
                speak("Sir, please tell me with which name I should save this screenshot?")
                name = takecommand()
                speak("Taking the screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()                                         #using pyautogui to take a screenshot
                img.save(f"{name}.png")                                              #using pyautogui to save the screenshot in DESKTOP_ASSISTANT folder
                speak("Screenshot has been saved in our main folder")   
            except Exception as e:
                 speak("Sir due to some error I am not able to take screenshot")
                 speak("Please try again sometime later")  
           

        if "no thanks" in query:
            speak("Pleasure to be at your service")
            sys.exit()
  

        # speak("Is there anything else you want me to do for you?")    