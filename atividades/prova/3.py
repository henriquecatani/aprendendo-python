# Questao 3: abre arquivo com 7 registros de temperatura por cidade, uma cidade por linha,
# e devolve em um novo arquivo a cidade com a maior média e alguns dados

def abreArquivoDeLista(arquivo):
    try:
        arquivoAberto = []
        with open(arquivo, 'r', encoding='utf-8') as f:
            cnt = 0
            for linha in f:
                linha = linha.split(',')
                arquivoAberto.append([])
                for x in linha:
                    x = x.strip()
                    arquivoAberto[cnt].append(x)
                cnt += 1
        return arquivoAberto
    except FileNotFoundError:
        return False

def salvaArquivoDeLista(arquivo, valores):
    try:
        with(open(arquivo, 'x', encoding='utf-8')) as f:
            f.write(k)
            for k in valores[1:]:
                f.write(',{}'.format(k))
    except FileExistsError:
        with(open(arquivo, 'w', encoding='utf-8')) as f:
            f.write(valores[0])
            for k in valores[1:]:
                f.write(',{}'.format(k))
    return

def media(valores):
    soma = 0
    for n in valores:
        soma += n
    return soma/len(valores)

print('Aluno: Henrique Catani\n\
Programa: temperaturasSemanais \n\
Faz cálculos com temperaturas de cidades, lendo o arquivo temperaturas.txt e escrevendo no arquivo maiorMedia.txt.\n')

aberto = abreArquivoDeLista('temperaturas.txt')
if aberto != False:
    maiorCidade = 0
    maiorMedia = 0
    nCidade = 0
    menorTemp = []
    maiorTemp = []
    for cidade in aberto:
        menorTemp.append(100)
        maiorTemp.append(0)
        soma = 0
        for temp in cidade[1:]:
            temp = int(temp)
            soma += temp
            if temp < menorTemp[-1]:
                menorTemp[-1] = temp
            elif temp > maiorTemp[-1]:
                maiorTemp[-1] = temp
        m = soma/7
        if m > maiorMedia:
            maiorMedia = m
            maiorCidade = nCidade
        nCidade += 1
    final = [aberto[maiorCidade][0], maiorMedia, maiorTemp[maiorCidade]]
    salvaArquivoDeLista('maiorMedia.txt', final)
else:
    print('Arquivo temperaturas.txt não foi encontrado!')