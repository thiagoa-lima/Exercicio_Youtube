import datetime

cont_maior = 0
cont_menor = 0
ano_atual = datetime.date.today().year

for i in range(1, 8):
    nascimento = int(input(f"Em que ano a pessoa {i}ª pessoa nasceu? "))
    if (ano_atual - nascimento > 18):
        cont_maior += 1
    elif (ano_atual - nascimento < 18):
        cont_menor += 1

print(f"\nAo todo tivemos {cont_maior} pessoas maiores de idade")
print(f"E também tivemos {cont_menor} pessoas menores de idade")
