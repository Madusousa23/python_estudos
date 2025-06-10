"""Peça ao usuário para digitar seu nome (str), idade (int), altura (float) e cor favorita (str). Armazene esses valores em variáveis e crie uma frase concatenada com essas informações."""

nome=(input("Digite seu nome: "))
idade=int(input("Digite sua idade: "))
altura=float(input("Digite sua altura: "))
cor=(input("Digite sua cor favorita: "))

print("Olá, ",nome,"! Você tem ", idade, "Anos, e mede", altura,"M e sua cor favorita é ", cor)