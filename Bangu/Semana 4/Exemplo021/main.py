# Desenvolva um programa que leia o nome dos amigos da turma e saude-os com BOm dia, enquanto não for  digitado "Oswaldo"


nome = input("Digite o nome: ")
while nome!="Oswaldo":
   print("Bom dia " + nome);
   nome = input("Digite o nome: ")
