"""Uma lanchonete vende:

X-Burger: R$ 10.00

Refri: R$ 4.50
Peça ao usuário quantos X-Burgers e quantos refris ele quer e calcule o total da conta."""

xburguer = 10.00
refri = 4.50

compra_burguer = int(input("Quantos X-Burgers você deseja ? "))

compra_refri = int(input("Quantos Refrigerantes você deseja? "))

total = (compra_burguer * xburguer) + (compra_refri * refri)

print("O total da sua compra : R${:.2f}".format(total)) #{:.2f} = 2 casas decimais depois da virgula