"""Vamos fazer um programa que pergunta sua idade e decide se você pode andar de montanha-russa:
"""

idade=int(input("Quantos anos você tem? "))
altura=float(input("Qual a sua altura?" ))

pode_andar = (idade >= 12) and (altura >= 1.40)

print("Você pode andar na montanha russa ?", pode_andar)