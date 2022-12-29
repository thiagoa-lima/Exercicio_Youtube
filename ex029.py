velocidade_atual = float(input("Qual é a velocidade atual do carro? "))

limite_velocidade = 80

multa = (velocidade_atual - limite_velocidade) * 7

if velocidade_atual <= limite_velocidade:
    print("Tenha um bom dia! Diriga com segurança!")
else:
    print("MULTADO! Você excedeu o limite o limite permitido que é de 80km/h")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
    print("Tenha um bom dia! Dirija com segurança!")
