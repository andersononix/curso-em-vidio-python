import random
n1 = str(input("Primero nome do aluno: "))
n2 = str(input("Segundo nome do aluno: "))
n3 = str(input("Teceiro nome do aluno: "))
aluno = [n1, n2, n3]
es = random.choice(aluno)
print(f"O aluno escolhido foi: {es}")
