numero = input("Inform um número qualquer: ")

print(f"Analisando o número {numero}")

numero_separado = " ".join(numero)

lista = numero_separado.split()

if (len(lista) == 1):
    print(f"Unidade: {lista[len(lista) - 1]}")
    print(f"Dezena:  0")
    print(f"Centena: 0")
    print(f"Milhar:  0")
elif (len(lista) == 2):
    print(f"Unidade: {lista[len(lista) - 1]}")
    print(f"Dezena:  {lista[len(lista) - 2]}")
    print(f"Centena: 0")
    print(f"Milhar:  0")
elif (len(lista) == 3):
    print(f"Unidade: {lista[len(lista) - 1]}")
    print(f"Dezena:  {lista[len(lista) - 2]}")
    print(f"Centena: {lista[len(lista) - 3]}")
    print(f"Milhar:  0")
else:
    print(f"Unidade: {lista[len(lista) - 1]}")
    print(f"Dezena:  {lista[len(lista) - 2]}")
    print(f"Centena: {lista[len(lista) - 3]}")
    print(f"Milhar:  {lista[len(lista) - 4]}")
