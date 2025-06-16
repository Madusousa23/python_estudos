""" Soma de Números
Crie uma função que peça 5 números ao usuário (usando loop) e mostre a soma total no final."""

def tabela ():
    soma=0
    for i in range (0,5):
        resultado=int(input("Entre com o número:"))
        soma += resultado
        
    print("Soma = {}".format(soma))

tabela()