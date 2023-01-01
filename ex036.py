valor_da_casa = int(input("Valor da casa: R$"))
salario = int(input("Salario do comprador: R$"))
anos_de_financiamento = int(input("Quantos anos de financiamento? "))

prestacao = valor_da_casa / (anos_de_financiamento * 12)

print(f"Para pagar um casa de R${valor_da_casa:.2f} em {anos_de_financiamento} a prestação será "
      f"de R$ {prestacao:.2f}")


if (prestacao / salario * 100) < 30:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NÃO pode ser CONCEDIDO!")

