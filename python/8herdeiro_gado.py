gados = int(input("Informe a quantidade de cabeças de gado: "))
herdeiros = int(input("Informe a quantidade de herdeiros: "))

divisao = gados // herdeiros
resto = gados % herdeiros

print(f"Ficará para cada herdeiro {divisao} cabeças de gado e sobrará {resto}.")