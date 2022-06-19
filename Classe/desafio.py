

class Carro:
    def __init__(self, concessionaria, cor, modelo):
        self.concessionaria = concessionaria
        self.cor = cor
        self.modelo = modelo

    def Ligar(self):
        print('Estou andando')

    def Desligar(self):
        print('Estou parado')

    def ExibirInformacoesDoCarro(self):
        print(self.concessionaria, self.cor, self.modelo)


Carro1 = Carro('Poshe', 'Preto', '911')     # instância
Carro1.Ligar()
Carro1.Desligar()
Carro1.ExibirInformacoesDoCarro()
