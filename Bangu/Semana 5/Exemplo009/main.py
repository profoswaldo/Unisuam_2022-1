def calcular_inss():
  return salario_bruto * 0.11

def calcular_salario_liquido():
  return salario_bruto - inss


matricula = input("Digite a matricula: ")
while matricula != "0":
    nome = input("Digite o nome: ")
    salario_bruto = float(input("Digite o salario bruto: "))

    inss = calcular_inss()
    salario_liquido = calcular_salario_liquido()

    print("Matricula: " + matricula)
    print("Nome: " + nome)
    print("INSS: " + str(inss))
    print("Salário Bruto: " + str(salario_bruto))
    print("Salário Líquido: " + str(salario_liquido))

    matricula = input("Digite a matricula: ")