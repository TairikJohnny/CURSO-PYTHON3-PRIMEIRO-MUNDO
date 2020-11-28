km = float(input("Informe a quantidade de de KM percorridos: "))
dias = int(input("Informe quantos dias o carro foi alugado: "))

km_rodado = km * 0.15
aluguel_carro = dias * 60
soma = km_rodado + aluguel_carro

print("O valor a ser pago é de R$ {:.2f}".format(soma))