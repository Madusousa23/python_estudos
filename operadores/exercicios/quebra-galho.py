"""Exercício 2: Quebra-Galho
Um pintor cobra R$ 80 por dia de trabalho. Peça quantos dias ele trabalhou e calcule o salário."""

dia_trabalho=80.00

dias=int(input("Quantos dias ele vai trabalhar? "))

sal= dias*dia_trabalho

print("Dias trabalhados: ",dias)
print("Total: R${:.2f}".format(sal))