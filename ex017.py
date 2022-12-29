import math

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
hipotenusa_1 = math.hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa mede {hipotenusa:.2f}")

print(f"A hipotenusa mede {hipotenusa_1:.2f}")