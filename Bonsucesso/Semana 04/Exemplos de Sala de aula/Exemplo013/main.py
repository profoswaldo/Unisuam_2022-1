# Desenvolva um algormtimo em Python que, dada uma turma composta por 5 alunos, receba a matricula, o nome, a nota de teste, a nota da prova e que calcule e exiba, para cada aluno, a matricula, o nome e a média individual.


for numero_vezes in range(5):
    matricula = input("Digite a matricula: ")
    nome = input("Digite o nome: ")
    teste = float(input("Digite o teste: "))
    prova = float(input("Digite a prova: "))
    media = (teste + prova) / 2;
    print("Matricula: " + matricula)
    print("Nome: " + nome)
    print("Média: " + str(media))












