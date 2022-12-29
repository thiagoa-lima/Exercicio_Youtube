distancia = float(input("Qual é a distância da sua viagem? "))
preco_1 = distancia * 0.50
preco_2 = distancia * 0.45

print(f"Você está prestes a comeeçar uma viagem de {distancia}km.")

if (distancia <= 200):
    print(f"E o preço da sua passagem será de R${preco_1}")
else:
    print(f"E o preço da sua passagem será de R${preco_2}")

