def exibir_mensagem_soma():
    print("Valor da Soma: ")


def exibir_mensagem_subtracao():
    print("Valor da Subtração: ")


def exibir_soma():
    print(soma)


def somar():
    return numero1 + numero2


def subtrair():
    return numero1 - numero2


def exibir_subtracao():
    print(subtracao)


numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))

soma = somar()
subtracao = subtrair()

exibir_mensagem_soma()
exibir_soma()

exibir_mensagem_subtracao()
exibir_subtracao()

