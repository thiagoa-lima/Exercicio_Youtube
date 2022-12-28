distancia = float(input("Uma distância em metros: "))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print(f"A distância de {distancia} corresponde a")
print(f"{km}km")
print(f"{hm}hm")
print(f"{dam}dam")
print(f"{dm}dm")
print(f"{cm}cm")
print(f"{mm}mm")
