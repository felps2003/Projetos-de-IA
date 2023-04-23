from functions import *
from pedidos import *

count = 0
count2 = 0
while True:
    if count == 1:
        break
    if count2 == 0:
        texto = reconhecerFala("Olá sou a Samambaia, se precisar da minha ajuda é só dizer o meu nome")
        count2 +=1
    else:
        texto = reconhecerFala("diga?")
    if texto == None:
        texto = 'a'
    texto = texto.lower()
    if 'samambaia' in texto:
        falar('conectado com sucesso')
        while True:
            try:
                pedido = reconhecerFala('por favor me peça para fazer algo!').lower()
                if 'parar' in pedido or 'sair' in pedido or 'saia' in pedido or 'chega' in pedido:
                    falar("Tudo bem então! tchau!")
                    count = 1
                    break
                elif 'ria' in pedido:
                    falar("RA! RA! RA! RA RA! RA! RA!")
                elif 'abrir' in pedido or 'abra' in pedido or 'abrisse' in pedido and 'arquivo' in pedido: 
                    arquivo = reconhecerFala('Ok vamos procurar o arquivo, qual é o nome?').lower()
                    abrir(arquivo)
                elif 'tempo' in pedido or 'dia' in pedido or 'horas' in pedido:
                    falar(tempo())
                elif 'pesquisar' in pedido:
                    pesquisa = reconhecerFala('O que você quer pesquisar?')
                    pesquisar(pesquisa)
                elif 'conversar' in pedido:
                    conversar()
            except:
                pass
            
    elif 'não' in texto:
        falar("Tudo bem então tchau!")
        break
    else:
        falar('Por favor tente novamente!')
