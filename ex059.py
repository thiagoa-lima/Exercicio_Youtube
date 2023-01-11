from time import sleep

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

opção = 0
while opção != 5:

    print("    [ 1 ] somar")
    print("    [ 2 ] multiplicar")
    print("    [ 3 ] maior")
    print("    [ 4 ] novos valores")
    print("    [ 5 ] sair do programa")

    opção = int(input("Qual é a sua opção? "))

    if opção == 1:
        soma = valor1 + valor2
        print(f"O resultado de {valor1} + {valor2} = {soma}")
        print("=-=" * 10)
        sleep(1)

    elif opção == 2:
        multiplicação = valor1 * valor2
        print(f"O resultado de {valor1} x {valor2} = {multiplicação}")
        print("=-=" * 10)
        sleep(1)

    elif opção == 3:
        maior = max(valor1, valor2)
        print(f"Entre {valor1} e {valor2}, o maior é {maior}")
        print("=-=" * 10)
        sleep(1)

    elif opção == 4:
        print(f"Informe os números novamente")
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
        sleep(1)

    elif opção == 5:
        print(f"Programa encerrado com sucesso!")

    else:
        print("Opção inválida. Esolha uma opção válida.")
        sleep(1)