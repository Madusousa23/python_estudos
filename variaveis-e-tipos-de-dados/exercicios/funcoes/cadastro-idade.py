"""Crie uma função chamada verificar_maioridade() que pergunte a idade de 5 pessoas. Para cada uma, informe se é maior de idade (18 anos ou mais) ou menor de idade. Ao final, mostre quantas pessoas são maiores de idade."""

def verificar_maioridade ():
    maior_idade =0
    for i in range (0,5):
        nome = input("\nEntre com seu nome: ")
        idade=int(input("Entre com a sua idade {}:".format(nome)))
        if idade >=18 :
            print("{} é Maior de idade".format(nome))

            maior_idade += 1
            
        else :
            print("{} Menor de idade".format(nome))
    print("\nMaiores de 18 anos = {}".format(maior_idade))

verificar_maioridade ()
