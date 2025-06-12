"""Cada caixa custa R$ 8. Se a pessoa comprar um número par de caixas, ela ganha 1 caixa grátis. Diga quantas caixas ela vai levar no total."""

unidade = 8

caixas=int(input("Quantas caixas deseja : "))

total = caixas * unidade
print("Total da compra : R$", total)
print("")

if caixas % 2 == 0 :
    print("Você ganhou 1 caixa de cortesia")

    print("Total caixas: ", caixas + 1)
else:
    print("Total caixas: ", caixas)


