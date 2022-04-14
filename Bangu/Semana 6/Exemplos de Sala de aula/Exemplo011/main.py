class Circulo:
  pi = 3.14
  def calcular_area(self, raio):
    return self.pi*raio*raio

  def calcular_perimetro(self, raio):
    return 2*self.pi*raio

circulo = Circulo()

print(circulo.calcular_area(10))
print(circulo.calcular_perimetro(10))