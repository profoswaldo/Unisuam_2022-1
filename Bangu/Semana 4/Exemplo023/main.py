# Faça um programa que receba o salário dos funcionarios de uma empresa, até que seja digitado 0 para o salario, e que calcule e mostre, para cada funcionario, o novo salário, acrescido de bonificação, conforme tabela abaixo:

# SALARIO 			                  	  BONIFICAÇÃO
# Até R$ 500,00			              	5% do salário
# Entre R$ 500,00 e R$ 1200,00	  	  12% do salário
# Acima de R$ 1200,00		         		Sem bonificação

salario_bruto = float(input("Digite o salario bruto: "))

while salario_bruto != 0:
    if salario_bruto <= 500:
        bonificacao = salario_bruto * 5 / 100
    elif salario_bruto <= 1200:
        bonificacao = salario_bruto * 12 / 100
    else:
        bonificacao = 0

    salario_liquido = salario_bruto + bonificacao
    print("Salario Líquido: " + str(salario_liquido))
    salario_bruto = float(input("Digite o salario bruto: "))