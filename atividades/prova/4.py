# questao 4: le respostas de enquete até que valor seja 0

enquete = {'q1': ['Qual a melhor banda?','1- Pink Floyd', '2- Beatles', '3- Led Zeppelin', '4- Outra'],
           'q2': ['Qual o melhor álbum?','1- Dark Side of the Moon', '2- The Wall', '3- Wish You Were Here', '4- Outro'],
           'q3': ['Qual o melhor baixista?','1- Roger Waters', '2- Paul McCartney', '3- Baixista do Led Zeppelin', '4- Outro']
           }
responder = 1
participantes = 0
respostas = []
while responder != 0:
    responder = int(input('Responder a enquete?(1 / 0):'))
    if responder != 0:
        participantes += 1
        cnt = 0
        for x,y in enquete.items():
            for j in y:
                print(j)
            resposta = int(input('Digite sua resposta: '))
            respostas.append([])
            respostas[cnt].append(resposta)
            cnt += 1
print(f'Contagem de participantes: {participantes}, Contagem de respostas q1: {len(respostas[0])}, Contagem de respostas q3: {len(respostas[0])}, Contagem de respostas q3: {len(respostas[0])}')