print("Gerador de PA")
print("-=" * 10)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))

termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} > ", end="")
    termo = termo + razão
    cont += 1
print("FIM")
