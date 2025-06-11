"""Um celular está com bateria de 30%. A cada hora de carregamento ele sobe 25%.
Pergunte quantas horas ele carregou e diga a bateria atual (máximo 100%)."""

bateria_atual=int(input("Quantos porcentos estava a bateria? no começo "))

horas=float(input("Quantas horas ele carregou ? "))

total_horas= horas * 25

total_bateria = total_horas + bateria_atual

if total_bateria >= 100 :
    print("100%"+" carregado")
else :
    print("Sua bateria está com {}%".format(total_bateria))


