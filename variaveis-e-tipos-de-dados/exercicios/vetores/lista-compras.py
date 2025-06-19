"""Peça ao usuário para digitar 5 itens que ele quer comprar. Guarde tudo em uma lista e depois mostre cada item com a frase:

"Você precisa comprar: [item]"""

lista = []

for i in range (1,6):
    itens=str(input(f"Digite o item {i}: "))
    lista.append(itens)
print("Você precisa comprar: ", lista)
