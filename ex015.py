total_de_diarias = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos km rodados? "))
valor_da_diaria = 60
valor_do_km = 0.15

total_a_pagar = (total_de_diarias * valor_da_diaria) + (km_rodados * valor_do_km)

print(f"O total a pagar pelo aluguel do carro é de R${total_a_pagar:.2f}")