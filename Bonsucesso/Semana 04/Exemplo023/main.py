# Um empresa  de produtos alimentício possui vários  pedidos a serem tratados . Para cada pedido foi registrado o número do produto (tipo inteiro), a quantidade do produto (tipo inteiro), e o preço unitário de cada produto (tipo float). Faça um programa em python, que calcule e  mostre o preço total dos produtos a serem vendidos, até que seja digitado o número do produto igual a 0.

numero_produto = input("Digite o número do produto: ")
while numero_produto != "0":
  quantidade_produto = int(input("Digite a quantidade do produto: "))
  preco_unitario_produto = float(input("Digite o preço de cada do produto: "))

  preco_total_produto =  quantidade_produto * preco_unitario_produto

  print("Preço total: " + str(preco_total_produto))

  numero_produto = input("Digite o número do produto: ")



