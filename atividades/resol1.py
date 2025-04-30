# Algoritmos e Programação - Lista de exercícios 1
# Aluno: Henrique Catani

def mediaNotas(nota_1, nota_2, nota_3):
    mediaPonderada = (nota_1 * 3 + nota_2 * 5 + nota_3 * 2)/10
    return "Média: {}".format(mediaPonderada)

def operacoes(a, b):
    soma = a+b
    subtracao = a - b
    divisao = a/b
    multiplicacao = a*b
    return "Soma: {}, Subtração: {}, Divisão: {}, Multiplicação: {}".format(soma, subtracao, divisao, multiplicacao)

def conversaoCelsiusKelvin(temp_c):
    temp_k = temp_c + 273
    return "{} K".format(temp_k)

def conversaoRealDolar(cotacaoDolar, valorReal):
    valorDolar = valorReal * cotacaoDolar
    return "{} dólares".format(valorDolar)

def qtdCerveja(qtdCaixas):
    qtdTotal = (int(qtdCaixas) * 24 * 600)/1000
    return "{} litros".format(qtdTotal)

def valorCamisetas(qtdPequeno, qtdMedio, qtdGrande):
    valor = qtdPequeno * 10 + qtdMedio * 12 + qtdGrande * 15
    return "{} Reais".format(valor)

def converteTempo(qtdDias):
    qtdAnos = qtdDias // 365
    qtdDias = qtdDias - 365 * qtdAnos
    qtdMeses = qtdDias // 30
    qtdDias = qtdDias - 30 * qtdMeses
    return "{} anos, {} meses e {} dias".format(int(qtdAnos), int(qtdMeses), int(qtdDias))

def main():
    funcoes = {
        1 : "mediaNotas",
        2 : "operacoes",
        3 : "conversaoCelsiusKelvin",
        4 : "conversaoRealDolar",
        5 : "qtdCerveja",
        6 : "valorCamisetas",
        7 : "converteTempo",
        0 : "Sair"
        }
    print(f"Atividades de Algoritmos e Programação.\n Aluno: Henrique Catani\n \nSelecione a atividade:") 
    for k, l in funcoes.items():
        print(k, " - ", l)
    escolha = int(input("Opção: "))
    def submenu():
        continuar = input("Aperte Enter para voltar ao menu ")
        if continuar == "": # se somente apertar enter
            main()
    if escolha == 1:
        n1 = float(input("Diga a nota da primeira prova: "))
        n2 = float(input("Diga a nota da segunda prova: "))
        n3 = float(input("Diga a nota dos trabalhos: "))
        print(mediaNotas(n1, n2, n3))
        submenu()
    if escolha == 2:
        n1 = float(input("Diga o primeiro número: "))
        n2 = float(input("Diga o segundo número: "))
        print(operacoes(n1, n2))
        submenu()
    if escolha == 3:
        c = float(input("Diga a temperatura em Celsius: "))
        print(conversaoCelsiusKelvin(c))
        submenu()
    if escolha == 4:
        n1 = float(input("Diga a cotação do dólar: "))
        n2 = float(input("Diga o valor em real: "))
        print(conversaoRealDolar(n1, n2))
        submenu()
    if escolha == 5:
        c = float(input("Diga a quantidade de caixas de cerveja: "))
        print(qtdCerveja(c).format())
        submenu()
    if escolha == 6:
        n1 = float(input("Diga a quantidade de camisetas pequenas: "))
        n2 = float(input("Diga a quantidade de camisetas médias: "))
        n3 = float(input("Diga a quantidade de camisetas grandes: "))
        print(valorCamisetas(n1, n2, n3))
        submenu()
    if escolha == 7:
        d = float(input("Diga a quantidade de dias: "))
        print(converteTempo(d))
        submenu()
    if escolha == 0:
        print(f"Obrigado por usar o programa!\nass. Henrique Catani")
        sair = input(f"\nAperte Enter para sair")
        if sair == "":
            print("")
if __name__ == '__main__':
    main()
