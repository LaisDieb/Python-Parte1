#6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num= int(input("Digite um valor: "))

d=2*num
t=3*num
rq=num**(1/2)
print("Você digitou {}.\nSeu dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}.".format(num,d,t,rq))