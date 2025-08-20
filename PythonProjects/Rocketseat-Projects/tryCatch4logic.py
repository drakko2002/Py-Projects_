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
        print("Entrada inválida. Por favor, tente novamente.")


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
#    contato = {
#        "Nome": nome.strip(),
#        "Sobrenome": sobrenome.strip(),
#        "Email": email.strip(),
#        "Telefone": telefone.strip(),
#        "Favorito": favorito
#            }

    try: 
        #nome = capturar_dados("Digite seu nome: ")
        #sobrenome = capturar_dados("Digite seu sobrenome: ")
        #email = capturar_dados("Digite seu e-mail: ")
        #telefone = capturar_dados("Digite seu telefone: ")
        print("Insira as informações do contato: \n")

        if not nome:
            nome = capturar_dados("Digite seu nome: ")
        if not sobrenome:
            sobrenome = capturar_dados("Digite seu sobrenome: ") 
        if not email:
            email = capturar_dados("Digite seu email: ")

        if not telefone:
            telefone = capturar_dados("Digite seu telefone: ")
        contato.update({
            "Nome": nome,
            "Sobrenome": sobrenome,
            "Email": email,
            "Telefone": telefone,
            "Favorito": False
        })
        print("Contato adicionado com sucesso!")
        exibir_contato([contato])
    except KeyboardInterrupt as e:
        raise SystemExit("Usuário finalizou o programa.") from e


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
            if not nome:
                nome = capturar_dados("Digite seu nome: ")
                if nome not in contato:
                    print("O valor informado nao está na agenda.")
            if nome in contato:
                contato.update(nome)
        case 2:
            if not sobrenome:
                sobrenome = capturar_dados("Digite seu sobrenome: ")
                if sobrenome not in contato:
                    print("O valor informado nao está na agenda.")
            if sobrenome in contato:
                contato.update(sobrenome)
        case 3:
            if not email:
                email = capturar_dados("Digite seu email: ")
                if email not in contato:
                    print("O valor informado nao está na agenda.")
            if email in contato:
                contato.update(email)
        case 4:
            if not telefone:
                telefone = capturar_dados("Digite seu telefone: ")
                if telefone not in contato:
                    print("O valor informado nao está na agenda.")
            if telefone in contato:
                contato.update(telefone)


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