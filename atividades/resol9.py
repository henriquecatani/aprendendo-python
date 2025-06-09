def cntLetras(frase): # questao 1
    cnt = {}
    # percorre todas as posicoes das string
    for letra in frase:
        # testa se o caractere e valido
        if letra.isalpha():
            letra = letra.upper()
            # testa de letra ja esta sendo contada
            if letra in cnt :
                cnt[letra] += 1
            else :
                cnt[letra] = 1
    yield "Contagem de letras:"
    for j,k in cnt.items():
        yield '{}: {}'.format(j, k)
    
def cntPalavras(arquivo): # questao 2
    cnt = {}
    v = True
    try:
        with open(arquivo, "r", encoding="UTF-8") as f:
            for linha in f:
                palavras = linha.split()
                for palavra in palavras:
                    palavra = palavra.strip('\n').lower()
                    cnt[palavra] = cnt.get(palavra,0) +1
        return cnt, v
    except FileNotFoundError:
        v = False
        return "Arquivo não encontrado!", v

def main():
    funcoes = {
        1 : "cntLetras",
        2 : "cntPalavras",
        3 : "tipoTriangulo",
        4 : "estadoBR",
        5 : "ordemCrescente",
        6 : "ehPrimo",
        0 : "Sair"
        }
    print(f"Atividades de Algoritmos e Programação 8.\n Aluno: Henrique Catani\n \nSelecione a atividade:") 
    for k, l in funcoes.items():
        print(k, " - ", l)
    escolha = int(input("Opção: "))
    def submenu():
        continuar = input("Aperte Enter para voltar ao menu ")
        if continuar == "": # se somente apertar enter
            main()
    match escolha:
        case 1:
            frase = input("Digite uma frase para contar as letras: ")
            resultado_contagem = cntLetras(frase)
            for l in resultado_contagem:
                print(l)
            submenu()
        case 2:
            x = input('Digite o nome do arquivo: ')
            plvs, valido = cntPalavras(x)
            
            if valido:
                print('Palavras | Quantidade')
                for a,b in plvs.items(): # type: ignore
                    print(f'{a}: {b}')
            else:
                print(plvs)
        case 0:
            print(f"Obrigado por usar o programa!\nass. Henrique Catani")
            sair = input(f"\nAperte Enter para sair")
            if sair == "":
                print("")
if __name__ == '__main__':
    main()