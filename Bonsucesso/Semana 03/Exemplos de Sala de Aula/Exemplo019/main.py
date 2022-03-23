# Faça um algoritmo em Python para receber um número qualquer e informar na tela se é par ou ímpar.


# Dados: Número - ler
# Processamento:
   # calcular resto da difisão por 2
   #identificar par/impar
# Informação: exibir par/impar


numero = float(input("Digite um número: "))

if numero % 2 == 0:
  print("Par")
else:
  print("Ímpar")

