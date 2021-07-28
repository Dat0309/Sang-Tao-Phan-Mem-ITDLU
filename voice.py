import speech_recognition as sr
from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text = text, lang = 'vi')
    filename = 'wanning.wav'
    tts.save(filename)
    playsound.playsound(filename)

speak("Cảnh báo không đeo khẩu trang")