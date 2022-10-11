#8. Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
num= float(input("Digite um valor em metros: "))

cm= num*100
mm= num*1000

print("O valor digitado de {} metros corresponde a {:.2f} centímetros e {:.2f} milímetros.".format(num,cm,mm))