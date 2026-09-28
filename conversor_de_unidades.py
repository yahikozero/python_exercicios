while True:
  print("=== CONVERSOR DE UNIDADES ===")

  print(" 1 - Metros para centímetros")
  print(" 2 - Centímetros para metros")
  print(" 3 - Quilômetros para metros")
  print(" 4 - Celsius para Fahrenheit")
  print(" 5 - Sair")

  opcao = int(input("Escolha uma opção: "))


  if(opcao == 5):
    print("Bye, bye...")
    break

  if (opcao in (1, 2, 3, 4)):
    valor = float(input("Insira o valor a ser convertido:"))
    if (opcao == 1):
      resultado = valor * 100
      print(f"{valor}m é equivalente a {resultado}cm  ")
    elif (opcao == 2):
      resultado = valor / 100
      print(f"{valor}cm é equivalente a {resultado}m  ")
    elif (opcao == 3):
      resultado = valor * 1000
      print(f"{valor}km é equivalente a {resultado}m  ")
    elif (opcao == 4):
      resultado = (valor * 9 / 5) + 32
      print(f"{valor}°C é equivalente a {resultado}F  ")
  else:
    print("Opção inválida!")