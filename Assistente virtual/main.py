from functions import *
from pedidos import *

count = 0
while True:
    if count == 1:
        break
    texto = reconhecerFala("Olá tudo bem ? Meu nome é Samambaia, sou uma assistente virtual e vou te ajudar, então por favor diga a senha!").lower()
    if texto == 'samambaia':
        falar('conectado com sucesso')
        while True:
            try:
                pedido = reconhecerFala('por favor me peça para fazer algo!').lower()
                if pedido == 'parar':
                    falar("Tudo bem então! tchau!")
                    count = 1
                    break
                elif pedido == 'ria':
                    falar("RA! RA! RA! RA RA! RA! RA!")
                elif pedido == 'fale sobre a segunda guerra':
                    falar('A Segunda Guerra Mundial foi um conflito militar global que durou de 1939 a 1945, envolvendo a maioria das nações do mundo — incluindo todas as grandes potências — organizadas em duas alianças militares opostas: os Aliados e o Eixo')
                    falar('Além disso também posso te mostrar como foram os sons na epoca')
                    pedido = reconhecerFala('Você quer escutar ?').lower()
                    if pedido == 'sim':
                        falar("Pow pow pow, pleu pleu, baduntis, pow, piu piu piu, e foi assim")
                elif pedido == 'abrir arquivo':
                    arquivo = reconhecerFala('Ok vamos procurar o arquivo, qual é o nome?').lower()
                    abrir(arquivo)
                elif pedido == 'tempo':
                    falar(tempo())
                elif pedido == 'pesquisar':
                    pesquisa = reconhecerFala('O que você quer pesquisar?')
                    pesquisar(pesquisa)
            except:
                falar('por favor me peça para fazer algo!')
            
    elif texto == 'parar':
        falar("Tudo bem então tchau!")
        break
    else:
        falar('Por favor tente novamente!')

