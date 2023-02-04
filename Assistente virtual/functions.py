import speech_recognition as sr

def reconhecerFala():
    rec = sr.Recognizer()
    #print(sr.Microphone().list_microphone_names())
    while True:
        with sr.Microphone(1) as mic:
            rec.adjust_for_ambient_noise(mic)
            print('Por favor me diga a senha')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            print('Você disse: '+texto)
            if texto == 'batata frita':
                print('conectado com sucesso')
            else:
                print('Por favor tente novamente!')
