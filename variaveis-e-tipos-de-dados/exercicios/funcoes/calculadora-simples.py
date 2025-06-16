"""Crie uma função que receba dois números e uma operação (+, -, * ou /) e retorne o resultado."""

n1 = int(input("Entre com um número: "))
n2 = int(input("Entre com o segundo número : "))

def soma (n1,n2):
    if n1 > n2 :
        resultado = n1 + n2
        print("{} + {} = {}".format(n1,n2,resultado))
    else :
        resultado = n2 + n1
        print("{} + {} = {}".format(n2,n1,resultado))

def mult (n1,n2):
    resultado = n1 * n2 
    print("{} x {} = {} ".format(n1,n2,resultado))

def divisao (n1,n2):
    if n1 > n2 :
        resultado = n1 / n2
        print("{} / {} = {}".format(n1,n2,resultado))
    else :
        resultado = n2 / n1
        print("{} / {} = {}".format(n2,n1,resultado))

def sub (n1,n2):
    if n1 > n2 :
        resultado = n1 - n2
        print("{} - {} = {}".format(n1,n2,resultado))
    else :
        resultado = n2 - n1
        print("{} - {} = {}".format(n2,n1,resultado))

soma(n1,n2)
mult(n1,n2)
divisao(n1,n2)
sub(n1,n2)


