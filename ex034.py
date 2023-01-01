salario = float(input("Qual é o salário do funcionário? "))

if salario > 1250:
    aumento = 0.10
else:
    aumento = 0.15

salario_final = salario + (salario * aumento)

print(f"Quem ganhava R${salario:.2f} passa a ganhar R${salario_final:.2f} agora.")