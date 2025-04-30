# Algoritmos e Programação - Lista de exercícios 4
# Aluno: Henrique Catani


a = input(f'Digite uma frase, palavra, etc.:\n> ')
qtdCaracteres = len(a)
print('1- Quantidade de caracteres:', qtdCaracteres)

primCar, ultCar = a[0], a[-1]
print(f'2- Primeiro caractere: "{primCar}", Último caractere: "{ultCar}"')

posCharInicio = int(input('Informe a posição de um caractere a partir do início: '))
posCharFim = int(input('Informe a posição de um caractere a partir do fim: '))
print(f'3- Caractere {posCharInicio} a partir do início: "{a[posCharInicio]}"\n4- Caractere {posCharFim} a partir do final: "{a[-posCharFim]}"')

maiusculo = a.upper()
print(f'5- Tudo em maiúsculo:\n{maiusculo}')

minusculo = a.lower()
print(f'6- Tudo em minúsculo:\n{minusculo}')

subst, substPor = input('O que substituir? '), input('Pelo que substituir? ') 
print(f'7- Substituindo "{subst}" por "{substPor}":', a.replace(subst,substPor))

frase = "A ligeira raposa marrom ataca o cão preguiçoso"
palavras = frase.split()
qtdPlvs = 0
for j in palavras:
    qtdPlvs += 1
print(f'8- A frase "{frase}" tem {qtdPlvs} palavras')

seqChar = input('Diga uma sequência de caracteres: ')
if seqChar not in a:
    verSeq = "não"
else:
    verSeq = "" # a frase a seguir fica "A sequência se encontra"
print(f'9- A sequência de caracteres "{seqChar}" {verSeq} se encontra na frase lida')

seqChar = input('Diga uma sequência de caracteres: ')
print('10-',a+seqChar)

seqChar = input('Diga uma sequência de caracteres: ')
cont = a.count(seqChar)
print(f'11- A sequência de caracteres "{seqChar}" se encontra {cont} {"vez" if cont == 1 else "vezes"} na frase lida.')

char = input('Diga um caractere: ')
print(f'12- O caractere "{char}" primeiro se encontra na posição {a.find(char)} da frase lida.')

alfabetico = 0
for k in a:
    if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122 or ord(k) == 32:
        alfabetico = 1
    else:
        alfabetico = 0
        break
if alfabetico == 1:
    print('13- A frase lida é composta somente de caracteres alfabéticos')
    print('14- A frase lida NÃO é composta somente de caracteres numéricos') # outro calculo seria redundante
else:
    print('13- A frase lida NÃO é composta somente de caracteres alfabéticos')

    # fora deste else, o calculo seria redundante
    numerico = 0
    for k in a:
        if 48 <= ord(k) <= 57 or ord(k) == 32:
            numerico = 1
        else:
            numerico = 0
            break
    if numerico == 1:
        print('14- A frase lida é composta somente de caracteres numéricos')
    else:
        print('14- A frase lida NÃO é composta somente de caracteres numéricos')

palavrasA = a.split()
print(f'A frase lida em formato de título: ', end='')
for l in palavrasA:
    print(l.capitalize(), end=' ') # reescreve a frase capitalizando todas as palavras
print()

print(f'Aluno: Henrique Catani\nFim!')
