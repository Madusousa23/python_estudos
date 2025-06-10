"""Exercício 5: Divisão de Conta
Peça o valor total da conta de um restaurante e quantas pessoas vão dividir. Calcule quanto cada um deve pagar."""

valor_conta= float(input("Qual o valor total da compra ?"))

pessoas=int(input("Quantas pessoas vão dividir a conta ? "))

total = valor_conta / pessoas

print("Valor total : ", valor_conta)
print("Quantas pessoas vão dividir : ", pessoas)
print("Total da conta para cada : R${:.2f}" .format(total))