import lib_list_alunos

list_alunos = []

while True:
    print("======== CADASTRO DE ALUNOS ========")
    print("==   1 - Inserir aluno            ==")
    print("==   2 - Exibir alunos            ==")
    print("==   3 - Consultar aluno          ==")
    print("==   4 - Alterar nome do aluno    ==")
    print("==   5 - Excluir TODOS os alunos  ==")
    print("==   6 - Excluir aluno            ==")
    print("==   7 - Sair                     ==")
    print("====================================")

    try:
        opcao = int(input("Digite uma opção de 1-7: "))

        if (opcao == 1):
            aluno = input("Digite o nome do aluno: ")
            lib_list_alunos.inserir_aluno(list_alunos, aluno)

        elif (opcao == 2):
            lib_list_alunos.exibir_aluno(list_alunos)

        elif (opcao == 3):
            lib_list_alunos.consulta_aluno(list_alunos)

        elif (opcao == 4):
            lib_list_alunos.alterar_aluno(list_alunos)

        elif(opcao == 5):
            lib_list_alunos.excluir_todos(list_alunos)

        elif (opcao == 6):
            lib_list_alunos.excluir_aluno(list_alunos)

        elif (opcao == 7):
            print("== F i m  d o  p r o g r a m a ==")
            break
        
        else:
            print("Insira uma das opções de 1-7!")
    
    except ValueError:
        print("Insira uma das opções de 1-7!")