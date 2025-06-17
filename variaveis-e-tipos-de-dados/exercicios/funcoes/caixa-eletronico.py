"""Enunciado:
Crie uma função chamada simular_saque() que pergunte o valor que o usuário deseja sacar. O saque deve ser feito com as seguintes notas disponíveis: R$ 100, R$ 50, R$ 20, R$ 10 e R$ 2. Mostre quantas notas de cada tipo serão entregues.
Exemplo: para R$ 286 → 2 notas de 100, 1 de 50, 1 de 20, 1 de 10 e 3 de 2."""

def simular_saque():
    valor=int(input("Entre com a quantidade que deseja sacar: "))
    
    sobra=0
    tamanho=0
    tamanho_total=0

    if valor >= 100 :
        tamanho = valor // 100
        tamanho_total = tamanho * 100
        sobra = valor - tamanho_total
        print("Cabem {} notas de 100".format(tamanho))
    if sobra >=50 :
        tamanho = sobra // 50 
        tamanho_total = tamanho * 50
        sobra_total= sobra - tamanho_total
        print("Cabem {} notas de 50".format(tamanho))
    if sobra_total >=20:
        tamanho = sobra_total // 20
        tamanho_total = tamanho * 20
        sobra = sobra_total - tamanho_total
        print("Cabem {} notas de 20".format(tamanho))
    if sobra >= 10:
        tamanho = sobra // 10
        tamanho_total = tamanho * 10
        sobra = sobra - tamanho_total
        print("Cabem {} notas de 10".format(tamanho))
    if sobra >=2:
        tamanho = sobra//2
        tamanho_total = tamanho*2
        sobra= sobra - tamanho_total
        print("Cabem {} notas de 2".format(tamanho))
    if sobra == 0 :
        print("zeramos")
        
simular_saque()


        