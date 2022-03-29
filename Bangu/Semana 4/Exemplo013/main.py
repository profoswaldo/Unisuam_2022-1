# Uma empresa possui 3 funcionario e contratou você para gerar a sua folha de pagamento. Para tanto, desenvolva um algoritmo em Python que receba, para cada funcionario, a sua matricula, nome, valor do salário bruto e que calcule e exiba a matricula, o nome e o salário liquido, conforme determinado abaixo:
# INSS -> salario bruto * 0,11
# salario líquido -> salario bruto - INSS


for i in range(3):
    # dados
    matricula = input("Digite sua matricula: ")
    nome = input("Digite o nome: ")
    salario_bruto = float(input("Digite o salário Bruto: "))

    # Processamento:
    inss = salario_bruto * 0.11
    salario_liquido = salario_bruto - inss

    # Informação
    print("Matricula: " + matricula)
    print("Nome:      " + nome)
    print("Salário Líquido: " + str(salario_liquido))








