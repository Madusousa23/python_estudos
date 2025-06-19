"""Peça 4 números ao usuário, armazene em uma lista e mostre:

Todos os números digitados

A soma total

A média dos números"""
soma = []
total =0
for i in range(1,5):
    
    num=int(input(f"Entre com o número {i}: "))
    soma.append(num)
    total+=num
print("O total= ",total)
media= total/4
print("O media = ", media)
print("Lista completa = ",soma)




