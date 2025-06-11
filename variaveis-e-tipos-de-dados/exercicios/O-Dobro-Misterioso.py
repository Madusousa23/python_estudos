"""Um sábio disse: “Darei um desafio. Pense em um número... dobre esse número, depois some 10 e divida por 2”.
Mostre o resultado final do desafio com o número pensado pelo usuário."""

print("Darei um desafio. Pense em um número... ")

numero=int(input("Pensou ? Qual é : "))

print("Vamos dobrar esse número....")
print("")



dobro = numero * 2

print("Agora, vamos somar com 10...")
print("")

soma = dobro + 10

print("Agora vamos dividir por 2...")
print("")

divisao= soma/2

print("O número {}".format(numero))
print("Virou: {}".format(divisao))