
def exibir(aux):
  print(aux)

def multiplicar(num1, num2):
  return num1 * num2

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
produto = multiplicar(valor1,valor2)
exibir("O valor do produto é ")
exibir(produto)
