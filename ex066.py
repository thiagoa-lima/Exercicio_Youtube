valor = 0
valores = []
while valor != 999:
    valor = int(input("Digite um valor [999 para parar]: "))
    if valor == 999:
        pass
    else:
        valores.append(valor)
    print(valores)

print(f"A soma dos {len(valores)} valores foi de {sum(valores)}!")
