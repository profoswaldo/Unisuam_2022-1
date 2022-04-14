class Circulo:
  pi = 3.14
  def calcular_area(self):
    return self.pi*self.raio*self.raio

  def calcular_perimetro(self):
    return 2*self.pi*self.raio

circulo = Circulo()
circulo.raio = int(input("Digite o valor do raio: "))
print(circulo.calcular_area())
print(circulo.calcular_perimetro())