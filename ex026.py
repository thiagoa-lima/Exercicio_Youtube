frase = str(input("Digite uma frase: ")).strip().lower()

a = frase.count("a")
primeiro_a = frase.find("a") + 1
ultimo_a = frase.rfind("a") + 1

print(f"A letra A aparece {a} vezes na frase.")
print(f"A primeira letra A apareceu na posição {primeiro_a}")
print(f"A útim a letra A apareceu na posição {ultimo_a}")