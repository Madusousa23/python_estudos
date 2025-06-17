"""Enunciado:
Crie uma função chamada calcular_combustivel() que pergunte ao usuário:

Quantos litros ele quer abastecer.

Qual tipo de combustível (álcool ou gasolina).
Considere os preços:

Gasolina: R$ 6,20

Álcool: R$ 4,80
Mostre o valor total. Se forem mais de 30L, aplique 5% de desconto."""

def calcular_combustivel():
    litros=float(input("Entre com a quantidade de gasolina que deseja: "))

    print("Qual tipo de combustível deseja: álcool ou gasolina ?")
    print("1 - gasolina\n2 - Álcool")
    combustivel=int(input("Entre com a escolha: "))

    

    if litros >= 30 and combustivel == 1:
        valor = litros * 6.20
        desc = valor * 0.05
        total = valor - desc 
        print("Você ganhou 5%"+" de desconto")
        print("O total é de : R${}".format(total))
    elif litros >= 30 and combustivel == 2:
        valor = litros * 4.80
        desc = valor * 0.05
        total = valor - desc 
        print("Você ganhou 5%"+" de desconto")
        print("O total é de : R${}".format(total))
    elif litros < 30 and combustivel == 1:
        total = litros * 6.20
        print("Total: R$ {}".format(total))
    elif litros < 30 and combustivel == 2:
        total = litros * 4.80
        print("Total: R${}".format(total))


calcular_combustivel()


        



