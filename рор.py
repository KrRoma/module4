import time

# import os
# from gtts import gTTS
# from pygame import mixer
#
# my_file = open('some.txt','r',encoding='utf-8')
# my_text = my_file.read()
# my_file.close()
#
# mixer.init()
# tts = gTTS(text=my_text,lang='ru')
# tts.save('audio_1.mp3')
# mixer.music.load('audio_1.mp3')
# mixer.music.play()
# while mixer.music.get_busy():
#     time.sleep(1)
# mixer.music.unload()
import pyaudio
# import speech_recognition as sr
#
# recognize = sr.Recognizer()
# while True:
#     with sr.Microphone() as source:
#         print('скажи что нибудь...')
#         audio = recognize.listen(source)
#     speech= recognize.recognize_google(audio,language='ru_Ru').lower()
#     print('вы сказали',speech)
#     if speech=='привет':
#         print('Привет)')
#     if speech=='пока':
#         print('пока(')
#         break
