def exibir_soma():
    print(soma)


def exibir_subtracao():
    print(subtracao)


def somar():
    return valor1 + valor2


valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

soma = somar()
subtracao = valor1 - valor2

exibir_soma()
exibir_subtracao()
