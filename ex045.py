import time
import random

print("Sua opções:")

minha_jogada = 0

while minha_jogada not in [1, 2, 3]:
    print("[ 1 ] PEDRA")
    print("[ 2 ] PAPEL")
    print("[ 3 ] TESOURA")

    minha_jogada = int(input("Qual é a sua jogada? "))

    if minha_jogada == 1 or minha_jogada == 2 or minha_jogada == 3:
        pass
    else:
        print("")
        print("Opção inválida. Favor escolher uma opção correta.")

print(" ")
print("JO")
time.sleep(.5)
print("kEN")
time.sleep(.5)
print("PÔ")
print(" ")

numero_computador = random.randint(1, 3)



if minha_jogada == 1:
    meu_jogo = "PEDRA"
elif numero_computador == 2:
    meu_jogo = "PAPEL"
else:
    meu_jogo = "TESOURA"



if numero_computador == 1:
    jogo_computador = "PEDRA"
elif numero_computador == 2:
    jogo_computador = "PAPEL"
else:
    jogo_computador = "TESOURA"

# REGRAS DO JOGO
print("-=" * 15)
print(f"Você jogou {meu_jogo}")
print(f"Computador jogou {jogo_computador}")
print("-=" * 15)
print("1")

if minha_jogada == numero_computador:
    print("Empatou. Ninguem ganhou!!!")
elif minha_jogada == 1 and numero_computador == 3:
    print("Parabens!!! Você ganhou.")
elif minha_jogada == 2 and numero_computador == 1:
    print("Parabens!!! Você ganhou.")
elif minha_jogada == 3 and numero_computador == 2:
    print("Parabens!!! Você ganhou.")
else:
    print("Que pena, o computador ganhou!!! ")

