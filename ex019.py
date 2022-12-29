import random

aluno_1 = str(input("Primeiro aluno: "))
aluno_2 = str(input("Segundo aluno: "))
aluno_3 = str(input("Terceiro aluno: "))
aluno_4 = str(input("Quarto aluno: "))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteio = random.choice(lista_alunos)

print(sorteio)
