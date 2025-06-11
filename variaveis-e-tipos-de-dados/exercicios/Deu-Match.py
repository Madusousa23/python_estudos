"""Joana vai sair com Pedro. Ela gosta de números pares e ele de ímpares.
Peça um número e diga se ele é par (Joana vai gostar) ou ímpar (Pedro vai gostar)."""

numero=int(input("Entre com um número: "))

if numero % 2 == 0 :
    print("É par")
    print("Joana vai Gostar")
elif numero % 2 == 1:
    print("É impar")
    print("Pedro vai gostar")