velocidade = float(input("Informe a velocidade do veiculo: "))

if velocidade <= 80:
    print("Você está dirigindo com cuidado!!!")
else:
    multa = (velocidade - 80) * 7
    print("Você foi multado e tera que pagar uma multa de R$ {:.2f}".format(multa))
