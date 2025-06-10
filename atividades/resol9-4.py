# definicao de variaveis globais
usuarios = {}

def criarUsuario(codigo, nome, email, idade) :
    # verifica se ja tem usuario com o codigo informado
    if codigo in usuarios :
        print("Erro: Codigo do usuario ja existe! ")
        return
    else :
        # percorre o dicionario verificando se o email ja existe
        for usuario in usuarios.values() :
            if usuario["email"] == email :
                print("Erro: e-mail ja cadastrado ")
                return
    usuarios[codigo] = {"nome": nome, "email": email, "idade": idade }
    print("\nUsuario cadastrado com sucesso")

def lerUsuario(codigo) :
    if codigo not in usuarios :
        print("Erro: Usuario nao encontrado! ")
        return
    usuario = usuarios[codigo]
    print(f"Codigo:{codigo}, Nome: {usuario['nome']}, E-mail:{usuario['email']}, Idade:{usuario['idade']}")

def atualizarUsuario(codigo, nome, email, idade) :
    if codigo not in usuarios :
        print("Erro: Codigo do usuario nao existe! ")
        return
    else :
        usuarios[codigo] = {"nome": nome, "email": email, "idade": idade }
        print("\nUsuario atualizado com sucesso")

def deletaUsuario (codigo) :
    if codigo not in usuarios :
        print("Erro: Codigo do usuario nao existe! ")
        return
    else :
        usuarios.pop(codigo)
        print("\nUsuario removido com sucesso")
        
def listaUsuarios() :
    if not usuarios :
        print("\nDicionario vazio")
        return
    for codigo, usuario in usuarios.items() :
        print(f"Codigo: {codigo}, Nome: {usuario['nome']}, E-mail:{usuario['email']}, Idade: {usuario['idade']}")

# funcao principal
def main() :
    while True :
        print("\nMenu")
        print("1. Criar usuario")
        print("2. Ler usuario")
        print("3. Atualizar usuario")
        print("4. Deletar usuario")
        print("5. Listar todos usuarios")
        print("6. Sair")
        opcao = input("Escolha sua opcao: ")
        
        if opcao == "1" :
            codigo = input("Digite o codigo do usuario: ")
            nome = input("Digite o nome do usuario: ")
            email = input("Digite o email do usuario: ")
            idade = input("Digite a idade do usuario: ")
            criarUsuario(codigo, nome, email, idade)
        elif opcao == "2" :
            codigo = input("Digite o codigo do usuario: ")
            lerUsuario(codigo)
        elif opcao == "3" :
            codigo = input("Digite o codigo do usuario: ")
            nome = input("Digite o nome do usuario: ")
            email = input("Digite o email do usuario: ")
            idade = input("Digite a idade do usuario: ")
            atualizarUsuario(codigo, nome, email, idade)            
        elif opcao == "4" :
            codigo = input("Digite o codigo do usuario: ")
            deletaUsuario(codigo)
        elif opcao == "5" :
            listaUsuarios()
        elif opcao == "6" :
            print("saindo ...")
            break
# programa principal
main ()