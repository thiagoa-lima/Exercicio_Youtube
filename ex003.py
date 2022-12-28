
# Usa-se o int para números inteiros
valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite outro valor: "))

soma_1 = valor_1 + valor_2

print("A soma entre {} e {} é igual a {}!".format(valor_1, valor_2, soma_1))
print(f"A soma entre {valor_1} e {valor_2} é igual a {soma_1}!")

# Usa-se o float para números reais
valor_3 = float(input("Digite um valor: "))
valor_4 = float(input("Digite outro valor: "))

soma_2 = valor_3 + valor_4
print("A soma entre {} e {} é igual a {}! - NÚMEROS FLOAT SEM FORMATAÇÃO".format(valor_3, valor_4, soma_2))
print("A soma entre {:.0f} e {:.0f} é igual a {:.0f}! NÚMEROS FLOAT COM FORMATAÇÃO".format(valor_3, valor_4, soma_2))
print(f"A soma entre {valor_3:.0f} e {valor_4:.0f} é igual a {soma_2:.0f}! NÚMEROS FLOAT SEM FORMATAÇÃO")
