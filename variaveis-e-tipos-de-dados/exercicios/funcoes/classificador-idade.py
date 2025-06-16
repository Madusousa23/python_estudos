"""Crie uma função que receba a idade de uma pessoa e diga se ela é: criança (0–12), adolescente (13–17), adulta (18–59) ou idosa (60+)."""

idade=int(input("Entre com a sua idade: "))

def classificador(idade):
    if idade == 0 or idade <=12:
        print("Criança")
    elif idade == 13 or idade <=17:
        print("Adolescente")
    else:
        print("Adulto(a)")

classificador(idade)