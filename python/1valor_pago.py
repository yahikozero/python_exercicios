#calcular o valor do produto

valor_produto = float(input("Digite o valor original do produto: "))
desconto = float(input("Digite o desconto do produto: "))

valor_final = valor_produto - (valor_produto * (desconto / 100))

print(f"O produto com o valor original de R${valor_produto:.2f} com o desconto de {desconto}%, fica R${valor_final:.2f}")
