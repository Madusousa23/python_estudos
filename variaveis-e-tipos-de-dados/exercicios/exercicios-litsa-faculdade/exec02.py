qtd=int(input("Quantos motoristas deseja verificar: "))

cont =0
maior_multas = 0
maior_carteira = 0
total=0
while cont < qtd :
    divida=0
    carteira=int(input("Entre com a carteira do motorista: "))
    num_multas=int(input("Qual a quantidade de multas: "))
    
    if num_multas > maior_multas :
        maior_multas = num_multas
        maior_carteira = carteira

    for i in range(1,num_multas+1):
        multa=int(input("Entre com o valor da multa: "))
        divida+=multa 
    total+=divida
    cont += 1

    print("")
    print("Número motorista: {}".format(carteira))
    print("Número de multas do motorista: {}".format(num_multas))
    print("Valor total: {} ".format(divida))
    print("")
    print("Total: {}".format(total))
    print("O motorista {}, teve maior número de multas".format(carteira))
    print("Número de multas: {}".format(num_multas))

