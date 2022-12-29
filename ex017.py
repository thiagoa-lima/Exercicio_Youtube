import math

angulo = float(input("Digite o ângulo que voce deseja: "))

radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f"O ângulo de {angulo:.2f} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo:.2f} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo:.2f} tem o TANGENTE de {tangente:.2f}")