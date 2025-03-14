import gerenciamento

def menu():
    while True:
        print("\nMenu de Gerenciamento de Filmes:")
        print("1. Adicionar Filme")
        print("2. Remover Filme")
        print("3. Buscar Filme")
        print("4. Editar Filme")
        print("5. Listar Filmes")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "1":
            titulo = input("Digite o título do filme: ")
            genero = input("Digite o gênero do filme: ")
            ano_lancamento = int(input("Digite o ano de lançamento do filme: "))
            avaliacao = float(input("Digite a avaliação do filme (0 a 10): "))
            print(gerenciamento.adicionar_filme(titulo, genero, ano_lancamento, avaliacao))

        elif opcao == "2":
            titulo = input("Digite o título do filme que deseja remover: ")
            print(gerenciamento.remover_filme(titulo))

        elif opcao == "3":
            titulo = input("Digite o título do filme que deseja buscar: ")
            print(gerenciamento.buscar_filme(titulo))

        elif opcao == "4":
            titulo = input("Digite o título do filme que deseja editar: ")
            novo_titulo = input("Digite o novo título do filme (ou pressione Enter para manter o atual): ")
            novo_genero = input("Digite o novo gênero do filme (ou pressione Enter para manter o atual): ")
            novo_ano_lancamento = input("Digite o novo ano de lançamento do filme (ou pressione Enter para manter o atual): ")
            nova_avaliacao = input("Digite a nova avaliação do filme (ou pressione Enter para manter o atual): ")

            # Conversão condicional
            novo_ano_lancamento = int(novo_ano_lancamento) if novo_ano_lancamento else None
            nova_avaliacao = float(nova_avaliacao) if nova_avaliacao else None

            print(gerenciamento.editar_filme(titulo, novo_titulo, novo_genero, novo_ano_lancamento, nova_avaliacao))

        elif opcao == "5":
            print(gerenciamento.listar_filmes())

        elif opcao == "6":
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
