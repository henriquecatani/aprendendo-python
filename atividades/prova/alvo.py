lista = [3,7,1,9,2]
alvo = 9

for item in lista:
    if item == alvo:
        encontrado = True
    
if encontrado:
    print('Encontrado')
else:
    print('Não encontrado')