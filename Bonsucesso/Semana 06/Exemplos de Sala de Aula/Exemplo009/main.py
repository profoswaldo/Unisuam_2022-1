class Circulo:

    def calcular_area(self, pi, raio):
        return pi * raio * raio

    def calcular_perimetro(self, pi, raio):
        return 2 * pi * raio


raio = float(input("Digite o valor do raio: "))
pi = 3.14

circulo = Circulo()

print(circulo.calcular_area(pi, raio))
print(circulo.calcular_perimetro(pi, raio))
