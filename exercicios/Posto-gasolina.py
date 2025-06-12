"""O litro da gasolina custa R$ 6,20. Peça quantos litros o cliente quer e diga o valor total. Se ele pedir mais de 30L, aplique 5% de desconto."""

litro = 6.20

litros_cliente=float(input("Quantos litros deseja : "))

total = litros_cliente * litro

if litros_cliente >= 30 :
    desconto = total * 0.05
    total_desconto = total - desconto
    print("Você ganhou desconto de 5%")
    print("")
    print("Total : {:.2f}".format(total_desconto))
else:
    print("Total : ", total)
