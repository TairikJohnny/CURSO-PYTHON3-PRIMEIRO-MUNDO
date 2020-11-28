num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))
num3 = int(input("Informe o terceiro valor: "))

# Verificando o menor

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando o mair
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num2:
    maior = num3

print("O menor valor informado foi {}".format(menor))
print("O maior valor informado foi {}".format(maior))
