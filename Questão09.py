#9. Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n= int(input("Digite um número inteiro: "))
print("A tabuada de {} é: ".format(n))

print('_' * 14)
print('{:>2}  *  1 = {:>3}'.format(n, n * 1))
print('{:>2}  *  2 = {:>3}'.format(n, n * 2))
print('{:>2}  *  3 = {:>3}'.format(n, n * 3))
print('{:>2}  *  4 = {:>3}'.format(n, n * 4))
print('{:>2}  *  5 = {:>3}'.format(n, n * 5))
print('{:>2}  *  6 = {:>3}'.format(n, n * 6))
print('{:>2}  *  7 = {:>3}'.format(n, n * 7))
print('{:>2}  *  8 = {:>3}'.format(n, n * 8))
print('{:>2}  *  9 = {:>3}'.format(n, n * 9))
print('{:>2}  * 10 = {:>3}'.format(n, n * 10))
print('_' * 14)

