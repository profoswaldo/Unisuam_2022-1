class Circulo:
  def calcular_area(self, pi, raio):
    return pi*raio*raio

  def calcular_perimetro(self, pi, raio):
    return 2*pi*raio




circulo = Circulo()

print(circulo.calcular_area(3.14, 10))
print(circulo.calcular_perimetro(3.14, 10))