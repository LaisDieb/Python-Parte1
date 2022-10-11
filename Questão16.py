#16. Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
n = float(input("Digite um número real qualquer: "))
print("A porção inteira desse número é {}.".format(trunc(n)))