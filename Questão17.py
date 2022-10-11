#17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostra o comprimento da hipotenusa.
import math
co = float(input("Informe o comprimento do cateto oposto: "))
ca = float(input("Informe o comprimento do cateto adjacente: "))

hi = math.hypot(co, ca)
print("O comprimento da hipotenusa é {:.2f}." .format(hi))

'''Método sem o uso de biblioteca:
co = float(input("Informe o comprimento do cateto oposto: "))
ca = float(input("Informe o comprimento do cateto adjacente: "))

hi = (co**2 + ca**2)**(1/2)
print("O comprimento da hipotenusa é {:.2f}." .format(hi))'''