nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))

media = (nota_2 + nota_1) / 2

print(f"Tirando {nota_1} e {nota_2}, a média do aluno é {media}")

if (media < 5):
    print("O aluno está REPROVADO!")
elif (media >= 5 and media < 6):
    print("O aluno está em recuperação!")
else:
    print("O aluno foi APROVADO!")