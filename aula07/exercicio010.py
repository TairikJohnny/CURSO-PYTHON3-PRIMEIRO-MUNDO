dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))

conversao = dinheiro / 4.97  # Cotação do Dólar do dia 10/06/2020

print("Com R$ {:.2f}, você pode comprar US$ {:.2f}".format(dinheiro, conversao))