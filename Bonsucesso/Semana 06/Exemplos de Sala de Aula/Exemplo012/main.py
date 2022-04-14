class Circulo:
    pi = 3.14

    def inicializar(self, raio):
        self.raio = raio

    def calcular_area(self):
        return self.pi * self.raio * self.raio

    def calcular_perimetro(self):
        return 2 * self.pi * self.raio


circulo1 = Circulo()
circulo2 = Circulo()

circulo1.inicializar(10)
circulo2.inicializar(20)

print(circulo1.calcular_area())
print(circulo1.calcular_perimetro())

print(circulo2.calcular_area())
print(circulo2.calcular_perimetro())