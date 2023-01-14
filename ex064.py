
soma = cont = 0
numero = int(input("Digite um número qualquer [999 para parar]: "))

while numero != 999:
    soma += numero
    cont += 1
    numero = int(input("Digite um número qualquer [999 para parar]: "))
    print(cont, numero, soma)

print(f"Você digitou {cont} e a soma entre eles foi {soma}")
