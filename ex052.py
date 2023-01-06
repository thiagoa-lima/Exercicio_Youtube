numero = int(input("Digite um número: "))
cont = 0
for i in range(1, numero + 1):
    print(i, end=" ")
    if (numero % i == 0):
        cont += 1
print(f"\nO número {numero} foi divisível {cont} vezes")
if cont <= 2:
    print("E por isso ele é PRIMO")
else:
    print("E por isso ele NÃO É PRIMO")
