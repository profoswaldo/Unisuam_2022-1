# Faça um algoritimo em Python que receba o nome e três notas de um aluno. Este deverá exibir o nome e a média do mesmo

#saidas: nome, media

#entradas: nome, 3 notas

#processamento: calcular a média

nome = input("Digite o nome do aluno: ")
nota1 = input("Digite a nota 1: ")
nota2 = input("Digite a nota 2: ")
nota3 = input("Digite a nota 3: ")

media = (float(nota1) + float(nota2) + float(nota3))/3

print("Nome: " + nome)
print("Média: " + str(media))