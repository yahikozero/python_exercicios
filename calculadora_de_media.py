print("=== Calculadora de Média ===")

soma = 0
quantidade = 0

while True:
  nota = float(input("Insira uma nota e para finalizar digite -1: "))

  if (nota == -1):
    break

  soma = soma + nota
  quantidade = quantidade + 1

if (quantidade == 0):
  print("Programa finalizado!")
else:
  media_final = soma / quantidade
  print(f"Sua média final é {media_final:.2f}")