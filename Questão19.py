#19. Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Primeiro aluno: "))
n3 = str(input("Primeiro aluno: "))
n4 = str(input("Primeiro aluno: "))
lista =[n1,n2,n3,n4]
escolhido = random.choice(lista)

print("O aluno escolhido foi {}.".format(escolhido))