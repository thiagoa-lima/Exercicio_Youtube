
soma = 0
cont = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma = soma + numero
        cont = cont + 1
print(f"1. {cont} números no total")
print(f"2. {soma} é a soma de todos os números ímpares divisíveis por 3")

