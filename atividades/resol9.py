def cntLetras(frase):
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
    for j,k in cnt.items():
        yield '{}: {}'.format(j, k)

frase = input("Digite uma frase para contar as letras: ")
resultado_contagem = cntLetras(frase)
print("Contagem de letras:")
for l in resultado_contagem:
    print(l)
# for letra, quantidade in resultado_contagem.items():
    # print(f"{letra}: {quantidade}")