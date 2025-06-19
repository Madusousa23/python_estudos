"""Crie uma lista com 3 nomes fixos. Depois, pergunte ao usuário qual nome ele quer remover e mostre a nova lista."""

lista = []

lista.append("Maria")
lista.append("Vanessa")
lista.append("João")

print("Lista:", lista)

remover=(input("Qual nome você deseja remover: "))

if remover == lista[0]:
    lista.remove("Maria")
elif remover == lista[1]:
    lista.remove("Vanessa")
else:
    lista.remove("João")

print("Lista atualizada",lista)