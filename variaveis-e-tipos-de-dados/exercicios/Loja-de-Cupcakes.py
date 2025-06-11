"""Cada cupcake custa R$ 3,75.
Se a pessoa comprar mais de 6 cupcakes, recebe 15% de desconto no valor total.
Peça a quantidade e mostre o valor a pagar (com ou sem desconto)."""

unidade = 3.75

qtd=int(input("Quantos cupcakes deseja : "))

total = qtd * unidade



if qtd >= 6 :
    print("Você conseguiu 15%"+" de desconto")
    desconto = total * 0.15
    valor_final= total - desconto
    print("Total da compra com DESCONTO: {:.2f}".format(valor_final))
else:
    print("Você não atingiu o limite da compra para desconto")
    print("Total da compra :{:.2f}".format(total))