import random
n1 = str(input("Primero nome do aluno: "))
n2 = str(input("Segundo nome do aluno: "))
n3 = str(input("Terceiro nome do aluno: "))
aluno = [n1, n2, n3]
es = random.shuffle(aluno)
print(f"O aluno escolhido foi: {aluno}")