from functions import *
import datetime 
import os

diretorios = {
    'google': 'https://www.google.com/',
    'youtube': 'https://www.youtube.com/',
    'códigos': 'https://github.com/felps2003?tab=repositories',
    'notepad': 'notepad.exe'
}

def tempo():
    agora = datetime.datetime.now()
    mensagem = f'Hoje é dia {agora.day}, mês {agora.month}, do ano de {agora.year}. Agora são {agora.hour}:{agora.minute}'
    return mensagem

def abrir(mensagem):
    if mensagem in diretorios.keys():
        falar('Encontrei o arquivo, irei abrilo')
        os.startfile(diretorios[mensagem])
    else:
        falar('Não encontrei o arquivo, me desculpe')
        falar('Quer que eu pesquise para você ?')
        pedido = reconhecerFala()
        if pedido == 'sim':
            pesquisar(mensagem)
        else:
            falar('Ok então tudo bem!')    

def pesquisar(mensagem):
    if ' ' in mensagem:
        mensagem = mensagem.replace(' ','+')
    diretorio = f'https://www.google.com/search?q={mensagem}'
    os.startfile(diretorio)