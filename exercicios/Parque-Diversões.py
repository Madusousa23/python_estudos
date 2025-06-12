"""Para entrar no brinquedo, a pessoa deve ter mais de 1.40m de altura e ser maior de 10 anos. Peça idade e altura e diga se pode entrar.
"""

altura=float(input("Entre com a sua altura : "))

idade=int(input("Entre com a sua idade : "))

if altura >= 1.40 and idade>=10 :
    print("Pode ir no brinquedo")
else: 
    print("Não pode ir no brinquedo")