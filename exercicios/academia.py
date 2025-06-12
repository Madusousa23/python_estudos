"""A mensalidade da academia é R$ 150. Se a pessoa tiver menos de 18 anos ou mais de 60, ganha 20% de desconto. Peça a idade e calcule o valor final.
"""

mensalidade = 150

idade=int(input("Entre com a idade : "))

if idade < 18 or idade >=60 :
    desconto = mensalidade * 0.2
    valor_final= mensalidade - desconto
    print ("Você ganha desconto")
    print("Total mensalidade : {:.2f}".format(valor_final))
else:
    print("Você não ganha desconto")
    print("Total mensalidade : {:.2f}".format(mensalidade))