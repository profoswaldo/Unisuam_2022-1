def exibir(aux):
    print(aux)


def somar(val1, val2):
    return val1 + val2


def subtrair(val1, val2):
    return val1 - val2


valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

soma = somar(valor1, valor2)
subtracao = subtrair(valor1, valor2)

exibir("O valor do soma é igual a:")
exibir(soma)
exibir("O valor da subtracao é igual a:")
exibir(subtracao)
