import random

aluno_1 = str(input("Primeiro aluno: "))
aluno_2 = str(input("Segundo aluno: "))
aluno_3 = str(input("Terceiro aluno: "))
aluno_4 = str(input("Quarto aluno: "))

print("A ordem de apresentação será")

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

random.shuffle(lista_alunos) # embaralha a lista

print(lista_alunos)

