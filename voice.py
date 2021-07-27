import speech_recognition as sr
from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text = text, lang = 'vi')
    filename = 'voice.wav'
    tts.save(filename)
    playsound.playsound(filename)

# speak("Đeo khẩu trang")