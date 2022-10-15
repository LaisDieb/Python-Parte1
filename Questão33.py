#33. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input("Informe o seu salário em reais:R$ "))
if sal>1250:
    aumento = sal + (sal * 0.1)
    print("O valor do seu salário é R${}.\nCom o aumento de 10% passa a ser R${}.".format(sal, aumento))
else:
    aumento = sal + (sal * 0.15)
    print("O valor do seu salário é R${}.\nCom o aumento de 15% passa a ser R${}.".format(sal, aumento))
