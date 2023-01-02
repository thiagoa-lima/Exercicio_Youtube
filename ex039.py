import datetime

ano_nascimento = int(input("Ano de nascimento: "))
ano_corrente = datetime.date.today().year

idade = ano_corrente - ano_nascimento

tempo_para_alistamento = 18 - (ano_corrente - ano_nascimento)

if idade < 18:
    print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_corrente}.")
    print(f"Ainda faltam {tempo_para_alistamento} anos para o alistamento.")
    print(f"Seu alistamento será em {ano_corrente + tempo_para_alistamento}.")
elif idade > 18:
    print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_corrente}.")
    print(f"Você já deveria ter se alistado há {abs(tempo_para_alistamento)} anos.")
    print(f"Seu alistamento foi em {ano_corrente + tempo_para_alistamento}.")
else:
    print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_corrente}.")
    print(f"Você tem que se alistar IMEDIATAMENTE!!!")