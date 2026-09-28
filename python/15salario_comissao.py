nome = input("Digite seu nome: ")
salario = float(input("Informe seu salário: "))
vendas = float(input("Informe o valor arrecadado em vendas: "))
comissao = vendas * (15/100)
salario_final = salario + comissao

print(f"Nome do funcionário: {nome}")
print(f"Salário Fixo: R${salario:.2f}")
print(f"Salário Final: R${salario_final:.2f}")
