# Uma escola deseja fazer o programa que gere o boletim de suas turmas. O programa deverá receber a quantidade de alunos da turma e, para cada aluno, a matricula, nome, nota do teste, nota da prova e calcular e exibir, para cada aluno, a matricula, o nome, a média e o status do aluno, conforme discriminado abaixo:
# Aprovado: média superior ou igual a 7
# Reprovado: Média inferior a 7


numero_aluno = int(input("Digite a quantidade de alunos da turma: "))
for na in range(numero_aluno):
    # Dados
    matricula = input("Digite a matricula: ")
    nome = input("Digite o nome: ")
    teste = float(input("Digite a nota do teste: "))
    prova = float(input("Digite a nota da prova: "))
    # processamento:
    media = (teste + prova) / 2
    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
    print("O aluno " + nome + ", de matricula " + matricula + " obteve a média de " + str(media) + " e está " + status)


