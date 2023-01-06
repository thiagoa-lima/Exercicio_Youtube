print("===================================")
print("        10 TERMOS DE UMA PA        ")
print("===================================")

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão

for i in range(primeiro, décimo, razão):

    print(i, end=" -> ")
print("ACABOU")
