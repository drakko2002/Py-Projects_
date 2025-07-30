def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso.")
    return


tarefas = [] 
#abrindo agora uma lista vazia fora da funçao adicionar_tarefa.


def visualiza_tarefa(tarefas):
    print(f"Lista de Tarefas: \n")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else "☓"
        nome_tarefa = tarefa["tarefa"] #Acessando a chave do dicionário tarefa tarefas.
        print(f"{indice} - [{status}] {nome_tarefa}")
    return


def atualiza_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    ajuste_indice = indice_tarefa - 1  #Tratando tamanho do indice da tarefa
    if ajuste_indice >= 0 and ajuste_indice <= len(tarefas)
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    tarefas[indice_tarefa]["tarefa"] = novo_nome_tarefa
    #A lista sempre começa no indice 0
    return
    

while True: 
#Meu deus do céu, como eu esqueci de deixar o While fora da funçao?
        print("\nMenu de Gerenciador de Lista de Tarefas")
        print("1 - Adicionar uma tarefa;")
        print("2 - Visualizar lista de tarefas;")
        print("3 - Atualizar uma tarefa;")
        print("4 - Completar tarefa;")
        print("5 - Deletar tarefas completadas;")
        print("6 - Sair do programa.")
        opcao = [1, 2, 3, 4, 5, 6]
        try:  #Ao invés de fazer uma única variável, prefiro colocar uma lista como limitadora.
            selecionaOpcao = int(input("Digite opcao desejada: \n"))
            if selecionaOpcao not in opcao:
                print("Digite uma opcao válida!")
                selecionaOpcao
            match selecionaOpcao:
                case 1:
                    print("Voce selecionou adicionar tarefa! \n")
                    nome_tarefa = input("Digite o nome da tarefa: ")
                    adicionar_tarefa(tarefas, nome_tarefa)
                case 2:
                    print("Voce selecionou visualizar as tarefas!")
                    visualiza_tarefa(tarefas)
                case 3:
                    print("Voce selecionou editar tarefa!")
                    visualiza_tarefa(tarefas) #Pro usuário ver quais tarefas estao na lista
                    #Mas pra chamar a funçao atualiza_tarefa, precisamos definir duas variáveis
                    #antes que estas possam ser utilizadas como argumentos da funçao
                    indice_tarefa = int(input("indice da tarefa que deseja editar: "))
                    novo_nome_tarefa = str(input("Novo nome da tarefa: "))
                    #Penso em adicionar uma variável de informaçao da tarefa também
                    atualiza_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
                #O bloco try/except serve bem ao propósito.
        except ValueError:
            print("O valor digitado está incorreto!")
            continue