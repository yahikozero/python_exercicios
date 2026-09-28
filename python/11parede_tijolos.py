import math

altura_parede = float(input("Insira a altura da parede: "))
base_parede = float(input("Insira o comprimento da parede: "))
altura_tijolo = float(input("Insira a altura do tijolo: "))
base_tijolo = float(input("Insira o comprimento do tijolo: "))

converte_altura = altura_parede * 100
converte_base = base_parede * 100

area_parede = converte_base * converte_altura
area_tijolo = base_tijolo * altura_tijolo

total_tijolo = area_parede / area_tijolo

print(f"A quantidade de tijolos necessários para construir a parede é  de: {math.ceil(total_tijolo)} tijolos.")