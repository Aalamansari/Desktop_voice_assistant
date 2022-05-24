from datetime import datetime
from cv2 import SparseMat_HASH_BIT
import pyttsx3
import speech_recognition as sr
import os    # To get the access to our windows application like notepad
import pywhatkit as kit
import sys  #Used to exit the program
import smtplib
import pyautogui
import time
import requests 

engine = pyttsx3.init('sapi5')    #initiating an engine from pyttsx3 
voices = engine.getProperty('voices')  #getting the voices property from the engine
# engine.setProperty('voices',voices[0].id)  #setting the voice of Zion that would give response to user
engine.setProperty('language','hi')
engine.setProperty("rate", 197)    #setting the rate of speed with which the Zion would speak


def speak (audio):          #Function that will convert text to speech
    engine.say(audio)
    print("Zion : ",audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        # r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        r.energy_threshold=350
        audio = r.listen(source,0,4) #try source,0,4

    try:
        print("Recognizing....") 
        query = r.recognize_google(audio,language='en-in')
        print(f"User : {query}\n")

    except Exception as e:
        speak("Please say that again...") 
        return "None"
    return query          

def Greetme():
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
    Greetme()

    # if 1:  
    while True:    #infinite loop
        query = takecommand().lower()

        if "what is your name" in query:
            speak("I am Zion")

        elif "hello" in query:
            speak("Hello sir, how are you?")

        elif "i am fine" in query:
            speak("Glad to hear that sir") 

        elif "how are you" in query:
            speak("Perfect and ready to work with you") 
        
        elif "thank you" in query:
            speak("You are welcome sir")

        elif "who is your owner" in query:
            speak("My owner's are Group 6 of second year of computer engineering at Anjuman-I-Islam's kalsekar technical campus ")                  

        elif "nice" in query or "nice work" in query:
            speak("Happy to be at your service")
 
        elif "tell me about yourself" in query  or "tell me more about you" in query:
            speak("Sir, I am Zion.")
            speak("An desktop voice assistant created for the purpose of serving you.")
            speak("I am able to listen to your commands with the help of Speech Recognition module and able to reply to them with the help of different modules provided by Python ")

        elif "are you a copy" in query:
            speak("No, I was created with the  hardship of Group 6")

        elif "open notepad" in query:
            notepath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(notepath)

        elif "close notepad" in query:
        #    if "notepad" in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe") 
        #    elif "vs code" in query:
        #        speak("Okay sir, closing vscode")
        #        os.system("taskkill /f /im Code.exe")     
        #    elif "chrome" in query:
        #        speak("Okay sir, closing chrome")
        #        os.system("taskkill /f /im chrome.exe")

        elif "open" in query:
            from diffapps import openappweb
            openappweb(query)
        
        elif "close" in query:
            from diffapps import closeappweb
            closeappweb(query)
  
        elif "time" in query:
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {current_time}")

        elif "search" in query:
            from chromesearch import search
            search(query)

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


        elif "shutdown the system" in query:
            speak("Sir do you want me to shutdown the system ?")
            check = takecommand().lower()
            if "yes" in check:
             os.system("shutdown /s /t 5")        
            elif "no" in check:
                pass   

        elif "restart the system" in query:
           try :
              speak("Sir do you want me to restart the system ?")
              check = takecommand().lower()
              if "yes" in check:
                os.system("shutdown /r /t 5")
           except Exception as e:
                 speak("Can you confirm once again?")
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

        elif "window" in query:
            pyautogui.keyDown("alt")  #keeeps pressing the alt key
            pyautogui.press("tab")
            # time.sleep(1)
            pyautogui.keyUp("alt")

        elif "my location" in query:    
            from location import mylocation
            mylocation()

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


        if "stop" in query or "top" in query:
            speak("Pleasure to be at your service")
            sys.exit()


