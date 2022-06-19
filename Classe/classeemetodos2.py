"""
Neste primeiro não é a melhor forma de se fazer, pois a classe tem que ser dinâmica
Se modelando a uma situação, onde ele está sendo usada, então seria incorreto deixar 
as suas fixadas """""


# Primeiro Exemplo (Usando Class/Forma incorreta):
class Computador:
    def __init__(self):  # Construtor (serve para acessar as propriedades ou metodos de uma instância)
        self.marca = 'Asus'
        self.memoria_ram = '8gb'
        self.placa_de_video = 'Nvidia'

    pass


computador1 = Computador()
computador2 = Computador()
computador3 = Computador()

print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_de_video)

print()

# Segundo Exemplo (Usando Class/ forma correta):


class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass


computador1 = Computador('Asus', '8gb', 'Nvidia')
computador2 = Computador('Dell', '10gb', 'GeForce')
computador3 = Computador('Acer', '16gb', 'ATM')

print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_de_video)

