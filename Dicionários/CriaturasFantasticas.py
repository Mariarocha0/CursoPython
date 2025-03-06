criaturas = {
    101: {"nome": "Draco", "especie": "Dragão", "poder": "Sopro de fogo", "idade": 500},
    102: {"nome": "Luna", "especie": "Unicórnio", "poder": "Cura mágica", "idade": 150},
    103: {"nome": "Fawkes", "especie": "Fênix", "poder": "Ressurreição", "idade": 800}
}

# Função para exibir o menu
def exibir_menu():
    print("\nMenu do Sistema")
    print("1. Adicionar uma nova criatura")
    print("2. Remover uma criatura")
    print("3. Exibir todas as criaturas")
    print("4. Buscar uma criatura pelo ID")
    print("5. Editar os dados de uma criatura")
    print("6. Sair")


# Função para adicionar uma nova criatura
def adicionar_criatura():
    try:
        id = int(input("Digite o ID da criatura: "))
        if id in criaturas:
            print("Erro: ID já existe!")
            return
        nome = input("Digite o nome da criatura: ")
        especie = input("Digite a espécie da criatura: ")
        poder = input("Digite o poder especial da criatura: ")
        idade = int(input("Digite a idade da criatura: "))
        criaturas[id] ={"nome": nome, "especie": especie, "poder": poder, "idade": idade}
        print("Criatura adicionada com sucesso.")
    except ValueError:
        print("Erro: ID e idade devem ser números inteiros")
        

#Função para remover uma criatura pelo ID
def remover_criatura():
    try:
        id = int(input("Digite o ID da criatura que deseja remover: "))
        if id in criaturas:
            del criaturas[id]
            print("Criatura removida com sucesso.")
        else:
            print("Erro: ID não encontrado.")
    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
        
# Função para exibir todas as criaturas
def exibir_criaturas():
    if not criaturas:
        print("Nenhuma criatura cadastrada!")
    else:
#items = retorna uma lista de tuplas, onde cada tupla contém um ID e um valor.
        for id, detalhes in criaturas.items():
             print(f"ID: {id}, Nome: {detalhes['nome']}, Espécie: {detalhes['especie']}, Poder: {detalhes['poder']}, Idade: {detalhes['idade']}")
             
# Função para buscar uma criatura pelo ID
def buscar_criatura():
    try:
        id = int(input("Digite o ID da criatura que deseja buscar:"))
        if id in criaturas:
            detalhes = criaturas[id]
            print(f"ID: {id}, Nome: {detalhes['nome']}, Espécie: {detalhes['especie']}, Poder: {detalhes['poder']}, Idade: {detalhes['idade']}")
        else:
            print("Erro: ID não encontrado.")
    except ValueError:
        print("Erro: ID deve ser um número inteiro.")
        
# Funçãop para editar os dados doe uma criatura
def editar_criatura():
    try:
        id - int(input("Digite o ID da criatura que deseja editar: "))
        if id in criaturas:
            nome = input("Digite o novo nome da criatura (ou pressione Enter para manter o atual): ")
            if nome:
                criaturas[id]['nome'] = nome
            especie = input("Digite a nova espécie da criatura (ou pressione Enter para manter a atual): ")
            if especie:
                criaturas[id]['especie'] = especie
            poder = input("Digite o novo poder especial da criatura (ou pressione Enter para manter o atual): ")
            if poder:
                criaturas[id]['poder'] = poder
            idade = input("Digite a nova idade da criatura (ou pressione Enter para manter a atual): ")
            if idade:
                criaturas[id]['idade'] = int(idade)
            print("Criatura editada com sucesso.")
        else:
            print("Erro: ID não encontrado.")
    except ValueError:
        print("Erro: ID e idade devem ser números inteiros.")
    
# Função principal para o menu do sistema
def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                adicionar_criatura()
            elif opcao == 2:
                remover_criatura()
            elif opcao == 3:
                exibir_criaturas()
            elif opcao == 4:
                buscar_criatura()
            elif opcao == 5:
                editar_criatura()
            elif opcao == 6:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: A opção deve ser um número inteiro.")

# Iniciar o sistema
if __name__ == "__main__":
    main()
