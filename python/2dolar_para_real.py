#valor em reais do dolar

valor_dolar = float(input("Digite o valor em dólares: "))
valor_cotacao = float(input("Digite a cotação do dia: "))
valor_real = valor_dolar * valor_cotacao

print(f"O valor em reais de ${valor_dolar:.2f} com a cotação de hoje é R${valor_real:.2f}.")
