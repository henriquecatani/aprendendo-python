palavras = {
    'banana': 'Uma fruta amarela e deliciosa.',
    'python': 'Uma linguagem de programação poderosa.',
    'praia': 'Um lugar com areia e água salgada.',
    'cachorro': 'O melhor amigo do homem.'
}
import random

def jogo():
    palavra = random.choice(list(palavras.keys()))
    dica = palavras[palavra]
    tentativas = 3
    while tentativas > 0:
        print('Dica: ', dica)
        palpite = input('Adivinhe a palavra: ').lower()
        if palpite == palavra:
            print("Parabéns, você acertou!")
            return
        else:
            tentativas -= 1
            print(f"Incorreto! Você tem {tentativas} tentativas restantes.")
    print("Suas tentativas acabaram. A palavra era:", palavra)

jogo()