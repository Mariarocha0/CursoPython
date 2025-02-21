def mostrar_menu():
    print("\nOpções")
    print("1. Adicionar tarefas")
    print("2. Remover tarefas")
    print("3. Vizualizar tarefas")
    print("4. Sair")
    
def adicionar_tarefas(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada.')

def remover_tarefa(tarefas):
    tarefa = input("Digite a tarefa a ser removida: ")
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print(f'Tarefa "{tarefa}" removida.')
    else:
        print(f'Tarefa "{tarefa}" não encontrada.')
        
def visualizar_tarefas(tarefas):
    if tarefas:
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")
        
def main():
    tarefas = []
    []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_tarefas(tarefas)
        elif escolha == '2':
            remover_tarefa(tarefas)
        elif escolha == '3':
            visualizar_tarefas(tarefas)
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break
        else: 
            print("opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()