import speech_recognition as sr
from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text = text, lang = 'vi')
    filename = 'voice.mp3'
    #tts.save(filename)
    playsound.playsound(filename)

