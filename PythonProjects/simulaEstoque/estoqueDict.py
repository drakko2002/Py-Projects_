#Todo: Crie um dicionário para armazenar produtos e suas quantidades.
#Todo: Permita que o usuário:
#Todo:  Adicione novos produtos.
#Todo:  Atualize a quantidade de um produto.
#Todo:  Remova produtos do estoque.
#Todo:  Exiba o estoque atualizado após cada operação.
'''    produto = str(input("Digite nome do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    try:
        estoque[produto] = quantidade
        print(estoque)
        return estoque

    except ValueError:
        print("Erro de valor.")
estoque_dict(est)''' #Bom protótipo.
def estoque_dict(estoque:dict=(str,int)) -> dict:

    while True:
        try:
            #Validação da entrada do produto do usuário.
            print("-> Digite 'sair' para voltar ao menu <-")
            produto = str(input("Digite nome do produto: ")).strip()
            #print("\n Ou digite 'sair' para voltar ao menu.")
            if not produto:
                raise ValueError("Nome do produto não pode ser vazio.")
            if produto.lower() == 'sair':
                break
            #Se o usuário digitar sair ao invés de uma entrada esperada, o programa
            #tornará sua execução para o menu!


            #Fim valida entrada produto.

            #Validação da entrada da quantidade do usuário.
            quantidade = int(input("Digite a quantidade: "))
            if quantidade < 0:
                #Ao invés de usar not quantidade, que invalida valores como 0
                #por se tratar de uma expressão booleana, invalidamos apenas
                #valores que sejam menores que zero.

                raise ValueError("Quantidade não pode ser nula.")
            #Fim valida entrada quantidade.
            if produto in estoque:
                estoque[produto] += quantidade
            else:
                estoque[produto] = quantidade
            #Atualiza o estoque com o produto e sua quantidade.

            print(f"Estoque atualizado: {estoque}")

        except ValueError as e:
            print(f"Erro: {e}")
            continue
        except KeyError:
            print("Houve um erro.")
            continue
        except KeyboardInterrupt:
            raise SystemExit("Programa finalizado pelo usuário.")
        except TypeError:
            print("Erro de tipagem de valor.")
        #finally:
        #    break
    return estoque


def atualiza_quantidade(estoque: dict) -> None:
    produto = input("Digite o nome do produto a atualizar: ").strip()
    if produto not in estoque:
        print(f"Produto '{produto}' não encontrado no estoque.")
        return #Lembrnado que o return finaliza a execução do bloco.


    try:
        nova_quantidade = int(input("Digite a nova quantidade: "))
        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        estoque[produto] = nova_quantidade
        print(f"Estoque atualizado: {estoque}")
    except ValueError as e:
        print(f"Erro: {e}")


def remove_produto(estoque:dict) -> None:
    print("Selecionou excluir produto...")
    produto = str(input("Digite o nome do produto: ")).strip()


    if produto not in estoque:
        print(f"Chave {produto} não encontrada no {estoque}")
        return


    estoque.pop(produto)
    print(f"Chave {produto} removida do estoque.")
    print(f"Estoque atualizado: {estoque}")


def main():
    estoque = {}
    while True:
        try:
            print("-->Bem vindo ao Menu de Dicionários de Estoque <--")
            print("1 - Adicionar produto")
            print("2 - Atualizar quantidade")
            print("3 - Remover produto")
            print("4 - Sair")
            opcao = int(input("Digite opção desejada: "))
            if opcao == 1:
                estoque_dict(estoque)

            elif opcao == 2:
                atualiza_quantidade(estoque)

            elif opcao == 3:
                remove_produto(estoque)

            elif opcao == 4:
                raise SystemExit("Saindo do programa...")

            else:
                print("Opção inserida é inválida. Tente novamente.")



        except KeyboardInterrupt:
            raise SystemExit("Saindo do programa...")


if __name__ == "__main__":
    main()