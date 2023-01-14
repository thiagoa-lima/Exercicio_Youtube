print("-" * 40)
print("Sequência de Fibonacci")
print("-" * 40)

primeiro = 0
segundo = 1

termos = int(input("Quantos termos você quer? "))

sequencia = 0
while sequencia in range(0, termos):
    print(primeiro)
    primeiro = primeiro + segundo
    segundo = primeiro - segundo

    sequencia += 1
