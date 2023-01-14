
quantidade = soma = 0
numeros = []

continua = "S"
while continua != "N":
    numero = int(input("Digite um número: "))
    continua = str(input("Quer continuar? [S/N] ").upper())
    numeros.append(numero)
    quantidade += 1
    print(numeros)

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)
print(f"Você digitou {quantidade} e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")


