import speech_recognition as sr
import pyttsx
import os
import json

#----------------------- Reading configurations -------------------------------#
with open("config.json", "r") as read_file:
    config = json.load(read_file)

AI_NAME= config["AI"]['NAME']
print(f"Olá! meu nome é {AI_NAME}")

#----------------------------- Speaker ----------------------------------------#

speaker = pyttsx.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

#------------------------- Speech Recognition ---------------------------------#
#
# recognizer = sr.Recognizer()
#
# with sr.Microphone() as sound:
#     recognizer.adjust_for_ambient_noise(sound)
#     while True:
#         try:
#             audio = recognizer.listen(sound)
#             speech = recognizer.recognize_google(audio, language='pt')
#             print("Você disse: ", speech)
#
#             response = "I am ready!"
#             print(f"{AI_NAME} disse: {response}")
#             speak(response)
#
#         except:
#             response = "Something are wrong!"
#             print(f"{AI_NAME} disse: {response}")
#             speak(response)
