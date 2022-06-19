class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):    # def = metodo 
        print(self.ano_atual - self.idade)  # self = instância


pessoa1 = Pessoa('Kevin Richard', 20)
print(pessoa1.ano_atual)

