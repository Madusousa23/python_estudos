"""Um refri custa R$ 5. Peça quanto dinheiro o usuário tem. Se for suficiente, calcule o troco. Se não for, diga quanto falta."""

refri = 5

dinheiro = float(input("Quanto você tem R$ : "))

if dinheiro > refri :
    troco = dinheiro - refri
    print("Seu troco é de: {:.2} Reais".format(troco))
elif dinheiro == refri :
    print("Você não ganha troco")
else : 
    print("Você não tem dinheiro suficiente")

    falta = refri - dinheiro

    print("Falta : R${:.2f} Reais".format(falta))