# Desenvolva um programa em Python   que receba o nome, o teste, a prova dos alunos de uma turma
# O programa deverá calcular e exibir, para cada aluno, a matricula, o nome, a média e se o aluno está aprovado(media>=7) ou reprovado(média<7).
# Além disso, para estar aprovado o aluno tamém precisa ter o número de faltas inferior a 10

nome = input("Digite o nome: ")
teste = float(input("Digite o teste: "))
prova = float(input("Digite a prova: "))
faltas = int(input("Digite ad faltas: "))

media = (teste + prova) / 2

if media >= 7:
    if faltas < 10:
        status = "Aprovado"
    else:
        status = "Reprovado"
else:
    status = "Reprovado"

print("Nome: " + nome)
print("Média: " + str(media))
print("Faltas: " + str(faltas))
print("Status: " + status)