from random import choice

aluno01 = input("Informe o nome do primeiro aluno: ")
aluno02 = input("Informe o nome do segundo aluno: ")
aluno03 = input("Informe o nome do terceiro aluno: ")
aluno04 = input("Informe o nome do quarto aluno: ")

lista= [aluno01, aluno02, aluno03, aluno04]

escolhido = choice(lista)

print("O aluno escolhido foi {}".format(escolhido))
