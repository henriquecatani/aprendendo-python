import random
def adivinhaNumero():
    numero = random.randint(1,101)
    numTentativas = 10
    i = 1
    while i <= numTentativas:
        tentativa = int(input('Diga um número de 1 a 100: '))
        if tentativa == numero:
            print('Parabéns!! Você adivinhou! Tentativas: ', i)
            return
        elif 1 > numero > 100:
            print('Número está entre 1 e 100.')
            i += 1
            
        elif tentativa in range(numero-2, numero+2):
            print('Tá quentíssimo!')
            print('Tentativas: ', i)
            i += 1
            
        elif tentativa in range(numero-5, numero+5):
            print('Tá quente!')
            print('Tentativas: ', i)
            i += 1
            
        elif tentativa in range(numero-10, numero+10):
            print('Tá morno!')
            print('Tentativas: ', i)
            i += 1
            
        elif tentativa in range(numero-25, numero+25):
            print('Tá frio!')
            print('Tentativas: ', i)
            i += 1
        elif tentativa in range(numero-50, numero+50):
            print('Tá muito frio!')
            print('Tentativas: ', i)
            i += 1
    print(f'Acabaram suas tentativas! Tentativas: {numTentativas}')
    return
        
adivinhaNumero()