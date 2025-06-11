"""Peça o salário atual de um funcionário e calcule o novo salário com um aumento de 15%."""

salario_atual=float(input("Entre com o seu salário: "))

aumento = salario_atual * 0.15

novo_salario = salario_atual + aumento 

print("Salário atual : {}".format(salario_atual))

print("Salario novo com aumento de 15% : {}".format(novo_salario))