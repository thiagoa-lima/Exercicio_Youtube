pesos = []
for i in (range(1, 6)):
    pesos.append(float(input(f"Peso da {i}ª pessoa: ")))
print(f"O maior peso lido foi de {max(pesos)} Kg")
print(f"O menor peso lido foi de {min(pesos)} Kg")
