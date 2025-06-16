""" 4. Tabuada com Função
Crie uma função que receba um número inteiro e imprima sua tabuada de 1 a 10."""

num=int(input("Entre com um número: "))

def tabuada (num):
    for i in range (0,11):
        resul = i * num
        print("{} x {} = {}".format(num,i,resul))

tabuada(num)