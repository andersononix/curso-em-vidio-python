import math
co = float(input("Qual o valor do cateto oposto: "))
ca = float(input("Qual o cateto adjacente: "))
hi = math.hypot(co, ca)
print("a hipotenusa é:{:.2f}".format(hi))
