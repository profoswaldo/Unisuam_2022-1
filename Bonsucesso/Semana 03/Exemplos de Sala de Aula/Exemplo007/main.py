# Desenvolva um algoritmo em Python que receba 2 notas e que calcule e exiba a média do aluno e sua situação conforme demonstrado abaixo:
   # aprovado  -> Média maior ou igual a 7
   # reprovado -> Média inferior a 7


#Dados:
   # Notas

#Processamento:
   # calcular media
   # identificar a situacao

#Informação:
   # media
   # situacao


teste = float(input("Digite a nota do Teste: "))
prova = float(input("Digite a nota da Prova: "))

#media = (teste + prova)/2
soma = teste + prova
media = soma /2

if media>=7:
  print(media)
  situacao = "Aprovado"
  print(situacao)
else:
  print(media)
  situacao = "Reprovado"
  print(situacao)






