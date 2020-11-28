'''
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input("Informe o seu salario: R$ "))

if salario <= 1250:
    reajuste = salario + (salario * 15 / 100)
else:
    reajuste = salario + (salario * 10 / 100)

print("O salario antigo é R$ {:.2f} e o salario atualizado é R$ {:.2f}".format(salario, reajuste))
