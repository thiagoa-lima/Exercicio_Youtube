
soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input("Escolha um numero qualquer: "))

    if i % 2 == 0:
        soma = soma + numero
        cont = cont + 1

print(f"soma: {soma}")
print(f"contagem dos números {cont}")