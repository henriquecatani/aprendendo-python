import json

dicionario = dict()

def lerArquivoJson(arquivo):
    try:
        with open(arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    
