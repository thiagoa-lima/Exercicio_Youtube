primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))

if primeiro == segundo:
    print("Não existe valor maior, os dois são iguais")
elif primeiro > segundo:
    print("O PRIMEIRO valor é maior")
else:
    print("O SEGUNDO valor é maior")
