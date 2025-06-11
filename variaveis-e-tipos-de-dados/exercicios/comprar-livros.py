"""Um livro custa R$ 25,00.
Se o cliente comprar mais de 4 livros, ele ganha 12% de desconto no total.
Mostre o valor final com ou sem desconto."""

unidade  = 25.00
qtd=int(input("Entre com a quantidade desejada: "))

total = unidade * qtd

if qtd >= 4 :
    print("Você ganhou 12%"+" de desconto")
    desconto = total * 0.12
    valor_final = total - desconto
    print("Total compra : {:.2f}".format(valor_final))
else :
    print("Você não atingiu o valor para desconto")
    print("Total compra :{:.2f}".format(total))