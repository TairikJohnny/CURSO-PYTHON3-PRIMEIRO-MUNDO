a = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(a))  # verifica o tipo primitivo da variavel
print("Só tem espaços? ", a.isspace())  # verifica se a variavel só tem espaços
print("É um número? ", a.isnumeric())  # verifica se a variavel só tem números
print("É alfabético? ", a.isalpha())  # verifica se a variavel é alfabética
print("É alfanumérico? ", a.isalnum())  # verifica se a variavel é alfanumérica
print("Esta em letras maiúsculas? ", a.isupper())  # verifica se a variavel esta com letras todas em maiuscúla
print("Esta em letras minúsculas? ", a.islower())  # verifica se a variavel esta com letras todas em munúsculas
print("Está capitalizada? ", a.istitle())  # verifica se a variavel esta capitalizada (primeira letra em maiúsculas e o resto em minúsculas)
