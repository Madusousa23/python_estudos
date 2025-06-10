"""Peça o ano de nascimento e diga se a pessoa já pode votar (idade >= 16)"""

ano=int(input("Em qual ano você nasceu ?"))
ano_atual = 2024

idade = ano_atual - ano

if idade >=16:
    print("Pode votar !")
    print("Você já tem: {}anos" .format(idade))
else: 
    print("Não pode votar")
    print("Você ainda tem: {}".format(idade))