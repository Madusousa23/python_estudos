"""Crie uma função que peça a senha do usuário até ele digitar a senha correta (“python123”)."""

senha=str(input("Entre com uma senha: "))
senha_correta = "python123"

def descubra (senha):
    if senha != senha_correta:
        print("Senha incorreta")
    else : 
        print("Acesso permitido")

descubra(senha)