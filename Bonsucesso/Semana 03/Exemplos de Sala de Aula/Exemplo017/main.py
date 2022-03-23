# Faça um algoritmo em Python que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.


# Dados:
  # A Ler
  # B Ler
  # C Ler

# Processo
   # soma - calcular
   # identificar se a soma é maior do que C

# Informação
  # exibir se a soma é maior ou não que C



a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

soma = a + b

if soma < c:
  print("Soma de A + B é menor que C")
elif soma == c:
  print("Soma de A + B é igual que C")
else:
  print("Soma de A + B é maior que C")






