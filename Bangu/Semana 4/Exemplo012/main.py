# Desenvolva um algoritmo em Python que receba um numero superior a 0 e que exiba os números entre 0 e esse valor, informando se é par ou impar.


numero = int(input("Digite um número maior do que zero: "))
for i in range(numero):
    if i % 2 == 0:
        print("O número " + str(i) + " é Par")
    else:
        print("O número " + str(i) + " é Ímpar")




