# aprendendo Programação orientada a Objetos
# codigo A

class Computador:
    def __init__(self, nome, ram, espacoDisco, cpu, gpu):
        self.nome = nome
        self.ram = ram
        self.espacoDisco = espacoDisco
        self.cpu = cpu
        self.gpu = gpu
    def imprima(self):
        print("Nome:", self.nome)
        if self.mesesUso == 0:
            print('Estado: Novo')
        elif self.mesesUso < 6:
            print('Estado: Semi-novo')
        else:
            print('Estado: Usado')
        print(f'Memória RAM: {self.ram}GB')
        print(f'Espaço em Disco: {self.espacoDisco}GB')
        print('Processador:', self.cpu)
        print('Placa de Vídeo:', self.gpu)
    def tempoUso(self, meses):
        if meses > 0:
            self.mesesUso = meses
        else:
            self.mesesUso = 0 
def adicionarComputador(listaPcs):
    x = len(listaPcs)
    listaPcs.append(x)
    nome = input('Digite o nome do computador: ')
    meses = int(input('Quantos meses de uso este computador tem? '))
    ram = int(input('Digite a quantidade de RAM do computador, em GB: '))
    espaco = int(input('Digite a quantidade de espaço em disco, em GB: '))
    cpu = input('Digite o modelo do processador: ')
    gpu = input('Digite o modelo da placa de vídeo: ')
    print('Adicionado!')  
    pc = listaPcs[x] = Computador(nome, ram, espaco, cpu, gpu)
    pc.tempoUso(meses)
    pc.imprima()
    return listaPcs
def main():
    listaComps = []
    add = 1
    while add != 0:
        add = int(input('Adicionar computador ao registro? (1/0)'))
        if add != 0:
            listaComps = adicionarComputador(listaComps)
    for computador in listaComps:
        computador.imprima()
    print('Quantidade de computadores adicionados: ', len(listaComps))

main()

