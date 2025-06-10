"""🧪 Exercício 2 – Compras no mercado
Crie variáveis para:

Nome do produto (str)

Quantidade comprada (int)

Preço por unidade (float)

Se está em promoção (bool)

Depois, mostre uma frase com tudo isso e diga quanto vai pagar no total (dica: total = quantidade * preço)."""

produto = "carne"
qtd_comprada = 2
preco_unidade = 30.99
promocao = False
total = qtd_comprada*preco_unidade

print("Fui ao mercado e comprei", produto, ", comprei apenas", qtd_comprada, ". Ela saiu por : $",preco_unidade, "Não estava em promoção",promocao,". Então o total foi de: ",total)
