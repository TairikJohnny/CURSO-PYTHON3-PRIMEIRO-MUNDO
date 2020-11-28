distancia = float(input("Informe a distancia da viagem em KM: "))

if distancia <= 200:
    print("A distancia percorrida vai ser de {}KM e o preço da passagem é de R${:.2f}".format(distancia, (distancia * 0.50)))
else:
    print("A distancia percorrida vai ser de {}KM e o preço da passagem é de R${:.2f}".format(distancia, (distancia * 0.45)))
