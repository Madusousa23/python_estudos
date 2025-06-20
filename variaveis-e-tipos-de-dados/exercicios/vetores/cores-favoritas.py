"""Peça para o usuário digitar suas 3 cores favoritas. Depois, mostre a lista com os índices, assim:"""
lista = []
for i in range(1,4):
    cor=str(input(f"Entre com a cor {i}: "))
    lista.append(cor)
for cor in range (len(lista)):
    print("Na posição",cor ," está :",lista[cor])

