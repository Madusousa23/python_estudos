""" 6. Contagem Regressiva
Crie uma função que receba um número e faça uma contagem regressiva até 0."""

num=int(input("Entre com um número: "))

def contagem (num):
    cont=1
    while num >= cont :
        print("{}...".format(cont))
        cont = cont + 1

contagem (num)