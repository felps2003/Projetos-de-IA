from functions import *

falar("Olá tudo bem ? Sou uma assistente virtual, bora começar ?")
count = 0
while True:
    if count == 1:
        break
    texto = reconhecerFala()

    if texto == 'batata frita':
        falar('conectado com sucesso')
        falar('por favor me peça para fazer algo!')
        while True:
            pedido = reconhecerFala()
            if pedido == 'parar':
                falar("Tudo bem então! tchau!")
                count = 1
                break
            elif pedido == 'ria':
                falar("RA RA RA RA RA RA RA")
            else:
                falar('por favor me peça para fazer algo!')
            
    elif texto == 'parar':
        falar("Tudo bem então tchau!")
        break
    else:
        falar('Por favor tente novamente!')

