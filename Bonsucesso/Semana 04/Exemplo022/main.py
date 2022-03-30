# Faça um programa que receba o salário dos funcionários de uma empresa, calcule e mostre o novo salario, acrescido de bonificação, enquanto o salario for positivo.

  #SALARIO 			                  BONIFICAÇÃO
  #Até R$ 500,00			              5% do salário
  #Entre R$ 500,00 e R$ 1200,00	  12% do salário
  #Acima de R$ 1200,00		          Sem bonificação

salario_bruto = float(input("Digite o valor do salario Bruto: "))
while salario_bruto >=0 :
  if salario_bruto <= 500:
    bonificacao = salario_bruto * 5/100
  elif salario_bruto <= 1200:
    bonificacao = salario_bruto * 12/100
  else:
    bonificacao = 0

  salario_liquido = salario_bruto + bonificacao
  print("Salario Líquido: " + str(salario_liquido))
  salario_bruto = float(input("Digite o valor do salario Bruto: "))