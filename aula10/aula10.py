nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6.0:
    print("Sua nota foi {} e você foi APROVADO!!!".format(media))
else:
    print("Sua nota foi {} e você foi REPROVADO".format(media))
