preco_inicial = float(input("Qual é o preço do produto? "))
taxa_desconto = 5
preco_final = preco_inicial * (1 - taxa_desconto/100)

print(f"O produto que custava R${preco_inicial:.2f}, na promoção com um desconto de {taxa_desconto}% vai custar R${preco_final:.2f}.")
