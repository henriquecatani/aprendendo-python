# Algoritmos e Programação - Lista de exercícios 6
# Aluno: Henrique Catani
# Exercício 1
opcoes = {
    1 : 'Adicionar item',
    2 : 'Remover item',
    3 : 'Exibir todos itens',
    4 : 'Ordenar alfabeticamente',
    5 : 'Verificar se um item está na lista',
    6 : 'Gravar lista em um arquivo',
    7 : 'Ler lista',
    8 : 'Sair do programa'
}
print('Digite uma opção para gerenciar a lista de compras: ')
for k, l in opcoes.items():
    print(f'{k} - {l}')

while n != 8:
    n = int(input('Opção: '))
    listaCompras = {}
    match n:
        case 1: # add
            item = input('Digite o item a ser adicionado: ')
            if item in listaCompras:
                print('Item já foi adicionado!')
            listaCompras.add(item)
        case 2: # remove
            item = input('Digite o item a ser removido: ')
            listaCompras.remove(item)
        case 3: # exibir
            print('Lista de compras: ')
            for j in listaCompras:
                print(f'- {j}')
        case 4: # ordenar
            print()
        case 5: # existe ou n
            item = input('Digite um item a ser pesquisado: ')
            if item in listaCompras:
                print(f'{item} está na lista!')
            else:
                print(f'{item} não está na lista.')
        case 8:
            break


            
