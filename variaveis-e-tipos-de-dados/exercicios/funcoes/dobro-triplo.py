"""🍰 2. Dobro e Triplo
Crie uma função que receba um número inteiro e mostre o dobro e o triplo desse número."""

numero = int(input("Entre com um número : "))
def dobro (numero):
    num_dobro = numero * 2
    print("O dobro de {} = {} ".format(numero,num_dobro))

def triplo (numero):
    resultado= numero * 3
    print("O triplo de {} = {}".format(numero,resultado))

dobro(numero)
triplo(numero)
