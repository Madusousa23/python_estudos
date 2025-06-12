""" Uma pizza custa R$ 60. Peça o número de amigos (incluindo o usuário) e diga quanto cada um deve pagar.
""" 

amigos=int(input("Quantos amigos vão participar (incluindo o usuário) ? "))

total = 60/amigos
print("Cada um deve pagar: R${:.2f}".format(total))