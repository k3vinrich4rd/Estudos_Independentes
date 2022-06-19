class Retangulo:
    def __init__(self, b, h):   # metodo construtor
        self.b = b
        self.h = h

    def CalcularAreaDoperimetro(self):
        return f'O resultado do Calculo do Perimetro é: {self.b * self.h}'

    def CalcularPerimetro(self):
        return f'O resultado do Calculo do Perimetro é: {self.b * 2 + self.h * 2}'


r1 = Retangulo(20, 5)
print(r1.CalcularAreaDoperimetro())
print(r1.CalcularPerimetro())
