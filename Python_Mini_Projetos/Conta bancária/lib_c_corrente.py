saldo = 0
extratocc = ""

def depositar(valor):
    global saldo
    global extratocc

    if(valor <= 0):
        print("Valor inválido, tente novamente!")

        return

    deposito_efetuado = f"\n- Depoisto de R$ {valor:.2f} efetuado com sucesso!"

    saldo += valor
    extratocc += deposito_efetuado
    print(deposito_efetuado)
    print(f"- Saldo atual: R$ {saldo:.2f}.")

    return

def sacar(valor):
    global saldo
    global extratocc

    if(valor <= 0):
        print("Valor inválido, tente novamente!")

        return
    
    elif (valor > saldo):
        print("- Saldo insuficiente!")
        print(f"- Saldo atual: R$ {saldo:.2f}.")

        return

    else:    
        saque_efetuado = f"\n- Saque de R$ {valor:.2f} efetuado com sucesso!"

        saldo -= valor
        extratocc += saque_efetuado
        print(saque_efetuado)
        print(f"- Saldo atual: R$ {saldo:.2f}.")

        return

def extrato_cc():

    print(extratocc)
    print(f"- Saldo atual: R$ {saldo:.2f}.")

    return

def saldo_cc():

    print(f"- Saldo atual: R$ {saldo:.2f}.")

    return
