"""Peça 6 números e guarde em uma lista. Depois, pergunte ao usuário um número qualquer e diga:

"Esse número está na lista" ou "Esse número NÃO está na lista"

Dica: use in."""
lista = []
for i in range (1,7):
    num=int(input(f"Entre com o número {i}: "))
    lista.append(num)

num_usuario = int(input("Entre com qualquer numero: "))

if num_usuario == lista[0]:
    print("Esse número está na lista")
elif num_usuario == lista[1]:
    print("Esse número está na lista")
elif num_usuario == lista[2]:
    print("Esse número está na lista")
elif num_usuario == lista[3]:
    print("Esse número está na lista")
elif num_usuario == lista[4]:
    print("Esse número está na lista")
elif num_usuario == lista[5]:
    print("Esse número está na lista")
else :
    print("Esse número NÃO está na lista")

print (lista)


