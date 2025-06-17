# Questao: soma dos elementos de duas listas

def somaListas(lista1, lista2):
    listaSomada = []

    i = 0
    try:
        for n in lista1:
            n = float(n)
            listaSomada.append(n)
            listaSomada[-1] += float(lista2[i])
            i += 1               
        return listaSomada
    except IndexError:
        return('Listas inválidas: as listas devem ter o mesmo tamanho!')
    except:
        return('Listas inválidas.')
print('Aluno: Henrique Catani\n\
Programa: somaListas \n\
Faz a soma dos elementos de duas listas do mesmo tamanho.\n')
lista1 = (input('Digite a primeira lista de números, separados por espaços (ex.: 1 2 3 4): ').strip()).split(' ')
lista2 = (input('Digite a primeira lista de números, separados por espaços, do mesmo tamanho que a primeira: ').strip()).split(' ')
print(somaListas(lista1, lista2))