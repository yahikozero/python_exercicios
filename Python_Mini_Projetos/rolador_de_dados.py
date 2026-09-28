import random

dados = {
    1: 3,
    2: 4,
    3: 6,
    4: 8,
    5: 10,
    6: 12,
    7: 20,
    8: 100
}

print("9 - Sair")

while True:
  print("\n===ROLADOR DE DADOS===")

  for opcao, faces in dados.items():
    print(f"{opcao} - Rolar um d{faces}")
  print("9 - Sair")

  opcao = int(input("Escolha uma opção: "))

  if (opcao == 9):
    break

  if (opcao not in dados):
    print("Opção inválida!")
    continue

  faces = dados[opcao]
  resultado = random.randint(1, faces)

  print(f"Rolou um d{faces}, resultado: {resultado}")