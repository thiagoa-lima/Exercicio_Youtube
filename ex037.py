numero = int(input("Digite um número inteiro: "))
print("")
print("Escolha uma das bases para conversão:")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
print("")
sua_opcao = int(input("Sua opção: "))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

if sua_opcao == 1:
    print(f"{numero} convertido para BINÁRIO é igual a {binario}")
elif sua_opcao == 2:
    print(f"{numero} convertido para OCTAL é igual a {octal}")
elif sua_opcao == 3:
    print(f"{numero} convertido para HEXADECIMAL é igual a {hexadecimal}")
else:
    print("Escolha um número de 1 a 3")
