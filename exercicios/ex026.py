frase = str(input("Digete uma frase: ")).upper().strip()
print("A letra A aparece: {} vezes na frase".format(frase.count("A")))
print("A pimeira letra A apareceu na posição: {}".format(frase.find("A")+1))
print("A ultima letra A apareceu na posição: {}".format(frase.rfind("A")+1))
