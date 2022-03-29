# Desenvolva um algoritmo em python que receba o número de funcionarios de uma empresa e o nome e salario bruto de cada um destes. O Algoritmo deverá exibir, para cada funcionario, o nome e o salario líquido, conforme cálculo demonstrado abaixo:
# INSS = salariobruto *0.11
# salarioliquido = salariobruto - INSS

num_funcionarios = int(input("Digite o número de funcionarios: "))

for num in range(num_funcionarios):
    nome = input("Digite o nome: ")
    salario_bruto = float(input("Digite o salario bruto: "))

    inss = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss

    print("Nome: " + nome)
    print("Salário Líquido: " + str(salario_liquido))










