# Algoritmos e Programação - Lista de exercícios 3
# Aluno: Henrique Catani

def cardapio(codigo,qtd):
    if codigo == 10:
        custo = 1.10 * qtd
        return '{}x Cachorro quente: {} Reais'.format(qtd, custo)
    elif codigo == 11:
        custo = 1.30 * qtd
        return '{}x Bauru simples: {} Reais'.format(qtd, custo)
    elif codigo == 12:
        custo = 1.50 * qtd
        return '{}x Bauru com ovo: {} Reais'.format(qtd, custo)
    elif codigo == 13:
        custo = 1.10 * qtd
        return '{}x Hamburguer: {} Reais'.format(qtd, custo)
    elif codigo == 14:
        custo = 1.30 * qtd
        return '{}x Cheeseburger: {} Reais'.format(qtd, custo)
    elif codigo == 15:
        custo = 1.50 * qtd
        return '{}x Refrigerante: {} Reais'.format(qtd, custo)
    else:
        return 'Código inválido'
def valorPassagem(valor,qtd):
    valorEstudante = valor * 0.6
    if qtd > 50:
        valorFinal = (qtd - 50) * valor + 50 * valorEstudante
        return 'Valor da passagem: {}, Valor a ser pago: {}'.format(valorEstudante, valorFinal)
    else:
        valorFinal = qtd * valorEstudante
        return 'Valor da passagem: {}, Valor a ser pago: {}'.format(valorEstudante, valorFinal)
def saoMultiplos(a,b):
    if 0 in (a,b) == 0:
        return 'Não são múltiplos'
    elif a % b == 0 or b % a == 0:
        return 'São múltiplos'
    else:
        return 'Não são múltiplos'
def signo(nome, dia, mes):
    
    if mes == 1 and dia > 20 or mes == 2 and dia < 19:
        return '{}: Aquário'.format(nome)
    elif mes == 2 and dia > 18 or mes == 3 and dia < 21:
        return '{}: Peixes'.format(nome)
    elif mes == 3 and dia > 20 or mes == 4 and dia < 21:
        return '{}: Áries'.format(nome)
    elif mes == 4 and dia > 20 or mes == 5 and dia < 22:
        return '{}: Touro'.format(nome)
    elif mes == 5 and dia > 21 or mes == 6 and dia < 22:
        return '{}: Gêmeos'.format(nome)
    elif mes == 6 and dia > 21 or mes == 7 and dia < 23:
        return '{}: Câncer'.format(nome)
    elif mes == 7 and dia > 22 or mes == 8 and dia < 24:
        return '{}: Leão'.format(nome)
    elif mes == 8 and dia > 23 or mes == 9 and dia < 23:
        return '{}: Virgem'.format(nome)
    elif mes == 9 and dia > 22 or mes == 10 and dia < 24:
        return '{}: Libra'.format(nome)
    elif mes == 10 and dia > 23 or mes == 11 and dia < 23:
        return '{}: Escorpião'.format(nome)
    elif mes == 11 and dia > 22 or mes == 12 and dia < 22:
        return '{}: Sagitário'.format(nome)
    elif mes == 12 and dia > 21 or mes == 1 and dia < 20:
        return '{}: Capricórnio'.format(nome)
    else:
        return 'Data inválida'

def maisVelho(nome1, n1, nome2, n2, nome3, n3):
    if n1 == n2 or n1 == n3 or n2 == n3:
        return "As idades são iguais!"
    else:
        if n1 < n2 and n1 < n3:
            nomeMenor, menor = nome1, n1
            if n2 < n3:
                nomeMaior, maior = nome3, n3
            else:
                nomeMaior, maior = nome2, n2
        elif n2 < n1 and n2 < n3:
            nomeMenor, menor = nome2, n2
            if n1 < n3:
                nomeMaior, maior = nome3, n3
            else:
                nomeMaior, maior = nome1, n1
        else:
            nomeMenor, menor = nome3, n3
            if n1 < n2:
                nomeMaior, maior = nome2, n2
            else:
                nomeMaior, maior = nome1, n1
    return "Mais velha: {} - {} anos, Mais nova: {} - {} anos".format(nomeMaior, maior, nomeMenor, menor)

def main():
    funcoes = {
        1 : "cardapio",
        2 : "valorPassagem",
        3 : "saoMultiplos",
        4 : "signo",
        5 : "maisVelho",
        0 : "Sair"
        }
    print(f"Atividades de Algoritmos e Programação 3.\n Aluno: Henrique Catani\n \nSelecione a atividade:") 
    for k, l in funcoes.items():
        print(k, " - ", l)
    escolha = int(input("Opção: "))
    def submenu():
        continuar = input("Aperte Enter para voltar ao menu ")
        if continuar == "": # se somente apertar enter
            main()
    if escolha == 1:
        itens = {
            'código' : "item",
            '    10' : "Cachorro-quente",
            '    11' : "Bauru simples",
            '    12' : "Bauru com ovo",
            '    13' : "Hamburguer",
            '    14' : 'Cheeseburger',
            '    15' : 'Refrigerante'
        }
        for k, l in itens.items():
            print(k, " | ", l)
        n1 = int(input("Diga o código do produto: "))
        n2 = int(input("Diga a quantidade: "))
        print(cardapio(n1, n2))
        submenu()
    if escolha == 2:
        n1 = int(input("Diga o valor normal da passagem: "))
        n2 = int(input("Diga a quantidade: "))
        print(valorPassagem(n1, n2))
        submenu()
    if escolha == 3:
        n1 = int(input("Diga um número inteiro: "))
        n2 = int(input("Diga um número inteiro: "))
        print(saoMultiplos(n1, n2))
        submenu()
    if escolha == 4:
        n1 = input("Diga o nome: ")
        n2 = int(input("Diga o dia de nascimento: "))
        n3 = int(input("Diga o mês de nascimento: "))
        print(signo(n1, n2, n3))
        submenu()
    if escolha == 5:
        n1 = input("Diga o nome da primeira pessoa: ")
        n2 = int(input("Diga a idade da primeira pessoa: "))
        n3 = input("Diga o nome da segunda pessoa: ")
        n4 = int(input("Diga a idade da segunda pessoa: "))
        n5 = input("Diga o nome da terceira pessoa: ")
        n6 = int(input("Diga a idade da terceira pessoa: "))
        print(maisVelho(n1,n2,n3,n4,n5,n6))
        submenu()
    if escolha == 0:
        print(f"Obrigado por usar o programa!\nass. Henrique Catani")
        sair = input(f"\nAperte Enter para sair")
        if sair == "":
            print("")
if __name__ == '__main__':
    main()
    
    
