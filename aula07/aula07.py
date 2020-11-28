n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
multiplicacao = n1 * n2
divisao_inteira = n1 // n2
potenciacao = n1 ** n2

print(" - A soma é igual a {}".format(soma))
print(" - A subtração é igual a {}".format(subtracao))
print(" - A divisão é igual a {:.3f}".format(divisao))
print(" - A multiplicação é igual a {}".format(multiplicacao))
print(" - A divisão inteira é igual a {}".format(divisao_inteira))
print(" - A potenciação é igual a {}".format(potenciacao))