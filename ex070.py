print("--------------------------------------")
print("          LOJA SUPER BARATÃO          ")
print("--------------------------------------")

continua = "S"
total = 0
mais_de_100 = []
contador = 0
mais_barato_item = 0
mais_barato_preco = 0

while continua == "S":
    produto = str(input("Nome do Produto: "))
    preco = int(input("Preço: R$"))

    continua = str(input("Quer continuar? [S/N] ")).upper()

    if continua not in "SsNn":
        continua = str(input("Quer continuar? [S/N] ")).upper()

    total += preco

    if preco > 100:
        mais_de_100.append(preco)

    if contador == 0:
        mais_barato_preco = preco
        mais_barato_item = produto

    elif contador > 0:
        if preco < mais_barato_preco:
            mais_barato_preco = preco
            mais_barato_item = produto

    contador += 1

print("------------FIM DO PROGRAMA-----------")
print(f"O total da compra foi de {total}.")
print(f"Temos {len(mais_de_100)} produtos custando mais de R$1.000,00")
print(f"O produto mais barato foi {mais_barato_item} que custa R${mais_barato_preco:.2f}")
