print("============ LOJAS GUANABARA ============")

preco = int(input("Preço das compras: R$"))

forma_pagamento = 0

while forma_pagamento not in [1, 2, 3, 4]:

    print("FORMA DE PAGAMENTO")
    print("[ 1 ] à vista dinheiro/pix")
    print("[ 2 ] à vista cartão")
    print("[ 3 ] 2 parcelas no cartão")
    print("[ 4 ] 3 parcelas ou mais no cartão")
    forma_pagamento = int(input("Qual é a opção? "))

    if forma_pagamento == 1:
        print(f"Sua compra é de R${preco:.2f} vai custar R${preco * .9:.2f} no final.")
    elif forma_pagamento == 2:
        print(f"Sua compra é de R${preco:.2f} vai custar R${preco * .95:.2f} no final.")
    elif forma_pagamento == 3:
        print(f"Sua compra será parcelada em 2x de {preco / 2:.2f} SEM JUROS")
    elif forma_pagamento == 4:
        parcelas = int(input("Quantas parcelas? "))
        print(f"Sua compra será parcelada em {parcelas}x de {preco * 1.2 / parcelas:.2f} COM JUROS")
        print(f"Sua compra de R${preco:.2f} vai custar R${preco * 1.2:.2f} no final")
    else:
        print("")
        print("Opção inválida. Escolha uma opção que esteja disponível")
        print("")
