"""O pacote de viagem custa R$ 4.000. A pessoa pode parcelar em até 10 vezes sem juros. Peça a quantidade de parcelas desejadas e mostre o valor de cada uma."""

pacote = 4000

print("Você pode parcelar em até 10x sem juros...")

parcelas=int(input("Quantas parcelas deseja :"))

if parcelas <= 10    :
    total = pacote / parcelas
    print("Cada parcela de {}x vai sair por : R${:.2f} ".format(parcelas,total))
elif parcelas > 10:
    print("opção inválida")
