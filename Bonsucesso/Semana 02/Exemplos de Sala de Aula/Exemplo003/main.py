# Um motorista deseja colocar no seu tanque X reais de gasolina.
# Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento,
# e exibir quantos litros ele conseguiu colocar no tanque.

# Dados:
        # ler o preço do litro da gasolina
        # ler o valor do pagamento

# Processo:
        # quantidade de litros = valor do pagamento/ preço da gasolina

# Informação:
        # exibir quantidade de litros


preco_gasolina = float(input("Digite o preço da Gasolina: "))
valor_pago = input("Digite o valor pago: ")

quantidade_litros = float(valor_pago) / preco_gasolina

print("Quantidade Abastecida:" + str(quantidade_litros))








