def inserir_aluno(lista, aluno):
    lista.append(aluno)

def exibir_aluno(lista):
    if (lista):
        for i in range(len(lista)):
            print(f"\n {i + 1} - {lista[i]}")
    else:
        print("Lista vazia!")

def consulta_aluno(lista):
    consulta = input("Insira o nome ou sobrenome que deseja pesquisar: ")
    encontrou = False

    for i in range(len(lista)):
        if (lista[i].find(consulta) != -1):
            print(f"Aluno encontrado no índice {i + 1}: {lista[i]}")
            encontrou = True

    if (encontrou == False):
        print(f"{consulta} não encontrado!")

def alterar_aluno(lista):
    numero_aluno = int(input("Insira o número do aluno que deseja alterar: "))
    indice = numero_aluno - 1

    if (indice >= 0 and indice < len(lista)):
        lista[indice] = input("Insira o novo nome do aluno: ")
        print(f"Novo nome inserido no índice {indice}: {lista[indice]}")
        
    else:
        print("Aluno não encontrado!")

def excluir_todos(lista):
    conf = input("Realmente deseja excluir TODOS os alunos a lista? (S / N): ")

    if (conf == "s") or (conf == "S"):
        lista.clear()
    else:
        return

def excluir_aluno(lista):
    exibir_aluno(lista)
    numero_aluno = int(input("Insira o número do aluno que deseja excluir: "))
    indice = numero_aluno - 1
    
    if (indice >= 0 and indice < len(lista)):
        conf = input(f"Tem certeza que deseja exluir o aluno? {lista[indice]} (S /N): ")
        if (conf == "s") or (conf == "S"):
            lista.pop(indice)
            print(f"Aluno excluído com sucesso!")
        
        else:
    
            return
    else:
        print("Aluno não encontrado!")