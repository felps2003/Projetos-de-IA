from functions import *

falar("Olá tudo bem ? Meu nome é Samambaia, sou uma assistente virtual e vou te ajudar, então por favor diga a senha!")
count = 0
while True:
    if count == 1:
        break
    texto = reconhecerFala().lower()
    if texto == 'samambaia':
        falar('conectado com sucesso')
        falar('por favor me peça para fazer algo!')
        while True:
            pedido = reconhecerFala().lower()
            if pedido == 'parar':
                falar("Tudo bem então! tchau!")
                count = 1
                break
            elif pedido == 'ria':
                falar("RA! RA! RA! RA RA! RA! RA!")
            elif pedido == 'fale sobre a segunda guerra':
                falar('A Segunda Guerra Mundial foi um conflito militar global que durou de 1939 a 1945, envolvendo a maioria das nações do mundo — incluindo todas as grandes potências — organizadas em duas alianças militares opostas: os Aliados e o Eixo')
                falar('Além disso também posso te mostrar como foram os sons na epoca')
                falar('Você quer escutar ?')
                pedido = reconhecerFala().lower()
                if pedido == 'sim':
                    falar("Pow pow pow, pleu pleu, baduntis, pow, piu piu piu, e foi assim")
            else:
                falar('por favor me peça para fazer algo!')
            
    elif texto == 'parar':
        falar("Tudo bem então tchau!")
        break
    else:
        falar('Por favor tente novamente!')

