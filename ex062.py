print("Gerador de PA")
print("-=" * 10)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

cont = 0
cont_final = 10
mais = 1
while mais != 0:
    while cont < cont_final:
        print(primeiro, end=" > ")
        primeiro += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar mais? "))
    cont_final += mais
print(f"Progressão finalizada com {cont_final} termos mostrados")