import speech_recognition as sr
import gtts
from playsound import playsound
import os

def reconhecerFala():
    rec = sr.Recognizer()
    #print(sr.Microphone().list_microphone_names())
    try:
        with sr.Microphone(1) as mic:
            rec.adjust_for_ambient_noise(mic)
            falar('Estou te escutando')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            return texto
    except:
        return 'Não consegui te endenter'

def falar(mensagem):
    frase = gtts.gTTS(mensagem,lang='pt-br',slow=False)
    frase.save('frase.mp3')
    playsound('frase.mp3')
    os.remove("frase.mp3")