#23. Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome "santo".
cidade= str(input("Em que cidade você nasceu? ")).strip() # Retira eventuais espaços antes e depois da frase.
print(cidade[:5].upper() == "SANTO") #O upper foi utilizado caso o usuário escreva em minúsculo ou saNto, por exemplo.
