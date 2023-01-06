frase = str(input("Digite uma frase: ")).strip().upper()
frase_inversa = frase.replace(" ", "")[::-1]
print(f"o inverso de {frase} é {frase_inversa}")

if frase.replace(" ","") == frase_inversa:
    print("A frase digitada é um palíndromo")
else:
    print("A frase digitada é não um palíndromo")
