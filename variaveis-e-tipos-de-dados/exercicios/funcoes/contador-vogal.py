"""Enunciado:
Crie uma função contar_vogais() que peça uma palavra ao usuário e mostre quantas vogais existem nela. Não diferencie maiúsculas de minúsculas."""

def contar_vogais():
    word=str(input("Entre com uma palavra: "))
    for i in range (0,word):
        print("Letra 1 : {}".format(i))
        if i == "a" or i == "A":
            a+=i
            print("Letra A: {}".format(a))
        elif i == "e" or i== "E":
            e+=i
            print("Letra E: {}".format(e))
        elif i == "i" or i=="I":
            letrai+=i
            print("Letra I: {}".format(letrai))
        elif i == "o" or i=="O":
            o+=i
            print("Letra O: {}".format(o))
        elif i == "u" or i=="U":
            o+=i
            print("Letra U: {}".format(o))

contar_vogais()
        