"""Enunciado:
Crie uma função chamada calcular_medias() que pergunte as notas de 4 alunos. Depois:

Calcule a média de cada aluno e diga se foi aprovado (média >= 6).

Ao final, mostre a média geral da turma."""

def calcular_medias():
    soma_medias=0
    for i in range (0,4):
        nome=str(input("Nome aluno:"))
        print("Entre com as notas do(a) {}".format(nome))
        nota1=int(input("Entre com a nota 1 : "))
        nota2=int(input("Entre com a nota 2 : "))
        nota3=int(input("Entre com a nota 3 : "))
        nota4=int(input("Entre com a nota 4 : "))

        media = (nota1 + nota2 + nota3 + nota4)/4
        soma_medias+=media

        if media >=6:
            print("Aprovado")
            print("Média: {}".format(media))
        else:
            print("Reprovado")
            print("Média: {}".format(media))
    total=soma_medias/4

    print("Média geral: {}".format(total))

calcular_medias()



    