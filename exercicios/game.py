"""Peça dois valores: pontos do jogador 1 e pontos do jogador 2. Mostre quem venceu ou se deu empate."""

print("Jogador 1...")
pontos1=int(input("Entre com os pontos :"))

print("Jogador 2...")
pontos2=int(input("Entre com os pontos :"))

if pontos1 > pontos2 :
    print("Jogar 1 venceu !")
elif pontos2 > pontos1 :
    print("Jogador 2 venceu !")
else :
    print("Empate")