print("---------------------------")
print("    CADASTRE UMA PESSOA    ")
print("---------------------------")


maior_18 = []
homem = []
f_menor18 = []

continua = "S"
while continua in "S":
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).upper().strip()
    print("---------------------------")

    if sexo == "M":
        homem.append(idade)

    if idade > 18:
        maior_18.append(idade)

    if idade < 18 and sexo == "F":
        f_menor18.append(idade)

    print()

    continua = str(input("Quer continuar? [S/N]: ")).upper().strip()
    while continua not in "SN":
        continua = str(input("Quer continuar? [S/N]: ")).upper().strip()

print(f"Total de pessoas com mais de 18 anos: {len(maior_18)}")
print(f"Ao todo tempo {len(homem)} homens cadastrados")
print(f"E temos {len(f_menor18)} mulheres com menos de 20 anos")


    
