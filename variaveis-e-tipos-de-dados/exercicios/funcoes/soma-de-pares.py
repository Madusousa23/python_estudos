"""Enunciado:
Crie uma função chamada soma_pares() que receba um número inteiro n e some todos os números pares de 0 até n (inclusive). Mostre o resultado no final."""

def soma_pares():
    soma=0
    num = int (input("Entre com um número inteiro : "))
    
    for i in range (0,num+1):
        if i % 2 == 0 :
            print("{}".format(i))
            soma+=i
    print("A soma: {}".format(soma))
            




soma_pares()
