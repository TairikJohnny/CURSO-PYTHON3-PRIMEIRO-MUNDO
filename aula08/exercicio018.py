from math import radians, cos, sin, tan

angulo = float(input("Digite o valor do ângulo: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O seno do ângulo {} é {:.2f}".format(angulo, seno))
print("O cosseno do ângulo {} é {:.2f}".format(angulo, cosseno))
print("A tangente do ângulo {} é {:.2f}".format(angulo, tangente))
