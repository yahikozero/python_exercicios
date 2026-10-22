saldo = 0
extratocc = ""

def depositar():
    global saldo
    global extratocc

    try:
        deposito = float(input("Digite o valor a ser depositado: "))

        if(deposito <= 0):
            print("Valor inválido, tente novamente!")


        else:
            deposito_efetuado = f"\n- Depoisto de R$ {deposito:.2f} efetuado com sucesso!"

            saldo += deposito
            extratocc += deposito_efetuado
            print(deposito_efetuado)
            print(f"- Saldo atual: R$ {saldo:.2f}.")

    except ValueError:
        print("Valor inválido, tente novamente!")


    return

def sacar():
    global saldo
    global extratocc

    try:
        saque = float(input("Digite o valor a ser sacado: "))

        if (saldo < saque):
            print("- Saldo insuficiente!")
            print(f"- Saldo atual: R$ {saldo:.2f}.")

            return
        
        elif(saque <= 0):
            print("Valor inválido, tente novamente!")

            return
        
        else:
            saque_efetuado = f"\n- Saque de R$ {saque:.2f} efetuado com sucesso!"

            saldo -= saque
            extratocc += saque_efetuado
            print(saque_efetuado)
            print(f"- Saldo atual: R$ {saldo:.2f}.")

    except ValueError:
        print("Valor inválido, tente novamente!")



    return

def extrato_cc():
    global saldo
    global extratocc

    print(extratocc)
    print(f"- Saldo atual: R$ {saldo:.2f}.")

    return

def saldo_cc():
    global saldo
    global extratocc

    print(f"- Saldo atual: R$ {saldo:.2f}.")

    return
