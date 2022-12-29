nome = str(input("Digite seu nome completo: ")).strip()

lista = nome.split()
primeiro_nome = lista[0].title()
ultimo_nome = lista[len(lista) - 1].title()

print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {primeiro_nome}")
print(f"Seu último nome é {ultimo_nome}")

