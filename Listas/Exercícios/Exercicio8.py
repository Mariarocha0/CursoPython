def mostrar_menu():
    print("\nOpções:")
    print("1. Adicionar item ao carrinho")
    print("2. Remover item do carrinho")
    print("3. Ver total da compra")
    print("4. Sair")

def adicionar_item(carrinho):
    item = input("Digite o nome do item: ")
    preco = float(input("Digite o preço do item: "))
    carrinho.append((item, preco))
    print(f'Item "{item}" adicionado ao carrinho por R$ {preco:.2f}.')

def remover_item(carrinho):
    for i, (nome, preco) in enumerate(carrinho):
        if nome == item:
            del carrinho[i]
            print(f'Item "{item}" removido do carrinho.')
            return
    print(f'Item "{item}" não encontrado no carrinho.')
def ver_total(carrinho):
    total = sum(preco for _, preco in carrinho)
    print(f'Total da compra: R$ {total:.2f}')

def main():
    carrinho = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_item(carrinho)
        elif escolha == '2':
            remover_item(carrinho)
        elif escolha == '3':
            ver_total(carrinho)
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
