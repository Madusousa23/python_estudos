"""Crie um programa que peça dois números ao usuário (um int e um float), realize as quatro operações básicas (soma, subtração, multiplicação e divisão) e mostre os resultados concatenados com strings explicativas."""

inteiro=int(input("Digite um número inteiro: "))
decimal=float(input("Digite um número decimal: "))

soma=inteiro+decimal
divisao=inteiro/decimal
mult=inteiro*decimal
sub=inteiro-decimal

print("A soma dos números ", inteiro, "+", decimal, "=", soma)
print("A Divisão dos números ", inteiro, "/", decimal, "=", divisao)
print("A Multiplicação dos números ", inteiro, "x", decimal, "=", mult)
print("A Subtração dos números ", inteiro, "-", decimal, "=", sub)

