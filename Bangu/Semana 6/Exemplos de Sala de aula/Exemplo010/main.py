class Circulo:
  def calcular_area(self, raio):
    self.pi = 3.14
    return self.pi*raio*raio

  def calcular_perimetro(self, raio):
    self.pi = 3.14
    return 2*self.pi*raio

circulo = Circulo()

print(circulo.calcular_area(10))
print(circulo.calcular_perimetro(10))