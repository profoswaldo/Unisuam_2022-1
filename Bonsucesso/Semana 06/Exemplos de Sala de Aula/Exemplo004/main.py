def exibir_soma():
    print(soma)


def exibir_subtracao():
    print(subtracao)


def somar(val1, val2):
    return val1 + val2


valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

soma = somar(valor1, valor2)
subtracao = valor1 - valor2

exibir_soma()
exibir_subtracao()
