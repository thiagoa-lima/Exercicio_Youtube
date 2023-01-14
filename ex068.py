import random

print("=" * 30)
print("VAMOS JOGAR PAR OU IMPAR")
print("=" * 30)

numero_jogador = int(input("Diga um valor: "))
opcao_jogador = str(input("Par ou Ímpar [P/I]?: ")).upper()

while opcao_jogador not in "PpIi":
    opcao_jogador = str(input("Par ou Ímpar [P/I]?: "))
print("-" * 30)

numero_computador = random.randint(1, 10)
soma = numero_computador + numero_jogador

if soma % 2 == 0:
    resultado = "DEU PAR"
else:
    resultado = "DEU ÍMPAR"

print(f"Você jogou {numero_jogador} e computador {numero_computador}. Total deu {soma} e {resultado}")

if resultado == "DEU PAR" and opcao_jogador == "P":
    print("VOCÊ VENCEU")
elif resultado == "DEU IMPAR" and opcao_jogador == "I":
    print("VOCÊ VENCEU")
else:
    print("VOCÊ PERDEU")