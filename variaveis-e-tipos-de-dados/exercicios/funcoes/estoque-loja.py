"""Crie uma função controle_estoque() que receba o nome e a quantidade de 3 produtos (entrada do usuário). Para cada um, verifique:

Se a quantidade é menor que 5, imprima: "Produto [nome] com estoque baixo".

Senão, diga: "Estoque de [nome] está ok".
No fim, mostre o total geral de unidades somadas."""





def controle_estoque():
    geral=0
    for i in range (0,3):
        nome = input("\nEntre com o nome do produto: ")

        qtd = int(input("Entre com a quantidade em estoque: "))

        if qtd < 5 :
            print("Produto" ,nome, "com estoque baixo")
        else :
            print("Estoque de ", nome, "está ok")
    geral = qtd + i #terminar

controle_estoque()
        