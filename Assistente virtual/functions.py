import speech_recognition as sr
import gtts
from playsound import playsound
import os

rec = sr.Recognizer()

def reconhecerFala(fala):
    #print(sr.Microphone().list_microphone_names())
    try:
        with sr.Microphone(1) as mic:
            rec.adjust_for_ambient_noise(mic)
            falar(fala)
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            return texto
    except:
        return falar('Não consegui te entender')

def falar(mensagem):
    try:
        os.remove("frase.mp3")
    except:
        ...
    frase = gtts.gTTS(mensagem,lang='pt-br',slow=False)
    frase.save('frase.mp3')
    playsound('frase.mp3')




