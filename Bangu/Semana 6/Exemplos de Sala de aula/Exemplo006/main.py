def exibir(msg):
    print(msg)


def somar(valor1, valor2):
    return valor1 + valor2


def subtrair(valor1, valor2):
    return valor1 - valor2


numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))

soma = somar(numero1, numero2)
subtracao = subtrair(numero1, numero2)

exibir("Valor da Soma: ")
exibir(soma)

exibir("Valor da Subtração: ")
exibir(subtracao)

