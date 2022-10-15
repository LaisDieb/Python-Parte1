#32. Faça um programa que leia três números e diga qual é o maior e qual o menor.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o primeiro número: "))
c = float(input("Digite o primeiro número: "))
#Verificando quem é menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor número digitado foi {}.".format(menor))
print("O maior número digitado foi {}.".format(maior))

