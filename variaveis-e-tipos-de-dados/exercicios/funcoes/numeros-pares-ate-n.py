"""Crie uma função que receba um número N e imprima todos os números pares de 0 até N."""

num=int(input("Entre com um número: "))

def tabela (num):
    for i in range (0,num):
        if i % 2 == 0:
            print("{} PAR".format(i))


tabela(num)

