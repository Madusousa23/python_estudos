"""O preço de um produto é R$ 100. A loja oferece:

10% de desconto à vista

ou 5% de acréscimo para parcelar
Peça a forma de pagamento (1 para à vista, 2 para parcelado) e calcule o valor final."""

produto= 100

qtd=int(input("Quantos produtos deseja : "))
print("")

total = produto * qtd
print("Valor total : ", total)

print("")
pagamento=int(input("Entre com a forma de pagamento : (1 - á vista | 2 = parcelado)"))

if pagamento == 1 :
    print("Parabéns, você ganhou 10%" + " de desconto")

    desconto = total * 0.1
    valor_final = total - desconto
    print("Total com 10%" + " de desconto : ", valor_final)
elif pagamento == 2 :
    print("Terá um acréscimo de 5%")
    print("")
    acrescimo = total * 0.05
    valor_final_acrescimo = total + acrescimo
    print("O total do valor com acréscimo de 5%: ", valor_final_acrescimo)