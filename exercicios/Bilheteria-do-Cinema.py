"""Uma pessoa quer ir ao cinema com um amigo. O ingresso custa R$ 35. Peça quanto cada um tem na carteira e diga se juntos conseguem comprar dois ingressos.
(Dica: entrada de dois valores e soma)"""

pessoa1=float(input("Quanto você tem na carteira R$ ?"))

pessoa2=float(input("Quanto você tem na carteira ? "))

qtd_ingresso = int(input("Quantos ingressos gostaria de comprar ?"))

ingresso = 35.00 * qtd_ingresso

soma = pessoa1 + pessoa2

print("Seu saldo é de: {:.2f}".format(soma))

if soma >=  ingresso :
    print("Vocês podem comprar {} ingressos".format(qtd_ingresso))


else:
    print("Infelizmente vocês não podem comprar {} ingressos".format(qtd_ingresso))