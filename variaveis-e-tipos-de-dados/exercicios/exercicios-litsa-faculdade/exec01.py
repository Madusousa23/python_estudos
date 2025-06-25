qtd=int(input("Com quantos números deseja entrar: "))

soma=0
mult=1
for i in range (qtd):
    num=int(input("Entre com um número inteiro positivo: "))
    if num % 2 == 1 :
        mult*=num

    elif num % 2 == 0:
        soma+=num
print(f"O produto é: {mult}")
print(f"A soma é: {soma}")
