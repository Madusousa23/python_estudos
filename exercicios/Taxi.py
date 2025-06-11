"""Você vai pegar um táxi e o valor da corrida é calculado assim:
Bandeirada = R$ 5 + R$ 2 por km rodado.
Peça ao usuário a quantidade de km e calcule o valor final da corrida."""

km=float(input("Entre com a quantidade de KM da corrida: "))

km_calculo = 2 * km

bandeirada = 5 + km_calculo

print("Sua corrida sairá por : {:.2f}".format(bandeirada))