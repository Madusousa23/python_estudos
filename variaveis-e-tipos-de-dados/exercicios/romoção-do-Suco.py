"""Um suco custa R$ 4,50. Se a pessoa comprar mais de 3 sucos, ganha 10% de desconto no total.
Peça a quantidade e diga o valor a pagar (com ou sem desconto)."""

suco = 4.50

qtd_sucos=int(input("Quantos sucos deseja : "))

total = qtd_sucos*suco

print("O total da sua compra SEM DESCONTO: R$ {}".format(total))

if qtd_sucos >= 3:
    desconto = total * 0.10
    valor_final_desc = total - desconto
    print("Você conseguiu 10%"+" de desconto")
    print("O total é de: R${:.2f}".format(valor_final_desc))
else:
    print("Sua compra não alcançou o limite para desconto")