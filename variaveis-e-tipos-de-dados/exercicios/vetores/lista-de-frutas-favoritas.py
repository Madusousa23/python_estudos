"""Enunciado:
Crie uma função chamada listar_frutas() que peça ao usuário para digitar 5 frutas e armazene em uma lista. Depois, mostre todas as frutas digitadas."""

frutas =[]
def listar_frutas():
    for i in range (1,6):
        fruta = str(input(f"Digite a fruta {i}: "))
        frutas.append(fruta)
    print("lista : ",frutas)

listar_frutas()
