# Algoritmos e Programação - Lista de exercícios 2
# Aluno: Henrique Catani

def parOuImpar(numero):
    if numero % 2 == 0:
        return "O número é par"
    else:
        return "O número é ímpar"
    
def maiorMenor(n1, n2):
    if n1 > n2:
        return "Maior: {}, Menor: {}".format(n1, n2)
    elif n2 > n1:
        return "Maior: {}, Menor: {}".format(n2, n1)
    else:
        return "Os números são iguais!"

def mediaAprovacao(n1,n2,n3):
    media = (n1+n2+n3)/3
    if media >= 7:
        return "Média {}: APROVADO".format(media)
    else:
        return "Média {}: REPROVADO".format(media)
    
def ordemNumeros(n1,n2,n3): 
    if n1 == n2 or n1 == n3 or n2 == n3:
        return "Os números são iguais!"
    else:
        if n1 < n2 and n1 < n3:
            menor = n1
            if n2 < n3:
                medio = n2
                maior = n3
            else:
                medio = n3
                maior = n2
        elif n2 < n1 and n2 < n3:
            menor = n2
            if n1 < n3:
                medio = n1
                maior = n3
            else:
                medio = n3
                maior = n1
        else:
            menor = n3
            if n1 < n2:
                medio = n1
                maior = n2
            else:
                medio = n2
                maior = n1
    return "Menor: {}, Intermediário: {}, Maior: {}".format(menor, medio, maior)

def categoriasNatacao(idade):
    if idade < 5:
        return "O nadador não tem idade o suficiente!"
    elif 5 <= idade <= 7:
        categoria = "infantil A"
    elif 8 <= idade <= 10:
        categoria = "infantil B"
    elif 11 <= idade <= 13:
        categoria = "juvenil A"
    elif 14 <= idade <= 17:
        categoria = "juvenil B"
    else:
        categoria = "adulto"
    return "Categoria: {}".format(categoria)

def aumentoSalario(salario, codigo):
    if codigo == 101:
        percentual = 1.1
    elif codigo == 102:
        percentual = 1.2
    elif codigo == 103:
        percentual = 1.3
    else:
        percentual = 1.4
    salarioNovo = salario * percentual
    return "Salário antigo: {}, Salário novo: {}, Diferença: {}".format(salario, salarioNovo, salarioNovo - salario)
def tipoTriangulo(a,b,c):
    if a < b + c and b < a + c and c < a + b: 
        # ^ fórmula que verifica se é triângulo utilizando AND,
        # pois se qualquer uma das condições for falsa, não é um triângulo
        if a == b and b == c:
            return "Triângulo equilátero"
        elif a == b or a == c or c == b:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Não é um triângulo"

def valorEmNotas(valor, isSpecial = 0):
    valor_b = valor - 6
    n100 = valor // 100
    valor = valor - n100 * 100
    n50 = valor // 50
    valor = valor - n50 * 50
    n20 = valor // 20
    valor = valor - n20 * 20
    n10 = valor // 10
    valor = valor - n10 * 10
    n5 = valor // 5
    valor = valor - n5 * 5
    n2 = valor // 2
    valor = valor - n2 * 2
    if isSpecial == 1: #somente quando chamado por essa própria função mais adiante
        n2 += 3
    if valor == 0:
        return "{} notas de 100, {} notas de 50, {} notas de 20, {} notas de 10, {} notas de 5 e {} notas de 2".format(n100, n50, n20, n10, n5, n2)
    else:
        return valorEmNotas(valor_b, 1) # garante que o algoritmo utilize 3*n2 ao invés de 1*5 + 1
def impostoRenda(valor):
    if valor <= 17989.8:
        percentual = 0
    elif 17989.81 <= valor <= 26961:
        percentual = 7,5
    elif 26961.01 <= valor <= 35948.40:
        percentual = 15
    elif 35948.41 <= valor <= 44918.28:
        percentual = 22.5
    else:
        percentual = 27.5
    imposto = valor * percentual / 100
    return "Valor a ser pago: {}".format(imposto)

def anoBissexto(ano):
    '''
    para uso na função dataValida,
    com base no artigo da Microsoft.
    '''

    if ano % 4 == 0:
        etapa1 = True
    else:
        return False
    if ano % 100 == 0:
        if ano % 400 == 0:
            return True
        else:
            return False
    else:
        return True

