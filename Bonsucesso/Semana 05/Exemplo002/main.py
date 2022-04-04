# Desenvolva um programa em Python   que receba a matricula, o nome, o teste, a prova dos alunos de uma turma, até que seja digitado 0 para a matricula do aluno.
# O programa deverá calcular e exibir, para cada aluno, a matricula, o nome, a média e se o aluno está aprovado(media>=7), Final(media >=5 e <7) ou reprovado(média<5).


matricula = input("Digite a matricula: ")
while not (matricula == "0"):

    nome = input("Digite o nome: ")
    teste = float(input("Digite o teste: "))
    prova = float(input("Digite a prova: "))
    media = (teste + prova) / 2
    if media >= 7:
        status = "Aprovado"
    elif media < 5:
        status = "Reprovado"
    else:
        status = "Final"

    print("Matricula: " + matricula)
    print("Nome: " + nome)
    print("Média: " + str(media))
    print("Status: " + status)

    matricula = input("Digite a matricula: ")