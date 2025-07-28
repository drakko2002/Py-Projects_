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

def atualiza_tarefa(tarefas):
    
    

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
        try: #Ao invés de fazer uma única variável, prefiro colocar uma lista como limitadora.
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
                #O bloco try/except serve bem ao propósito.
        except ValueError:
            print("O valor digitado está incorreto!")
            continue