tempo = float (input ("Informe o tempo de aplicação:"))
capital_inicial =  float (input ("Informe o capital inicial:"))
juros = int (input ("Informe o juros:"))

montante = capital_inicial * (1 + (juros / 100)) * tempo

print (f"O montante é: R${montante}")