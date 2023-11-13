import speech_recognition as sr
import gtts
import openai
import playsound as ps
import os

rec = sr.Recognizer()

# Criação dos parametros da SAMAM utilizando OPENAI ---------
openai.api_key = ""
model_engine = "text-davinci-003"
# -----------------------------------------------------------

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
    ps.playsound('frase.mp3')

def samam(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=200,
        temperature = 0.5,
    )
    print(response.choices[0].text)
    return falar(response.choices[0].text)

