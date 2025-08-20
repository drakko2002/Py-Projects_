import re



contato: dict = {
    "Nome": "",
    "Sobrenome": "",
    "Email": "",
    "Telefone": "",
    "Favorito": False
}


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
    if not contatos:
        print("Nenhum contato cadastrado.")
    for contato in contatos:
        print(f"Nome: {contato['Nome']}")
        print(f"Sobrenome: {contato['Sobrenome']}")
        print(f"Email: {contato['Email']}")
        print(f"Telefone: {contato['Telefone']}")
        print(f"Favorito: {'Sim' if contato['Favorito'] else 'Não'}")
        print("-" * 20)


def adicionar_contato(nome: str = "", sobrenome: str = "", email: str = "", telefone: str = "", favorito: bool = False):
    """Adiciona um contato à agenda."""
    global contato
    print("Insira as informações do contato: \n")
    try: #Bloco de validaçao
        if email: #Se tiver sido inserido um email, tenta normalizar.
            email_valido = None
            
            while not email_valido:
                email = capturar_dados("Insira um e-mail válido: ")
                try:
                    email_normalizado = normalizar_email(email)
                    email_valido = email_normalizado
                    if email_valido == True:
                        return
                    
                except Exception as e:
                    print(f"Erro inesperado: {e}")
                    continue
        if telefone: #Se tiver sido inserido um telefone.
            telefone_valido = None
            while not telefone_valido:
                telefone = capturar_dados("Digite um telefone válido: ")
                try:
                    telefone_normalizado = normalizar_telefone(telefone)
                    telefone_valido = telefone_normalizado
                    if telefone_normalizado == True:
                        return
                except Exception as f:
                    print(f"Telefone inserido é inválido: {f}")
                    continue
            
        contato.update({
            "Nome": nome,
            "Sobrenome": sobrenome,
            "Email": email_normalizado,
            "Telefone": telefone_normalizado,
            "Favorito": False
        })
        print("Contato adicionado com sucesso!")
        exibir_contato([contato])
    except KeyboardInterrupt as e:
        raise SystemExit("Usuário finalizou o programa.") from e


def normalizar_telefone(telefone: str) -> str:
    """Normaliza o número de telefone removendo caracteres não numéricos."""
    return re.sub(r'\D', '', telefone)


def normalizar_email(email: str) -> str:
    """Normaliza o email convertendo para minúsculas."""
    email = email.lower().strip()
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise ValueError("Email inválido. Deve conter '@' e um domínio.")
    return email


def editar_contato(contato: dict):
    print(f"Prévia dos dados: {contato}")
    nome = contato.get("Nome", "")
    sobrenome = contato.get("Sobrenome", "")
    email = contato.get("Email", "")
    telefone = contato.get("Telefone", "")
    print("Selecione qual dado deseja editar!")
    print("1 - Nome; ")
    print("2 - Sobrenome; ")
    print("3 - Email; ")
    print("4 - Telefone")
    editar = int(input("Digite o parametro desejado para editar: "))
    if editar not in [1, 2, 3, 4]:
        print("Opção inválida. Tente novamente.")
        return
    match editar:
        case 1:
            nome = capturar_dados("Digite seu nome: ")
            # Verifica se o nome já existe na agenda
            # Se existir, atualiza o nome, caso contrário, informa que não está na agenda
            if nome in {contato['Nome']}:
                print("O valor informado está na agenda!")
                nome_novo = capturar_dados("Digite o novo nome: ")
                contato.update({'Nome': nome_novo})
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
                if not re.match(r'^\d{10,15}$', telefone_novo):
                    print("Telefone inválido. Deve conter apenas números e ter entre 10 a 15 dígitos.")
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
        print("4 - Editar contato.")
        print("5 - Excluir contato.")
        print("6 - Sair.")
        try:
            opcao = int(input("Digite a opção desejada: "))
            match opcao:
                case 1:
                    nome = capturar_dados("Digite o nome: ")
                    sobrenome = capturar_dados("Digite o sobrenome: ")
                    email = capturar_dados("Digite o email: ")
                    telefone = capturar_dados("Digite o telefone: ")
                    adicionar_contato(nome, sobrenome, email, telefone)
                case 2:
                    exibir_contato(contatos=[contato])
                case 6:
                    print("Saindo da agenda.")
                    raise SystemExit("Programa finalizado.")
                case 4:
                    editar_contato(contato)
                case _:
                    print("Opção inválida.")
        except ValueError:
            print("O valor inserido é inválido.")
        except KeyboardInterrupt:
            print("Programa interrompido.")
            raise SystemExit("Finalizando.")


menu_agenda()