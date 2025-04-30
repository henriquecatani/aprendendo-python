# Algoritmos e Programação - Lista de exercícios 5
# Aluno: Henrique Catani

def tabuada(n):
    ''' exibe a tabuada de n '''
    for i in range(1,11):
        tabu = n * i
        print(f'{n}x{i} = {tabu}')


def somaCincoNumeros():
    ''' le 5 numeros e retorna a soma deles '''
    soma = 0
    for i in range(1,6):
        num = int(input('Diga um número:'))
        soma += num
    return '''Soma dos números: {}'''.format(soma)

def paresImpares(n1,n2):
    ''' exibe os números pares e ímpares entre n1 e n2 '''
    impares = []
    pares = []
    for i in range(n1 + 1, n2):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    print(f"Impares:", end=' ')
    for j in impares:
        print(j, end=', ')
    print(f'\b\b ') # remove a vírgula do último

    print(f"Pares:", end=' ')
    for k in pares:
        print(k, end=', ')
    print(f'\b\b ')

def ehPrimo(n):
    ''' algoritmo usado: verificar se é divisivel 
        por qualquer numero até a sqrt do numero '''
    if n < 2:
        return False
    i = 2
    while i * i <= n: 
        ''' ^ se cada numero é menor ou 
        igual à raiz do numero inicial '''
        if n % i == 0:
            return False # se for divisivel, não é primo
        i += 1
    return True

def todosPrimos(n1, n2):
    ''' imprime todos os numeros primos
    entre n1 e n2 '''
    primos = []
    n1_b = n1
    while n1 <= n2:
        if ehPrimo(n1):
            primos.append(n1)
        n1 += 1
    print(f"Primos entre {n1_b} e {n2}:", end=' ')
    for k in primos:
        print(k, end=', ')
    print(f'\b\b ')
def qntsPosNeg():
    ''' le 10 numeros e retorna a quantidade de positivos e negativos'''
    cntPos = 0
    cntNeg = 0
    numeros = []
    for i in range(1,11):
        numeros.append(int(input('Diga um número inteiro: ')))
    for j in numeros:
        if j > 0:
            cntPos += 1
        elif j < 0:
            cntNeg += 1
    return '''Quantidade de positivos: {}, Quantidade de negativos: {}'''.format(cntPos, cntNeg)

# a partir daqui exercicios com while

def somaAteCem():
    soma = 0
    cnt = 0
    while soma <= 100:
        soma += int(input('Digite um número inteiro: '))
        cnt += 1
    if cnt == 1:
        return "O número é maior que 100!"
    else:
        return '''A soma dos {} números passou de 100!'''.format(cnt)

def posOuNeg():
    ''' le 10 números diferentes de zero e 
    exibe se cada um deles é positivo ou negativo.
    Se o número for 0, não é contado '''
    i = 0
    while i <= 10:
        n = int(input('Diga um número inteiro diferente de 0: '))
        if n > 0: 
            print(f'{n} é positivo')
            i += 1 
        elif n == 0:
            print(f'Zero é inválido')
        else:
            print(f'{n} é negativo')
            i += 1


def senha():
    ''' senha: 2023
    pede input de senha e imprime se é inválida,
    até que seja válida, e conta a qnt de tentativas '''
    senha = '2023'
    senhaValida = False
    cnt = 0
    while senhaValida == False:
        senhaInput = input('Diga a senha: ')
        if senhaInput == senha:
            senhaValida = True
        else:
            print('SENHA INVALIDA')
        cnt += 1
    return '''ACESSO PERMITIDO - {} tentativas'''.format(cnt)

def media():
    ''' le numeros até que o input seja 0,
    e devolve a quantidade de números e
    a média aritmética'''
    
    n = 1
    soma = 0
    cnt = 0
    while n != 0:
        n = int(input('Diga um número ou digite 0 para parar: '))
        if n == 0:
            print('Número zero! Parando...')
        else:
            soma += n
            cnt += 1
    
    if cnt == 0:  # Evitar divisão por zero
        return "Nenhum número foi inserido."
    else:
        media = soma/cnt
        return ''' A média dos {} números lidos é: {}'''.format(cnt, media)

def main():
    funcoes = {
        1 : "tabuada",
        2 : "somaCincoNumeros",
        3 : "paresImpares",
        4 : "todosPrimos",
        5 : "qntsPosNeg",
        6 : "somaAteCem",
        7 : "posOuNeg",
        8 : "senha",
        9 : "media",
        0 : "Sair"
        }
    print(f"Atividades de Algoritmos e Programação 5.\n Aluno: Henrique Catani\n \nSelecione a atividade:") 
    for k, l in funcoes.items():
        print(k, " - ", l)
    escolha = int(input("Opção: "))
    def submenu():
        continuar = input("Aperte Enter para voltar ao menu ")
        if continuar == "": # se somente apertar enter
            main()
    if escolha == 1:
        n1 = int(input("Diga um número inteiro: "))
        print(f'Tabuada do número {n1}:')
        tabuada(n1)
        submenu()
    if escolha == 2:
        print(somaCincoNumeros())
        submenu()
    if escolha == 3:
        n1 = int(input("Diga um número inteiro inicial: "))
        n2 = int(input("Diga um número inteiro final: "))
        paresImpares(n1, n2)
        submenu()
    if escolha == 4:        
        n1 = int(input("Diga um número inteiro inicial (ex.: 1): "))
        n2 = int(input("Diga um número inteiro final (ex.: 1000): "))
        todosPrimos(n1,n2)
        submenu()
    if escolha == 5:
        print(qntsPosNeg())
        submenu()
    if escolha == 6:
        print(somaAteCem())
        submenu()
    if escolha == 7:
        posOuNeg()
        submenu()
    if escolha == 8:
        print(senha())
        submenu()
    if escolha == 9:
        print(media())
        submenu()
    if escolha == 0:
        print(f"Obrigado por usar o programa!\nass. Henrique Catani")
        sair = input(f"\nAperte Enter para sair")
        if sair == "":
            print("")
if __name__ == '__main__':
    main()
