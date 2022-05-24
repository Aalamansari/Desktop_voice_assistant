import webbrowser
import pyttsx3
import sys
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty("rate", 197)

def speak (audio):          #Function that will convert text to speech
    engine.say(audio)
    print("Zion : ",audio)
    engine.runAndWait()


def opennotepad():
      notepath = "C:\\windows\\system32\\notepad.exe"
      os.startfile(notepath)

def openyoutube():
     url1 = "youtube.com"
     chrome_path = r'C:\Program Files\Google\\Chrome\Application\chrome.exe'
     webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
     webbrowser.get('chrome').open_new_tab(url1)      

def openstack():
    url2 = "stackoverflow.com"
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url2)     

def openchrome():
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    os.startfile(chrome_path)

def com(query):
      chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
      webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
      webbrowser.get('chrome').open(query)    

