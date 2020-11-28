from math import hypot

cateto_oposto = float(input("Digite o valor do comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do comprimento do cateto adjacente: "))

#  hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
