# Faça um algoritmo em Python que leia a nota de um aluno e o número de faltas.Aumentar a nota em um ponto para os alunos que tiverem o número de faltas igual a 0.
# Ao final do algoritmo, exibir a nota final do aluno.

#Dados:
   # Nota ler
   # Faltas ler
   # Ponto extra igual a 1


#Processamento:
    # Verificar se faltas igual a 0
    # Se verdade, adicionar ponto extra

#Informação:
  # nota final do aluno



nota = float(input("Digite a nota: "))
faltas = int(input("Digite as faltas: "))
ponto = 1

notafinal = nota

if faltas==0:
 notafinal = nota + ponto

print(notafinal)






