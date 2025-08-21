import re


contatos = []
#contato: dict = {
#    "Nome": "",
#    "Sobrenome": "",
#    "Email": "",
#    "Telefone": "",
#    "Favorito": False
#}


def capturar_dados(prompt: str) -> str:
    """Função auxiliar para capturar dados do usuário com validação."""
    while True: 
        try: 
            valor = input(prompt).strip()
            if valor: 
                return valor 
        except KeyboardInterrupt: 
            raise SystemExit("Usuário finalizou o programa.") 
        print("Entrada de dados inválida. Por favor, tente novamente.")
        

def exibir_contato(contatos: list):
    """Exibe as informações dos contatos."""
    print("\nInformações fornecidas:")
    if not contatos: #Aqui, reforçamos a ideia do inverso lógico, onde enfatizamos que a lista está vazia.
        print("Nenhum contato cadastrado.")
    for contato in contatos:
        print(f"Nome: {contato}")


def adicionar_contato():
    """Adiciona um contato à agenda."""
    contato: dict = {
        "Nome": "",
        "Sobrenome": "",
        "Email": "",
        "Telefone": "",
        "Favorito": False
    }
    print("Insira as informações do contato: \n")
    nome = capturar_dados("Digite o nome: ")
    sobrenome = capturar_dados("Digite o sobrenome: ")
    #Bloco de validaçao
    email_valido = False

    while not email_valido:
        email = capturar_dados("Digite o e-mail: ")

        if not email:
            print("Digite um e-mail válido.")
            continue   # volta para o início do loop
        try:
            email_normalizado = normalizar_email(email)
            email_valido = True   # passou na validação
        except Exception as e:
            print(f"Digite um e-mail válido. Erro: {e}")
            if not email:
                email = capturar_dados("Digite um e-mail válido: ")
                continue  # volta para o início do loop

    telefone_valido = False

    while not telefone_valido:
        telefone = capturar_dados("Digite um telefone: ")

        if not telefone:
            print("Digite um telefone válido.")
            continue

        try:
            telefone_normalizado = normalizar_telefone(telefone)
            telefone_valido = True
            #if telefone_valido == True:
            #    break
        except Exception as e:
            print(f"Digite um telefone válido. Erro: {e}")
            continue

    contato.update({
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Email": email_normalizado,
        "Telefone": telefone_normalizado,
        "Favorito": False
    })
    contatos.append(contato)
    print("Contato adicionado com sucesso!")
    exibir_contato(contatos)


def normalizar_telefone(telefone: str) -> str:
    """Normaliza o número de telefone removendo caracteres não numéricos."""
    if not re.match(r'^\d{8,15}$', telefone):
        print("O telefone inserido é inválido.")
        raise ValueError("Telefone inválido.")
    return telefone


def normalizar_email(email: str) -> str:
    """Normaliza o email convertendo para minúsculas."""
    email = email.lower().strip()
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return email
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError("Email inválido.")




def busca_contato():
    print("-- Funçao de busca --")
    print("")
    print("1 - Nome")
    print("2 - Sobrenome")
    print("3 - E-mail")
    print("4 - Telefone")
    busca = int(input("Qual informaçao deseja buscar: "))
    #busca_contato = str(input("Digite a informaçao para buscar: "))
    match busca:
        case 1:
            busca_nome = str(input("Digite o nome: "))
            for c in contatos: #Iterando pela lista de dicionários utilizando pseudonimo "c"
                if c['Nome'] == busca_nome: #Compara a chave ['x'] de cada dicionário da lista com aquela inserida
                    contato = c #Salva o contato obtido dentro de uma variável
                    print(f"Valor encontrado: {contato['Nome']}")
                    print(f"No dicionário: {contato}")
        case 2:
            busca_sobrenome = str(input("Digite o sobrenome: "))
            for c in contatos: #Iterando pela lista de dicionários utilizando pseudonimo "c"
                if c['Sobrenome'] == busca_sobrenome: #Compara a chave ['x'] de cada dicionário da lista com aquela inserida
                    contato = c #Salva o contato obtido dentro de uma variável
                    print(f"Valor encontrado: {contato['Sobrenome']}")
                    print(f"No dicionário: {contato}")
        case 3:
            busca_email = str(input("Digite o e-mail para buscar: "))
            for c in contatos:  #Iterando pela lista de dicionários utilizando pseudonimo "c"
                if c['Email'] == busca_email: #Compara a chave ['x'] de cada dicionário da lista com aquela inserida
                    contato = c #Salva o contato obtido dentro de uma variável
                    print(f"Valor encontrado: {contato['Email']}\n")
                    print(f"No dicionário: {contato}\n")
        case 4:
            busca_telefone = str(input("Digite o telefone: "))
            for c in contatos: #Iterando pela lista de dicionários utilizando pseudonimo "c"
                if c['Telefone'] == busca_telefone: #Compara a chave ['x'] de cada dicionário da lista com aquela inserida
                    contato = c #Salva o contato obtido dentro de uma variável
                    print(f"Valor encontrado: {contato['Telefone']}")
                    print(f"No dicionário: {contato}")

