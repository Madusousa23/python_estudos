"""Crie uma função que peça ao usuário três notas, calcule a média e diga se ele foi aprovado (média ≥ 7)."""

nota1=int(input("Entre com a nota 1: "))
nota2=int(input("Entre com a nota 2: "))
nota3=int(input("Entre com a nota 3: "))

def boletim(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3)/3
    if media>=7:
        print("Aprovado")
    else :
        print("Reprovado")











boletim(nota1,nota2,nota3)