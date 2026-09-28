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

while True:
  print("\n===ROLADOR DE DADOS===")

  for opcao, faces in dados.items():
    print(f"{opcao} - Rolar um d{faces}")
  print("9 - Sair")
  
  try:
      opcao = int(input("Escolha uma opção: "))
  except ValueError:
      print("Opção inválida!")
      continue
   
  if (opcao == 9):
    break

  if (opcao not in dados and opcao):
    print("Opção inválida!")
    continue

  faces = dados[opcao]

  try:
    quantidade = int(input("Quantos dados deseja rolar? "))
  except ValueError:
    print("Quantidade inválida!")
    continue

  rolagens = []
  rolagens_txt = ""

  total = 0

  for i in range(quantidade):
    resultado = random.randint(1, faces)
    rolagens.append(resultado)
    if i > 0:
      rolagens_txt += ", " 
    total += resultado
    rolagens_txt += str(rolagens[i])

  print(f"Você rolou {quantidade}d{faces} resultando em: {rolagens_txt}, para um total de {total}.")