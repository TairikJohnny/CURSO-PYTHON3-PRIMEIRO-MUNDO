from random import shuffle

aluno01 = input("Primeiro aluno: ")
aluno02 = input("Segundo aluno: ")
aluno03 = input("Terceiro aluno: ")
aluno04 = input("Quarto aluno: ")

lista = [aluno01, aluno02, aluno03, aluno04]

shuffle(lista)

print("A ordem de apresentação sera ")
print(lista)
