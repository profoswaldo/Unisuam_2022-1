# Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.


numero = float(input("Digite um número: "))

resto = numero % 2

if resto != 0:
    numero = numero + 8
else:
    numero = numero + 5

print(numero)
