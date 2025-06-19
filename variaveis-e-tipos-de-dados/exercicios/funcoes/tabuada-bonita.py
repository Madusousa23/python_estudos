"""Enunciado:
Crie uma função chamada tabuada_formatada() que receba um número inteiro como parâmetro e exiba sua tabuada de 1 a 10, com uma formatação organizada (ex: 2 x 1 = 2)."""

num = int(input("Entre com um número inteiro: "))
def tabuada_formatada(num):
    for i in range (0,11):
        mult= num * i
        print("{} x {} = {}".format(num,i,mult))

tabuada_formatada(num)
