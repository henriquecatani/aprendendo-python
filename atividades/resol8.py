# Algoritmos e Programação - Lista de exercícios 8
# Aluno: Henrique Catani

# Exercícios com funções
# Como os algoritmos que faço geralmente são funções, alguns
# foram reutilizados e modificados.

def anoBissexto(ano): # funcao reutilizada da segunda lista de exercicios
    '''
    para uso na função dataValida,
    com base no artigo da Microsoft.
    '''

    if ano % 4 == 0:
        etapa1 = True
    else:
        return False
    if ano % 100 == 0:
        if ano % 400 == 0:
            return True
        else:
            return False
    else:
        return True

def dataValida(dia, mes, ano): # funcao reutilizada da segunda lista de exercicios
    if ano < 0 or ano > 3000:
        return False
    if (dia or mes) < 1:
        return False
    if mes > 12:
        return False
    if anoBissexto(ano): # função separada para organização
        if mes == 2:
            if dia > 29:
                return False
            else:
                return True
    else:
        if mes == 2:
            if dia > 28:
                return False
            else:
                return True
    if mes in (4,6,9,11):
        if dia > 30:
            return False
        else:
            return True
    else: # o resto dos meses, ja que não passaram > 12 no inicio
        if dia > 31:
            return False
        else:
            return True

def formatData(data): # questao 1
    # FORMATO: ddmmyyyy
    try:
        d = data[:2]
        m = data[2:4]
        y = data[4:8]
    except IndexError:
        return 'NULL'
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho',
             'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    try:
        d = int(d)
        m = int(m)
        y = int(y)
    except ValueError:
        return 'NULL'
    if dataValida(d, m, y):
        return '{} de {} de {}'.format(d, meses[m-1], y)
    else:
        return 'NULL'

def converteHoras(hora, min): # questão 2
    if 12 < hora < 24:
        hora = hora - 12
        return '{}:{} PM'.format(hora,min)
    elif hora == 24:
        return '00:{} AM'.format(min)
    elif 0 <= hora <= 12:
        return '{}:{} AM'.format(hora,min)
    else:
        return 'Horário inválido'

def tipoTriangulo(a,b,c): # questão 3 - reutilizada
    if a < b + c and b < a + c and c < a + b: 
        # ^ fórmula que verifica se é triângulo utilizando AND,
        # pois se qualquer uma das condições for falsa, não é um triângulo
        if a == b and b == c:
            return "Triângulo equilátero"
        elif a == b or a == c or c == b:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Não é um triângulo"

def estadoBR(sigla): # questao 4
    estados = {
        'RS': 'Rio Grande do Sul',
        'SC': 'Santa Catarina',
        'PR': 'Paraná',
        'SP': 'São Paulo',
        'MG': 'Minas Gerais',
        'RJ': 'Rio de Janeiro',
        'BA': 'Bahia',
        'PE': 'Pernambuco',
        'CE': 'Ceará',
        'GO': 'Goiás',
        'AM': 'Amazonas',
        'PA': 'Pará',
        'ES': 'Espírito Santo',
        'PB': 'Paraíba',
        'RN': 'Rio Grande do Norte',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'AL': 'Alagoas',
        'PI': 'Piauí',
        'DF': 'Distrito Federal',
        'SE': 'Sergipe',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'TO': 'Tocantins',
        'AC': 'Acre',
        'AP': 'Amapá'
    }
    sigla = sigla.upper()
    if sigla in estados:
        return estados[sigla]
    else:
        return 'Sigla inválida'

def ordemCrescente(a): # questao 5
    a1 = sorted(a)
    if a1 == a:
        return(True)
    else:
        return(False)

def ehPrimo(n): # questao 6 - reutilizada da lista 5
    ''' algoritmo usado: verificar se é divisivel 
        por qualquer numero até a sqrt do numero '''
    if n < 2:
        return False
    i = 2
    while i * i <= n: 
        ''' ^ se cada numero é menor ou 
        igual à raiz do numero inicial '''
        if n % i == 0:
            return False # se for divisivel, não é primo
        i += 1
    return True

def main():
    funcoes = {
        1 : "formatData",
        2 : "converteHoras",
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
            x = input('Digite uma data com o formato ddmmaaaa: ')
            print(formatData(x))
            submenu()
        case 2:
            x = int(input('Digite a hora no formato 24h: '))
            x1 = int(input('Digite os minutos: '))
            print(converteHoras(x, x1))
            submenu()
        case 3:
            x = int(input('Digite o primeiro lado do triângulo: '))
            y = int(input('Digite o segundo lado do triângulo: '))
            z = int(input('Digite o terceiro lado do triângulo: '))
            print(tipoTriangulo(x,y,z))
            submenu()
        case 4:
            x = input('Digite a sigla de um estado Brasileiro: ')
            print(estadoBR(x))
            submenu()
        case 5:
            x = list(map(int, input('Digite uma lista de números separados por uma vírgula (ex.: 1,2,3): ').split(',')))
            print(ordemCrescente(x))
            submenu()
        case 6:
            x = int(input('Digite um número inteiro: '))
            print(ehPrimo(x))
            submenu()
        case 0:
            print(f"Obrigado por usar o programa!\nass. Henrique Catani")
            sair = input(f"\nAperte Enter para sair")
            if sair == "":
                print("")
if __name__ == '__main__':
    main()