#21. Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras, sem considerar os espaços;
#Quantas letras tem o primeiro nome.


nome= str(input("Digite seu nome completo: ")).strip() #Elimina espaços antes e depois
print("Analisando seu nome...")
print("Seu nome com todos os caracteres em maiúsculo: {}".format(nome.upper()))
print("Seu nome com todos os caracteres em minúsculo: {}".format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nome) - nome.count(" ")))
#print("Seu primeiro nome tem {} letras.".format(nome.find(" "))) #Retirando o primeiro espaço, sabe-se quantos caracteres vem anteriormente
separa = nome.split()
print("Seu primeiro nome tem {} letras.".format(len(separa[0])))