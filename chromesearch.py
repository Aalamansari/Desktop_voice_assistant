import webbrowser
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty("rate", 197)

def speak (audio):          #Function that will convert text to speech
    engine.say(audio)
    print("Zion : ",audio)
    engine.runAndWait()


def search(query):
      query = query.replace("search", "")
      url = "https://www.google.com/search?q="
      search_url = url+query
      chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
      webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
      webbrowser.get('chrome').open(search_url)
      speak("This is what I found on Google chrome")