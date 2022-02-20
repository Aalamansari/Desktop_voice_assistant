#pip install SpeechRecognition
#pip install pyttsx3
#pip install pyaudio
from datetime import datetime 

hour_time = (int(datetime.now().strftime("%H"))) 
minute_time = (int(datetime.now().strftime("%M")))
print(type(hour_time))
print(type(minute_time))