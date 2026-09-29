import random

rol_soma = [] 
atributo_final = []
for i in range (6):
    resultados = []

    #rola os 4d6
    for dados in range (4):
        rolagens = random.randint(1, 6)
        resultados.append(rolagens)
    menor = min(resultados)
    soma = sum(resultados) - menor
    rol_soma.append(soma)

    if (soma <= 7):
        atributo_final.append(-2)
    elif (soma <=9):
        atributo_final.append(-1)
    elif (soma <= 11):
        atributo_final.append(0)
    elif (soma <= 13):
        atributo_final.append(1)
    elif (soma <= 15):
        atributo_final.append(2)
    elif (soma <= 17):
        atributo_final.append(3)
    else:
        atributo_final.append(4)
print(f"Atributos Iniciais: {atributo_final}")    
#rerolagem de atributo se soma menor que 6
while True:
    menor_atributo = min(atributo_final)
    posicao = atributo_final.index(menor_atributo)
    soma_final = sum(atributo_final)

    if (soma_final >= 6):
        break

    if (soma_final < 6):
        resultado_reroll = []
        for dados in range (4):
            reroll = random.randint(1, 6)
            resultado_reroll.append(reroll)
        menor_reroll = min(resultado_reroll)
        soma_reroll = sum(resultado_reroll) - menor_reroll

    if (soma_reroll <= 7):
        atributo_final[posicao] = -2    
    elif (soma_reroll <=9):
        atributo_final[posicao] = -1
    elif (soma_reroll <= 11):
        atributo_final[posicao] = 0
    elif (soma_reroll <= 13):
        atributo_final[posicao] = 1
    elif (soma_reroll <= 15):
        atributo_final[posicao] = 2
    elif (soma_reroll <= 17):
        atributo_final[posicao] = 3
    else:
        atributo_final[posicao] = 4
    
print(f"Atributos finais {atributo_final}")