import json

def carregaEstoque(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvaEstoque(estoque, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(estoque, f, indent=4)

def adicionaProduto(estoque, codigo, nome, quantidade):
    if codigo in estoque:
        print("Este código de produto já está em uso.")
    else:
        estoque[codigo] = {'nome': nome, 'quantidade': quantidade}
        print("Produto adicionado ao estoque.")

def atualizaEstoque(estoque, codigo, quantidade):
    if codigo in estoque:
        estoque[codigo]['quantidade'] += quantidade
        print("Estoque atualizado com sucesso.")
    else:
        print("Código de produto não encontrado.")

def exibeEstoque(estoque):
    print("Estoque atual:")
    for codigo, produto in estoque.items():
        print(f"Código: {codigo}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")

def main():
    arquivoEstoque = 'estoque.json'
    estoque = carregaEstoque(arquivoEstoque)

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Produto")
        print("2. Atualizar Estoque")
        print("3. Exibir Estoque")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            adicionaProduto(estoque, codigo, nome, quantidade)
        elif opcao == '2':
            codigo = input("Digite o código do produto: ")
            quantidade = int(input("Digite a quantidade a ser adicionada/subtraída: "))
            atualizaEstoque(estoque, codigo, quantidade)
        elif opcao == '3':
            exibeEstoque(estoque)
        elif opcao == '4':
            salvaEstoque(estoque, arquivoEstoque)
            print("Estoque salvo com sucesso. Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()