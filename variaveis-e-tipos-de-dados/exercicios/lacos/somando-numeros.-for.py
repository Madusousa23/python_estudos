"""Somando números
Peça 5 números ao usuário (usando input) e mostre a soma total no final."""

print("Entre com 5 números...")


mult=0
for i in range(1,6):
    soma=int(input("Entre com o número {}: ".format(i)))
    mult = mult + soma
print("A soma = ",mult)
