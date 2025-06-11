"""Um aluno fez duas provas. A média para passar é 6.0.
Peça as notas, calcule a média e diga se ele foi:

Aprovado (média ≥ 6)

Em recuperação (média >= 4 e < 6)

Reprovado (média < 4)"""

prova1=float(input("Entre com a nota da primeira prova: "))

prova2=float(input("Entre com a nota da segunda prova: "))

media= (prova1 + prova2)/2

if media >= 6 :
    print("Aprovado")
elif media >= 4 and media < 6 :
    print("Em recuperação")
else:
    print("Reprovado")