# Suponha que você foi contratado para identificar a média dos alunos d turma Bangu-Manha-Front_end. Sabe-se que, para cada aluno, será digitado a matricula, nome, 3 notas e deverá ser calculado e exibido a matricula, o nome e a média de cada aluno, até que seja digitado "FIM" para a matricula.

matricula = input("Digite a matricula: ")
while matricula!="FIM":
  # Dados
  nome =  input("Digite o nome: ")
  nota_1 =  float(input("Digite a nota 1: "))
  nota_2 =  float(input("Digite a nota 2: "))
  nota_3 =  float(input("Digite a nota 3: "))
  # processamento:
  media = (nota_1 + nota_2 + nota_3)/3
  # Informação
  print("Matricula: " + matricula)
  print("Nome: " + nome)
  print("Média: " + str(media))
  #Dados
  matricula = input("Digite a matricula: ")