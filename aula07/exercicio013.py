salario = float(input("Informe o salario do funcionario: R$ "))

aumento = salario + (salario * 15 / 100)

print("O salario do funcionario passou de R$ {:.2f}, para R$ {:.2f} com um aumento de 15%".format(salario, aumento))
