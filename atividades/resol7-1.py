# Algoritmos e Programação - Lista de exercícios 6
# Aluno: Henrique Catani
# Exercício 1

from time import sleep
print(f"Atividades de Algoritmos e Programação 7, Exercício 1.\n Aluno: Henrique Catani") 
def abreArquivo():
    listaCompras = set()
    listaLocal = False # verificação se o arquivo foi criado por este programa
    aberto = input('Diga o nome do arquivo a ser aberto (padrão: lista.txt). Se o arquivo não existe, será criado.\n> ')
    if aberto == '':
        aberto = "lista.txt"
    try:
        f = open(aberto, "x") # tenta criar o arquivo
        print(f'{aberto} não foi encontrado no diretório! Criando arquivo...')
        listaLocal = True
        f.close()
    except FileExistsError: # se o arquivo existir, lê ele para a lista
        print(f'{aberto} encontrado no diretório! Lendo arquivo...')
        listaLocal = True
        with open(aberto, "r") as f:
            linha1 = True
            for linha in f:
                linha = linha.strip()
                if linha1 and linha == 'Lista criada pelo criador de listas de Henrique Catani':
                    listaLocal = True    
                    linha1 = False        
                elif linha:
                    listaCompras.add(linha)
                elif linha1:
                    linha1 = False
                
    if listaLocal == False:
        sleep(0.5)
        print(f'Atenção: o arquivo {aberto} encontrado no diretório NÃO foi criado usando este programa.')
    return listaCompras, aberto
aberto = ''
listaCompras = set()
listaCompras, aberto = abreArquivo()

opcoes = {
    1 : 'Adicionar itens',
    2 : 'Remover item',
    3 : 'Exibir todos itens',
    4 : 'Ordenar alfabeticamente',
    5 : 'Verificar se um item está na lista',
    6 : 'Salvar arquivo',
    7 : 'Abrir outro arquivo',
    8 : 'Apagar todos itens',
    9 : 'Sair do programa'
}



sleep(1)
n = 0
while n != 9:
    
    if n != 0:
        sleep(1)
        print('Digite 0 para exibir as opções')
        n = int(input('Opção: '))
    match n:
        case 0: # exibir menu
            
            print(f'\nLista aberta: {aberto}')
            print(f'Digite uma opção para gerenciar a lista de compras: ')
            for k, l in opcoes.items():
                print(f'{k} - {l}')
            n = 10
        case 1: # add
            item = 'a'
            while item != '':
                item = input('Digite o item a ser adicionado (vazio para parar de adicionar): ')
                if item == '':
                    break
                if item in listaCompras:
                    print('Item já foi adicionado!')
                else:
                    listaCompras.add(item)
        case 2: # remove
            try:
                item = input('Digite o item a ser removido: ')
                listaCompras.remove(item)
            except KeyError:
                print('Item não existe na lista!')
        case 3: # exibir
            print('Lista de compras: ')
            for j in listaCompras:
                print(f'- {j}')
        case 4: # ordenar
            ordenada = sorted(listaCompras)
            for item in ordenada:
                print('-', item)
        case 5: # existe ou n
            item = input('Digite um item a ser pesquisado: ')
            if item in listaCompras:
                print(f'{item} está na lista!')
            else:
                print(f'{item} não está na lista.')
        case 6: # salvar
            with open(aberto, "w") as f:
                if len(listaCompras) > 0: # watermark para verificação se o arquivo foi criado aqui
                    f.write('Lista criada pelo criador de listas de Henrique Catani')
                    for k in listaCompras:
                        f.write('\n{}'.format(k))
                else:
                    f.write('')
            sleep(1)
            print(f'Arquivo {aberto} foi salvo.')
        case 7: # ler arquivo
            print(f'Arquivo aberto atualmente: {aberto}')
            listaCompras, aberto = abreArquivo()
        case 8:
            escolha = input('Você quer mesmo apagar todos os itens da lista? (s/N) ')
            if escolha in ['y','s','sim','S','Sim']:
                listaCompras = set()
                print('Os itens da lista foram apagados.')
            else:
                print('A lista foi mantida.')
        case 9:
            print(f"Obrigado por usar o programa!\nass. Henrique Catani")
            sair = input(f"\nAperte Enter para sair")
            if sair == "":
                print("")


            
