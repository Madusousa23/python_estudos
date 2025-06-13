"""Senha secreta com while
Peça uma senha até o usuário digitar “python123”.
Diga “Senha incorreta” se ele errar e “Acesso permitido” quando acertar."""

print("Entre com uma senha de 9 digitos...")



tentativa=str(input("Entre com a senha: "))

while tentativa != "python123":
    print("\nSenha incorreta")
    tentativa=str(input("Entre com a senha: "))
    if tentativa == "python123":
        print("Acesso permitido")

    


