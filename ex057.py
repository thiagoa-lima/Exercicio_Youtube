
sexo = str(input("Informe seu sexo: [M/F] ").upper().strip())

while sexo not in ("M", "F"):
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ").upper().strip())

