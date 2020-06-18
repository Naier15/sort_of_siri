import speech_recognition as sr
import pyttsx3 as pt

engine = pt.init()
r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    engine.say("talk")
    engine.runAndWait()
    audio = r.listen(source, phrase_time_limit=7)
    engine.stop()

query = r.recognize_google(audio, language="ru-RU")
print("You said: " + query)
