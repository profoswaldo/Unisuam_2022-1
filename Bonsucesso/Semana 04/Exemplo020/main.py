# Desenvolva um algoritmo que receba um valor inteiro e que exiba os números de 0 até ele.

# OBS: Obrigatório o uso do while

valor_digitado = int(input("Digite um valor maior que 0: "))
numero = 0
while numero <= valor_digitado:
    print(numero)
    numero = numero + 1

print("Valor final do numero: " + str(numero))
