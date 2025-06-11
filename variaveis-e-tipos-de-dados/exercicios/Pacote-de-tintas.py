"""Uma lata de tinta custa R$ 80,00.
Se forem compradas mais de 2 latas, a loja dá 10% de desconto no valor total.
Solicite a quantidade e exiba o valor com ou sem o desconto."""

unidade = 80.00

qtd=int(input("Entre com a quantidade comprada : "))

total = qtd * unidade

if qtd >= 2 :
    print("Você ganhou 10%"+" de desconto !!!")
    desconto = total * 0.1
    valor_final = total - desconto
    print("Total compra :{:.2f}".format(valor_final))
else :
    print("Infelizmente você não conseguiu desconto na sua compra")
    print("Total: {:.2f}".format(total))