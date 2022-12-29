import random
import time

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)

# A função .randint(1, 5) faz o computador escolher um número inteiro aleatório entre 1 e 5
computador = random.randint(1, 5)

jogador = int(input("Qual número eu pensei? "))

print("PROCESSANDO...")

time.sleep(2)

if jogador == computador:
    print("PARABENS, você ganhou.")
else:
    print(f"QUE PENA, voce errou! Eu pensei no número {computador} e não no número {jogador}.")