"""Cada par de tênis custa R$ 150,00.
Comprando 3 ou mais pares, o cliente recebe 20% de desconto no total.
Calcule e informe o valor final a ser pago."""

unidade = 150.00

qtd=int(input("Entre com a quantidade comprada: "))

total = unidade * qtd

if qtd >= 3 :
    print("Você conseguiu 20%"+" de desconto")

    desconto = total * 0.2
    valor_final = total - desconto

    print("Total compra com DESCONTO: {:.2f}".format(valor_final))
else:
    print("Infelimente você não conseguiu desconto")
    print("total:{:.2f}".format(total))