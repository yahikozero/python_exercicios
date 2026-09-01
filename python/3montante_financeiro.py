tempo = float (input ("Informe o tempo de aplicação:"))
capital_inicial =  float (input ("Informe o capital inicial:"))
juros = int (input ("Informe o juros:"))

montante = capital_inicial * (1 + juros) * tempo

print (f"O montante é: R${montante}")