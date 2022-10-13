#25. Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aprece a primeira vez;
#Em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: ")).upper().strip()
print("Essa frase possui {} letra(s) A.".format(frase.count("A")))
print("A letra A aparece a primeira vez na posição {}.".format(frase.find("A")+1)) # O (+1) é utilizado para desconsiderar a posição zero.
print("A letra A aparece a última vez na posição {}.".format(frase.rfind("A")+1))