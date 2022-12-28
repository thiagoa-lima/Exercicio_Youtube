salario_atual = float(input("Qual é o salário do funcionário? "))
taxa_de_reajuste = 15
salario_corrigido = salario_atual + (salario_atual * taxa_de_reajuste / 100)

print(f"Um funcionário com um salário de R${salario_atual}, terá um reajuste de {taxa_de_reajuste}% e passará a receber R${salario_corrigido}")