def editar_contato():
    identificador = (input("Digite um e-mail para buscar: "))
    normalizar_email(identificador)
    for c in contatos: 
        if c['Email'] == identificador:
            contato = c
            print(f"Dados do contato: \n")
            print(f"Nome: {contato['Nome']}")
            print(f"Sobrenome: {contato['Sobrenome']}")
            print(f"Email: {contato['Email']}")
            print(f"Telefone: {contato['Telefone']}")
            #return contato
        else:
            print("O contato nao foi encontrado!")
            
#Testar aqui pra ver se está conseguindo acessar o index

#A intençao aqui é acessar os indexes e edita-los a partir do e-mail como chave identificadora do contato.

    print("Selecione qual dado deseja editar!")
    print("1 - Nome; ")
    print("2 - Sobrenome; ")
    print("3 - Email; ")
    print("4 - Telefone")
    while True:
        editar = int(input("Digite o parametro desejado para editar: "))
        if editar not in [1, 2, 3, 4]:
            print("Opção inválida. Tente novamente.")
            return
        match editar:
            case 1:
                nome = capturar_dados("Digite seu nome: ")
                # Verifica se o nome já existe na agenda
                # Se existir, atualiza o nome, caso contrário, informa que não está na agenda
                for c in contatos:
                    if c['Nome'] == nome:
                        print("O valor informado está na agenda!")
                        contato = c
                        nome_novo = capturar_dados("Digite o novo nome: ")
                        
                        print("Nome atualizado com sucesso!")
                    else: #Se o nome não estiver na agenda, informa ao usuário.
                        print("O valor informado nao está na agenda.")
                        return
            case 2:
                sobrenome = capturar_dados("Digite seu sobrenome: ")
                if sobrenome in {contato['Sobrenome']}:
                    print("O valor informado está na agenda.")
                    sobrenome_novo = capturar_dados("Digite o novo sobrenome: ")
                    contato.update({'Sobrenome': sobrenome_novo})
                    print("Sobrenome atualizado com sucesso!")
                else: # Se o sobrenome não estiver na agenda, informa ao usuário.
                    print("O valor informado nao está na agenda.")
                    return
            case 3:
                email = capturar_dados("Digite seu email: ")
                if email in {contato['Email']}:
                    email = normalizar_email(email)
                    print("O valor informado está na agenda.")
                    email_novo = capturar_dados("Digite o novo email: ")
                    email_novo = normalizar_email(email_novo)
                    contato.update({'Email': email_novo})
                    print("Email atualizado com sucesso!")
                else: #Se o email não estiver na agenda, informa ao usuário.
                    print("O valor informado nao está na agenda.")
                    return

            case 4:
                telefone = capturar_dados("Digite seu telefone: ")
                # Normaliza o telefone para comparação
                telefone_normalizado = normalizar_telefone(telefone)
                if telefone_normalizado == normalizar_telefone(contato['Telefone']):
                    # Verifica se o telefone já existe na agenda
                    print("O valor informado está na agenda.")
                    telefone_novo = capturar_dados("Digite o novo telefone: ")
                    #Normaliza o novo telefone inserido para manter a consistência
                    if not re.match(r'^\d{8,15}$', telefone_novo):
                        print("Telefone inválido. Deve conter apenas números e ter entre 8 a 15 dígitos.")
                        return
                    telefone_novo_normalizado = normalizar_telefone(telefone_novo)
                    contato.update({'Telefone': telefone_novo_normalizado})
                    print("Telefone atualizado com sucesso!")
                else: #Se o telefone não estiver na agenda, informa ao usuário.
                    print("O valor informado nao está na agenda.")
                    return


def menu_agenda():
    print("--:) Menu da Agenda (:--")
    while True:
        print("1 - Adicionar um contato.")
        print("2 - Visualizar agenda.")
        print("3 - Buscar contato.")
        print("4 - Favoritar um contato.")
        print("5 - Listar Favoritos")
        print("6 - Editar contato.")
        print("7 - Excluir contato.")
        print("0 - Sair.")
        try:
            opcao = int(input("Digite a opção desejada: "))
            match opcao:
                case 1:
                    adicionar_contato()
                case 2:
                    exibir_contato(contatos)
                case 3:
                    busca_contato()
                    
                #case 4:
                
                #case 5:
                    
                case 6:
                    editar_contato()
                #case 6:
                    
                case 10:
                    print("Saindo da agenda.")
                    raise SystemExit("Programa finalizado.")
                case _:
                    print("Opção inválida.")
        except ValueError:
            print("O valor inserido é inválido.")
        except KeyboardInterrupt:
            print("Programa interrompido.")
            raise SystemExit("Finalizando.")


menu_agenda()

#Todo: Verificar o porque está pedindo duas vezes email e telefone. // Done
#Estava pedindo duas vezes os parametros de usuário em duas funçoes diferentes.

#Todo: Adaptar funçao editar() para atender aos novos parametros