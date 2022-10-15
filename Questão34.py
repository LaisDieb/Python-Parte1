#34. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("-=-"*8)
print("ANALISADOR DE TRIÂNGULO")
print("-=-"*8)
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima podem formar um triângulo.")
else:
    print("Os segmentos acima não podem formar um triângulo.")