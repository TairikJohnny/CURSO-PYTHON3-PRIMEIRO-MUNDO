'''
#EXERCICIO 1

x = -2
y = 5

z = (x * y) + 5

if z <= 0:
    resposta = "A"
else:
    if z <= 100:
        resposta = "B"
    else:
        resposta = "C"

if z <= 0:  # Outra maneira de resolver
    resposta = "A"
elif z <= 100:
    resposta = "B"
else:
    resposta = "C"

print("O valor de Z é {} e a resposta é {}".format(z, resposta))
'''
'''
RESOLUÇÃO EXERCICIO 1
    X   |   Y   |   Z   |   RESPOSTA
    3   |   2   |   11  |      B
    150 |   3   |   455 |      C
    7   |   -1  |   -2  |      A
    -2  |   5   |   -5  |      A
    50  |   3   |   155 |      C
'''

'''
#EXERCICIO 2

DONA ROSA = VESTIDO BRANCO
DONA BRANCA = VESTIDO VIOLETA
DONA VIOLETA = VESTIDO ROSA
'''

'''
#EXERCICIO 3

litros = float(input("Informe a quantidade de litros abastecidos: "))
combustivel = input("Informe o tipo do combustivel, sendo A - alcool e G - gasolina: ").upper()

if combustivel == "A":
    if litros <= 20:
        valor = litros * 2.90
        desconto = valor - (valor * 3 / 100)
        print("O valor do ALCOOL(R$2.90 por litro) a ser pago:\n Sem desconto: R${:.2f}\n Com desconto: R${:.2f}".format(valor, desconto))
    else:
        valor = litros * 2.90
        desconto = valor - (valor * 5 / 100)
        print("O valor do ALCOOL(R$2.90 por litro) a ser pago:\n Sem desconto: R${:.2f}\n Com desconto: R${:.2f}".format(valor, desconto))

elif combustivel == "G":
    if litros <= 20:
        valor = litros * 3.30
        desconto = valor - (valor * 4 / 100)
        print("O valor da GASOLINA(R$3.30 por litro) a ser pago:\n Sem desconto: R${:.2f}\n Com desconto: R${:.2f}".format(valor, desconto))
    else:
        valor = litros * 3.30
        desconto = valor - (valor * 6 / 100)
        print("O valor da GASOLINA(R$3.30 por litro) a ser pago:\n Sem desconto: R${:.2f}\n Com desconto: R${:.2f}".format(valor, desconto))

else:
    print("Tipo de combustivel invalido!!!")

'''