def dataValida(dia, mes, ano):
    if ano < 0 or ano > 3000:
        return '{}/{}/{}: Data inválida'.format(dia, mes, ano)
    if (dia or mes) < 1:
        return '{}/{}/{}: Data inválida'.format(dia, mes, ano)
    if mes > 12:
        return '{}/{}/{}: Data inválida'.format(dia, mes, ano)
    if anoBissexto(ano): # função separada para organização
        if mes == 2:
            if dia > 29:
                return '{}/{}/{}: Data Inválida'.format(dia, mes, ano)
            else:
                return '{}/{}/{}: Data Válida'.format(dia, mes, ano)
    else:
        if mes == 2:
            if dia > 28:
                return '{}/{}/{}: Data Inválida'.format(dia, mes, ano)
            else:
                return '{}/{}/{}: Data Válida'.format(dia, mes, ano)
    if mes in (4,6,9,11):
        if dia > 30:
            return '{}/{}/{}: Data inválida'.format(dia, mes, ano)
        else:
            return '{}/{}/{}: Data Válida'.format(dia, mes, ano)
    else: # o resto dos meses, ja que não passaram > 12 no inicio
        if dia > 31:
            return '{}/{}/{}: Data inválida'.format(dia, mes, ano)
        else:
            return '{}/{}/{}: Data Válida'.format(dia, mes, ano)

def main():
    funcoes = {
        1 : "parOuImpar",
        2 : "maiorMenor",
        3 : "mediaAprovacao",
        4 : "ordemNumeros",
        5 : "categoriasNatacao",
        6 : "aumentoSalario",
        7 : "tipoTriangulo",
        8 : "valorEmNotas",
        9 : "impostoRenda",
        10 : "dataValida",
        0 : "Sair"
        }
    print(f"Atividades de Algoritmos e Programação 2.\n Aluno: Henrique Catani\n \nSelecione a atividade:") 
    for k, l in funcoes.items():
        print(k, " - ", l)
    escolha = int(input("Opção: "))
    def submenu():
        continuar = input("Aperte Enter para voltar ao menu ")
        if continuar == "": # se somente apertar enter
            main()
    if escolha == 1:
        n = int(input("Digite um número inteiro: "))
        print(parOuImpar(n))
        submenu()
    if escolha == 2:
        n1 = int(input("Diga o primeiro número: "))
        n2 = int(input("Diga o segundo número: "))
        print(maiorMenor(n1, n2))
        submenu()
    if escolha == 3:
        n1 = int(input("Diga a primeira nota: "))
        n2 = int(input("Diga a segunda nota: "))
        n3 = int(input("Diga a terceira nota: "))
        print(mediaAprovacao(n1, n2, n3))
        submenu()
    if escolha == 4:
        n1 = int(input("Diga um número inteiro: "))
        n2 = int(input("Diga um número inteiro: "))
        n3 = int(input("Diga um número inteiro: "))
        print(ordemNumeros(n1, n2, n3))
        submenu()
    if escolha == 5:
        idade = int(input("Diga a idade do nadador: "))
        print(categoriasNatacao(idade))
        submenu()
    if escolha == 6:
        n1 = int(input("Diga o salário atual: "))
        n2 = int(input("Diga o código do cargo: "))
        print(aumentoSalario(n1, n2))
        submenu()
    if escolha == 7:
        n1 = int(input("Diga o primeiro lado do triângulo: "))
        n2 = int(input("Diga o segundo lado do triângulo: "))
        n3 = int(input("Diga o terceiro lado do triângulo: "))
        print(tipoTriangulo(n1,n2,n3))
        submenu()
    if escolha == 8:
        n1 = int(input("Diga a quantidade de reais a ser convertido: "))
        print(valorEmNotas(n1))
        submenu()
    if escolha == 9:
        valor = int(input("Diga a sua renda:"))
        print(impostoRenda(valor))
        submenu()
    if escolha == 10:
        n1 = int(input("Diga o dia: "))
        n2 = int(input("Diga o mês: "))
        n3 = int(input("Diga o ano: "))
        print(dataValida(n1,n2,n3))
        submenu()

    if escolha == 0:
        print(f"Obrigado por usar o programa!\nass. Henrique Catani")
        sair = input(f"\nAperte Enter para sair")
        if sair == "":
            print("")
if __name__ == '__main__':
    main()
    
    
