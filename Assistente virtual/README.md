# Assistente virtual Samambaia

# Versão 1 - metas

- Fazer o speech to text
- Fazer o text to speech
- Criar alguns comandos, como ver as horas ou abrir algum programa no pc

## Criando reconhecimento de voz

LIBS

- SpeechRecognition (pip install SpeechRecognition)
- PyAudio (python -m install pyaudio)

    Essa primeira versão tem apenas o reconhecimento de voz, então foi bem mais fácil, o reconhecimento de voz esta funcionando perfeitamente. 

```python
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
```

## Criando a Fala da assistente

LIBS

- gTTS(pip install gTTS)
- playsound (pip install playsound==1.2.2)
- os

    Essa versão ainda utiliza voz do google, e também tem um delay entre a fala do usuário e o reconhecimento.

```python
def falar(mensagem):
    try:
        os.remove("frase.mp3")
    except:
        ...
    frase = gtts.gTTS(mensagem,lang='pt-br',slow=False)
    frase.save('frase.mp3')
    playsound('frase.mp3')
```

---

## Pedidos

### Tempo

LIBS

- datetime (import datetime)

    Esse pedido te fala o dia e também o horário, ficou bem completo até para a primeira versão.

```python
def tempo():
    agora = datetime.datetime.now()
    mensagem = f'Hoje é dia {agora.day}, mês {agora.month}, do ano de {agora.year}. Agora são {agora.hour}:{agora.minute}'
    return mensagem
```

### Abrir arquivos

LIBS

- os (import os)

    Essa versão apenas abre os arquivos que coloquei em um dicionário, acho que devo encontrar alguma forma de abrir arquivos sem estarem nesse dicionário.

```python
def abrir(mensagem):
    if mensagem in diretorios.keys():
        falar('Encontrei o arquivo, irei abrilo')
        os.startfile(diretorios[mensagem])
    else:
        falar('Não encontrei o arquivo, me desculpe')
```

### Pesquisar

    Essa versão pesquisa palavras no google mesmo com separação entre elas.
    
```python 
def pesquisar(mensagem):
    if ' ' in mensagem:
        mensagem = mensagem.replace(' ','+')
    diretorio = f'https://www.google.com/search?q={mensagem}'
    os.startfile(diretorio)
```