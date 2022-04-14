class Circulo:
    pi = 3.14

    def calcular_area(self):
        return self.pi * self.raio * self.raio

    def calcular_perimetro(self):
        return 2 * self.pi * self.raio


circulo1 = Circulo()
circulo2 = Circulo()

circulo1.raio = float(input("Digite o valor do raio: "))

print(circulo1.calcular_area())
print(circulo1.calcular_perimetro())

circulo2.raio = float(input("Digite o valor do raio: "))

print(circulo2.calcular_area())
print(circulo2.calcular_perimetro())