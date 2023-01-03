peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura (m) "))

IMC = peso / (altura ** 2)
print(" ")
print(f"Seu IMC é de {IMC:.2f}")
print(" ")
if IMC <= 18.5:
    print(f"ATENÇÃO, você está ABAIXO DO PESO!")
elif IMC > 18.5 and IMC <= 25:
    print(f"PARABENS, você está dentro do PESO IDEAL!")
elif IMC > 25 and IMC <= 30:
    print(f"CUIDADO, você está em SOBREPESO!")
elif IMC > 30 and IMC <= 40:
    print(f"CUIDADO DOBRADO, você está em OBESIDADE!")
else:
    print(f"ATENÇÃO, você está em OBESIDADE MÓRBIDA!")
