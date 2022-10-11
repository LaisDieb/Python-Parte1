#10. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n= float(input("Quanto você possui em real? "))
dolar= n/5.16

print("Com {} reais você pode comprar {:.2f} dólares.".format(n,dolar))

