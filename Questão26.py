#26. Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro
# e o último nome separadamente.
nome = str(input("Qual seu nome completo? "))
separa = nome.split()
print("Seu primeiro nome é: {}".format(separa[0]))
print("Seu último nome é: {}".format(separa[len(separa)-1]))
