import random

print("Sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
palpite = int(input("Qual é seu palpite? "))
tentativas = 0

computador = random.randrange(0, 11)
print(computador)

while palpite != computador:
    if palpite > computador:
        print("Menos... Tente mais uma vez.")
        palpite = int(input("Qual é seu palpite? "))
        tentativas += 1
    if palpite < computador:
        print("Mais... Tente mais uma vez.")
        palpite = int(input("Qual é seu palpite? "))
        tentativas += 1
    if palpite == computador:
        tentativas += 1
        print(f"Acertou com {tentativas} tentativas. Parabéns!")


