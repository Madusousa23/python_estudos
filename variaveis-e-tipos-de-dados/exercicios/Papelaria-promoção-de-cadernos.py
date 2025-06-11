"""Um caderno custa R$ 12,00.
Se forem comprados mais de 10 cadernos, aplica-se um desconto de 25% no valor total.
Mostre quanto será pago com ou sem desconto.
"""

unidade = 12.00

qtd=int(input("Entre com a quantidade de cardenos compradas : "))

total= unidade * qtd

if qtd >= 10 : 
    print("Você conseguiu 25%"+" de desconto")
    desconto = total * 0.25
    valor_final = total - desconto
    print("Total com DESCONTO: {:.2f}".format(valor_final))
else :
    print("Infelizmente você não conseguiu desconto")
    print("Total compra : {:.2f}".format(total))