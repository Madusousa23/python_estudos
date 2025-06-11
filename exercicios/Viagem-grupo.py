"""Um carro faz 12 km por litro de gasolina. Peça a distância da viagem (km) e calcule quantos litros serão necessários."""

litros = 12

distancia = float(input("Qual a distância que você vai percorrer? "))

litros_necessarios = distancia / litros

print("Distância (KM): ", distancia)
print("Litros necessários: {:.2f} Litros".format(litros_necessarios))