nome = input("Digite seu nome completo: ")

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_contar = len(nome_minusculo) - nome.count(" ")
primeiro_nome = nome.split()[0].capitalize()
primeiro_nome_contar = len(primeiro_nome)

print("Analisando seu nome...")
print(f"Seu nome em maiúscula é {nome_maiusculo}")
print(f"Seu nome em minúsculo é {nome_minusculo}")
print(f"Seu nome tem ao todo {nome_contar} letras")
print(f"Seu primeiro nome é {primeiro_nome} e ele tem {primeiro_nome_contar} letras")

