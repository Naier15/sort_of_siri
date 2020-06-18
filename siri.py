import speech_recognition as sr
import pyttsx3 as pt
import os
import sys
import webbrowser

engine = pt.init()

def command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		engine.say("Слушаю Вас")
		engine.runAndWait()
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source,duration=1)
		audio = r.listen(source, phrase_time_limit=8)
	try:
		task = r.recognize_google(audio, language="ru-RU").lower()
		engine.say("Вы сказали " + task)
		engine.runAndWait()
	except sr.UnknownValueError:
		engine.say("Я Вас не поняла")
		engine.runAndWait()
		task = command()
	return task
	
def makeSomething(task):
	if "открой браузер" in task:
		url = "http://google.com"
		webbrowser.open(url)
	if "погода" in task:
		url = "https://www.gismeteo.ru/weather-nakhodka-4879/"
		webbrowser.open(url)
	elif "стоп" in task:
		engine.say("До свидания")
		engine.runAndWait()
		sys.exit()

while True:
	makeSomething(command())



# engine.say("Чего тебе надобно?")
# engine.runAndWait()
# engine.stop()