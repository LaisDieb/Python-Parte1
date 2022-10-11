#20. O mesmo professor do desafio anterior quer sortear a ordem de apresentção de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Primeiro aluno: "))
n3 = str(input("Primeiro aluno: "))
n4 = str(input("Primeiro aluno: "))
lista =[n1,n2,n3,n4]
random.shuffle(lista)

print("A ordem de apresentçaõ será:")
print(lista)