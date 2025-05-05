# Algoritmos e Programação - Lista de exercícios 6
# Aluno: Henrique Catani

def leEMostraNum(): # exercicio 1
    numeros = []
    n = int(input('Diga um número inteiro, ou 0 para parar: '))
    while n != 0:
        numeros.append(n)
        n = int(input('Diga um número inteiro, ou 0 para parar: '))
    return numeros

def inversoDezFloat(): # exercicio 2
    numeros = []
    i = 0
    while i != 10:
        numeros.append(float(input('Diga um número qualquer: ')))
        i += 1
    numeros.reverse()
    return numeros

def consoantesLidas(): # exercicio 3
    lista = []
    i = 0
    while i != 10:
        letra = input('Diga uma letra: ') 
        if letra not in 'aAeEiIoOu':
            lista.append(letra)
        i += 1
    return '''{} consoantes, {}'''.format(len(lista), lista)

def mediasAcimaDeSete(): # exercicio 4
    nAluno = 0
    medias = []
    aprovados = 0
    n = []
    while nAluno != 10:
        n.append(float(input(f'Diga a primeira nota (de 0 a 10) do aluno {nAluno + 1}: ')))
        n.append(float(input(f'Diga a segunda nota (de 0 a 10) do aluno {nAluno + 1}: ')))
        n.append(float(input(f'Diga a terceira nota (de 0 a 10) do aluno {nAluno + 1}: ')))
        n.append(float(input(f'Diga a quarta nota (de 0 a 10) do aluno {nAluno + 1}: ')))
        medias.append((n[nAluno*4] + n[1+nAluno*4] + n[2+nAluno*4] + n[3+nAluno*4])/4)
        nAluno += 1
    for i in medias:
        if i >= 7:
            aprovados += 1
    return '''Médias: {}, alunos com a média <= 7: {}'''.format(medias,aprovados)

def listaIntercalada(): # exercicio 5
    lista1 = []
    lista2 = []
    lista3 = []
    i = 0
    while i != 10:
        elemento = input('Diga um elemento para a lista 1: ') 
        lista1.append(elemento)
        i += 1
    i = 0
    while i != 10:
        elemento = input('Diga um elemento para a lista 2: ') 
        lista2.append(elemento)
        i += 1
    k = 0
    for j in lista1:
        lista3.append(j)
        lista3.append(lista2[k])
        k += 1
    return lista3

def mediaAnual(): # exercicio 6
    temps = []
    soma = 0
    meses = ['1- Janeiro', '2- Fevereiro',
             '3- Março', '4- Abril',
             '5- Maio', '6- Junho',
             '7- Julho', '8- Agosto',
             '9- Setembro', '10- Outubro',
             '11- Novembro', '12- Dezembro']
    i = 0
    while i != 12:
        tempMensal = float(input(f'Diga a temperatura média do mês {meses[i]}: ')) 
        temps.append(tempMensal)
        soma += tempMensal
        i += 1
    media = soma/12
    k = 0
    l = 0
    print('Meses que excederam a média anual: ')
    for j in temps:
        if j > media:
            print(meses[k], ':', j)
            l += 1
        k += 1
    print('Nenhum mês excedeu a média anual.') if l == 0 else print(end='')
    print('Média anual: ', media)

def crime(): # exercicio 7
    perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
                 "Mora perto da vítima?", "Devia para a vítima?",
                 "Já trabalhou com a vítima?"]
    n = 0
    for i in perguntas:
        resposta = input(f'{i} ("s" ou "n")')
        if resposta == 's':
            n += 1
    match n:
        case 2:
            return 'Suspeita'
        case 3, 4:
            return 'Cúmplice'
        case 5:
            return 'Assassino'
        case _:
            return 'Inocente'
    
def competicao(): # exercicio 8
    n = []
    atleta = input('Diga o nome do atleta: ')
    n.append(atleta)
    maior = 0
    maiorMedia = 0
    cnt = 0
    while atleta != '':
        n.append(float(input(f'Diga a altura do primeiro salto do atleta {atleta}: ')))
        n.append(float(input(f'Diga a altura do segundo salto do atleta {atleta}: ')))
        n.append(float(input(f'Diga a altura do terceiro salto do atleta {atleta}: ')))
        n.append(float(input(f'Diga a altura do quarto salto do atleta {atleta}: ')))
        n.append(float(input(f'Diga a altura do quinto salto do atleta {atleta}: ')))
        media = (n[1 + cnt*6] + n[2 + cnt*6] + n[3 + cnt*6] + n[4 + cnt*6] + n[5 + cnt*6])/5
        print(f'Atleta: {atleta}\nPrimeiro Salto: {n[1 + cnt*6]} m\nSegundo Salto: {n[2 + cnt*6]} m\nTerceiro Salto: {n[3 + cnt*6]} m\nQuarto Salto: {n[4 + cnt*6]} m\n Quinto Salto: {n[5 + cnt*6]} m')
        if media > maiorMedia:
            maiorMedia = media
            maior = cnt
        cnt += 1
        atleta = input('Diga o nome do atleta: ')
        n.append(atleta)
    print('Resultado final: ')
    media1 = (n[1] + n[2] + n[3] + n[4] + n[5])/5
    if maiorMedia == media1:
        print(f'Atleta: {n[0]}')
        maior = 0
    else:
        print(f'Atleta: {n[maior * 6]}')
    print(f'Saltos: {n[1 + maior * 6]} - {n[2 + maior * 6]} - {n[3 + maior * 6]} - {n[4 + maior * 6]} - {n[5 + maior * 6]}')
    print(f'Média dos saltos: {maiorMedia} m')
        
def main():
    funcoes = {
        1 : "leEMostraNum",
        2 : "inversoDezFloat",
        3 : "consoantesLidas",
        4 : "mediasAcimaDeSete",
        5 : "listaIntercalada",
        6 : "mediaAnual",
        7 : "crime",
        8 : "competicao",
        0 : "Sair"
        }
    print(f"Atividades de Algoritmos e Programação 6.\n Aluno: Henrique Catani\n \nSelecione a atividade:") 
    for k, l in funcoes.items():
        print(k, " - ", l)
    escolha = int(input("Opção: "))
    def submenu():
        continuar = input("Aperte Enter para voltar ao menu ")
        if continuar == "": # se somente apertar enter
            main()
    match escolha:
        case 1:
            print(leEMostraNum())
            submenu()
        case 2:
            print(inversoDezFloat())
            submenu()
        case 3:
            print(consoantesLidas())
            submenu()
        case 4:
            print(mediasAcimaDeSete())
            submenu()
        case 5:
            print(listaIntercalada())
            submenu()
        case 6:
            mediaAnual()
            submenu()
        case 7:
            print(crime())
            submenu()
        case 8:
            competicao()
            submenu()
        case 0:
            print(f"Obrigado por usar o programa!\nass. Henrique Catani")
            sair = input(f"\nAperte Enter para sair")
            if sair == "":
                print("")
if __name__ == '__main__':
    main()

