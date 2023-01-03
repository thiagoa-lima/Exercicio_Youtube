print("-=" * 15)
print("Analisador de Triângulos")
print("-=" * 15)

reta_1 = float(input("Primeiro segmento: "))
reta_2 = float(input("Segundo segmento: "))
reta_3 = float(input("Terceiro segmento: "))

if reta_1 == reta_2 == reta_3:
    triangulo = "EQUILÁTERO"
elif reta_1 != reta_2 != reta_3 != reta_1:
    triangulo = "ISÓSCELES"
else:
    triangulo = "ESCALENO"

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print(f"Os segmentos acima PODEM FORMAR um triângulo {triangulo} ")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
