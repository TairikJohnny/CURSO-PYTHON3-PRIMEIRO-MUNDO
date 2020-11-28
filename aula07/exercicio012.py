produto = float(input("Digite o preço do produto: R$ "))

desconto = produto - (produto * 5 / 100)

print("O produto que custava R$ {}, agora custa R$ {:.2f} com o desconto de 5%".format(produto, desconto))
