#18. Faça um programa que leia um ângulo qualquer e mostra na tela o valor
# do seno, cosseno e tangente desse ângulo.
from math
ang = float(input("Informe o ângulo: "))
seno= math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tan= math.tan(math.radians(ang))
print("O ângulo é: {}°.\nSeno: {}.\nCosseno: {}.\nTangente: {}".format(ang,seno,cos,tan))