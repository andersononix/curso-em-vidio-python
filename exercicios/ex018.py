import math
an = float(input("Qual o angulo do triangolo: "))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print("O angulo do treangulo é: {}, O seno é: {:.2f}".format(an, seno))
print("O angulo do treangulo é: {}, O seno é: {:.2f}".format(an, cosseno))
print("O angulo do treangulo é: {}, O seno é: {:.2f}".format(an, tangente))
