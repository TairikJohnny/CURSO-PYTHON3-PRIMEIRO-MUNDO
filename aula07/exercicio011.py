largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

area = largura * altura

print("A dimensão da sua parede é de {} X {} e a sua área é de {:.2f}m²".format(largura, altura, area))

tinta = area / 2

print("Para pintar a sua parede você precisara de {:.2f}L de tinta".format(tinta))
