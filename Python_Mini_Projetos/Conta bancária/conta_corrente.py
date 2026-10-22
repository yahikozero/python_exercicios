from lib_c_corrente import *

while True:

    print("***************************")
    print("** 1) Depósito na Conta  **")
    print("** 2) Saque da Conta     **")
    print("** 3) Extrato da Conta   **")
    print("** 4) Saldo da Conta     **")
    print("** 5) Sair               **")
    print("***************************")

    try:
        opcao = int(input("Digite uma opção: "))

        if (opcao == 1):
            
            try:
                valor = float(input("Digite o valor a ser depositado: "))
    
                depositar(valor)

                input("** Pressione ENTER para voltar ao MENU **")
            
            except ValueError:
                print("Valor inválido, tente novamente!")
                input("** Pressione ENTER para voltar ao MENU **")

        elif (opcao == 2):

            try:
                valor = float(input("Digite o valor do saque: "))

                sacar(valor)
                
                input("** Pressione ENTER para voltar ao MENU **")

            except ValueError:
                print("Valor inválido, tente novamente!")
                input("** Pressione ENTER para voltar ao MENU **")

        elif (opcao == 3):

            extrato_cc()
            input("** Pressione ENTER para voltar ao MENU **")

        elif(opcao == 4):

            saldo_cc()
            input("** Pressione ENTER para voltar ao MENU **")

        elif(opcao == 5):

            print("F i m  d o  p r o g r a m a !")
            break

        else:
            print("Opção inválida! \nDigite uma das opções do menu!")
            input("** Pressione ENTER para voltar ao MENU **")

    except ValueError:
        
        print("Opção inválida! \nDigite um dos valores numéricos do MENU!")
        input("** Pressione ENTER para voltar ao MENU **")