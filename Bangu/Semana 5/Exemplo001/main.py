# Desenvolva um programa em Python calcule e exiba o salario liquido, o valor do Inss(11%), a matricula e o nome dos funcionarios de uma empresa, até que seja digitado 0 para a matricula do funcionario.


matricula = input("Digite a matricula: ")
while matricula != "0":
    nome = input("Digite o nome: ")
    salario_bruto = float(input("Digite o salario bruto: "))

    inss = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss

    print("Matricula: " + matricula)
    print("Nome: " + nome)
    print("INSS: " + str(inss))
    print("Salário Bruto: " + str(salario_bruto))
    print("Salário Líquido: " + str(salario_liquido))

    matricula = input("Digite a matricula: ")