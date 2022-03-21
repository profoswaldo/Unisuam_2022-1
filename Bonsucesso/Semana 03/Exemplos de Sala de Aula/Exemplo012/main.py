# Desenvolva um algoritmo em Python que receba a matricula, nome, e 3 notas de um aluno e que calcule e exiba a matricula, nome, média e conceito do mesmo, conforme definido abaixo:
   # Conceito A - Média maior ou igual a 7
   # Conceito B - Média Menor do que 7 e maior ou igual a 5
   # Conceito C - Média Menor do que 5 e maior ou igual a 3
   # Conceito D - Média Menor do que 3




matricula = input("Digite a matricula: ")
nome = input("Digite a nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3)/3


if media >= 7:
  conceito = "A"
else:
  if media >= 5:
     conceito = "B"
  else:
    if media >= 3:
        conceito = "C"
    else:
        conceito = "D"

print("Matricula: " + matricula)
print("Nome: " + nome)
print("Média: " + str(media))
print("Conceito: " + conceito)