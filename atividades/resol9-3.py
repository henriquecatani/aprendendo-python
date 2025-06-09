import json 

# variaveis globais
dicionario = dict()

def lerArquivoJson(arquivo):
    try:
        with open(arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    
def gravar(arquivo):
    with open(arquivo, 'w') as arquivo:
        json.dump(dicionario, arquivo, indent=4)

def incluiPalavra(palavra, traducao):
    if palavra in dicionario:
        return(f"\nA palavra '{palavra}' já existe no dicionário.")
    else:
        dicionario[palavra] = traducao
        return(f"\nA palavra '{palavra}' com tradução '{traducao}' foi incluída no dicionário.")

def listaPalavras():
    if not dicionario:
        return("\nO dicionário está vazio.")
    else:
        palavras = "\n"
        for palavra, traducao in dicionario.items():
            palavras += f"{palavra}: {traducao} \n"
        return palavras

def alteraTraducao(palavra, traducao):
    if palavra in dicionario:
        dicionario[palavra] = traducao
        return(f"\nA tradução da palavra '{palavra}' foi alterada para '{traducao}'.")
    else:
        return(f"\nA palavra '{palavra}' não existe no dicionário.")

def removePalavra(palavra):
    if palavra in dicionario:
        dicionario.pop(palavra)
        return(f"\nA palavra '{palavra}' foi removida do dicionário.")
    else:
        return(f"\nA palavra '{palavra}' não existe no dicionário.")

def traduzir(palavra):
    return dicionario.get(palavra, f"\nA palavra '{palavra}' não existe no dicionário.")

def main() :
    global dicionario # permite acesso à variavel global
    dicionario = lerArquivoJson("dicionario.json") # busca dados no arquivo json
    
    # print(type(dicionario))
    menu = "\nDicionario\n1.Incluir\n2.Alterar\n3.Excluir\n4.Traduzir\n5.Listar\n9.Sair"
    
    while True :
        print(menu)
        try :
            opcao = int(input("Informe sua opcao: "))
        except :
            print("\nErro! Informe um número entre 1-5 ou 9 para sair")
            continue
        match opcao :
            case 1 :
                palavra = input("Informe palavra para adicionar: ")
                traducao = input("Informe traducao: ")
                print(incluiPalavra(palavra, traducao))
            case 2 :
                palavra = input("Informe palavra a alterar: ")
                traducao = input("Informe traducao: ")
                print(alteraTraducao(palavra, traducao))
            case 3 :
                palavra = input("Informe palavra a remover: ")
                print(removePalavra(palavra))
            case 4 :
                palavra = input("Informe palavra a traduzir: ")
                print(traduzir(palavra))
            case 5 :
                print(listaPalavras())
            case 9 :
                print("Finalizando")
                gravar("dicionario.json")
                break
  
# programa principal
main()