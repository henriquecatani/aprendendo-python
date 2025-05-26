# Algoritmos e Programação - Lista de exercícios 7
# Aluno: Henrique Catani
# Exercício 2
opcoes = {
    1 : 'União entre conjuntos',
    2 : 'Interseção entre conjuntos',
    3 : 'Diferença entre conjuntos',
    4 : 'Obter o tamanho do conjunto',
    5 : 'Obter o valor máximo e mínimo do conjunto',
    6 : 'Sair do programa'
}
def criaConjuntos():
    set1 = set(map(int, input('Digite um conjunto separado por vírgulas (ex.: 1,2,3): ').split(',')))
    set2 = set(map(int, input('Digite um conjunto separado por vírgulas (ex.: 1,2,3): ').split(',')))
    return set1,set2
n = 0
run1 = True
set1, set2 = set(), set()
while n != 6:
    if n != 0:
        print('Digite 0 para exibir as opções')
        n = int(input('Opção: '))
    match n:
        case 0: # exibir menu
            print(f'Digite uma opção para manipular conjuntos: ')
            for k, l in opcoes.items():
                print(f'{k} - {l}')
            n = 10
        case 1: 
            if run1 == False:
                r = input('Deseja usar os conjuntos digitados por último?')
                r.lower()
                if r not in ['y', 's', 'sim']:
                    set1 , set2 = criaConjuntos()
            else:
                set1 , set2 = criaConjuntos()
            run1 = False
            print(set1 | set2)
        case 2:
            if run1 == False:
                r = input('Deseja usar os conjuntos digitados por último? (s/N) ')
                r.lower()
                if r not in ['y', 's', 'sim']:
                    set1 , set2 = criaConjuntos()
            else:
                set1 , set2 = criaConjuntos()
            run1 = False
            print(set1 & set2)
        case 3:
            if run1 == False:
                r = input('Deseja usar os conjuntos digitados por último?')
                r.lower()
                if r not in ['y', 's', 'sim']:
                    set1 , set2 = criaConjuntos()
            else:
                set1 , set2 = criaConjuntos()
            run1 = False
            print(set1 - set2)
        case 4:
            if run1 == False:
                r = input('Deseja usar os conjuntos digitados por último?')
                r.lower()
                if r not in ['y', 's', 'sim']:
                    set1 , set2 = criaConjuntos()
            else:
                set1 , set2 = criaConjuntos()
            run1 = False
            print(f'Tamanho da primeira: {len(set1)}\nTamanho da Segunda: {len(set2)}')
        case 5:
            if run1 == False:
                r = input('Deseja usar os conjuntos digitados por último?')
                r.lower()
                if r not in ['y', 's', 'sim']:
                    set1 , set2 = criaConjuntos()
            else:
                set1 , set2 = criaConjuntos()
            run1 = False
            print(f'Máximo da primeira: {max(set1)}\nMáximo da Segunda: {max(set2)}')
            print(f'Mínimo da primeira: {min(set1)}\nMínimo da Segunda: {min(set2)}')
    
