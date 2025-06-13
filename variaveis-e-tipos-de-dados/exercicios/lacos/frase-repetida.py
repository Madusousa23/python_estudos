"""Peça um número ao usuário e repita a frase “Estudando Python!” esse número de vezes."""

print("Escolha um número que deseja repetir a frase")

numero=int(input("Entre com o número:"))

impressao=1
while impressao <= numero :
    print("{}: Estudando python".format(impressao))
    impressao = impressao + 1
    
