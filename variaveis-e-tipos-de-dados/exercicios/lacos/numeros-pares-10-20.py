"""Números pares de 0 a 20
Mostre todos os números pares de 0 até 20."""

print("Imprimindo números...")

for i in range(1,21):
    if i % 2 == 0 :
        print("{} é par".format(i))
    else : 
        print("{} é impar".format(i))
    