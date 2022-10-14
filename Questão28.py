#28. Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7 por cada km acima do limite.
veloc= int(input("Informe a velocidade do carro em km/h: "))
multa=(veloc-80)*7
if veloc>80:
    print("Você ultrapassou a velocidade máxima. \nDeverá pagar uma multa no valor de R${}".format(multa))