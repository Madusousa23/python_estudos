"""Contar até o número digitado
Peça um número ao usuário e conte de 1 até esse número."""

num=int(input("Entre com um número: "))

cont = 1

if cont <= num :
    for i in range(0,num):
        cont = i + 1
        print("{}...".format(cont))
