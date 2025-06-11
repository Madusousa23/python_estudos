"""5. Loja de Brinquedos (Desconto Simples)
Uma loja dá 10% de desconto para compras acima de R$ 50,00.
Peça ao usuário digitar o valor da compra e calcule o valor final com desconto (se aplicável)."""

valor_compra=float(input("Digite o valor da compra: "))



if valor_compra > 50 : 
    desconto= valor_compra * 0.10
    valor_compra_desconto = valor_compra - desconto
    print("Sua compra com desconto ficou : " , valor_compra_desconto)
else:
    print("Você não atingiu o valor para desconto, Sua compra saiu por :", valor_compra)