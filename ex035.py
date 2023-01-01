print("-=" * 15)
print("Analisador de Triângulos")
print("-=" * 15)

primeiro = float(input("Primeiro segmento: "))
segundo = float(input("Segundo segmento: "))
terceiro = float(input("Terceiro segmento: "))

if   (abs(segundo - terceiro) < primeiro < segundo + terceiro):
    print("Os segmentos acima PODEM FORMAR um triangulo")
elif (abs(primeiro - terceiro) < segundo < primeiro + terceiro):
    print("Os segmentos acima PODEM FORMAR um triangulo")
elif (abs(primeiro - segundo) < terceiro < primeiro + segundo):
    print("Os segmentos acima PODEM FORMAR um triangulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triangulo")
