from Veiculo import Veiculo

class Gerenciador:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def remover_veiculo(self, id):
        for veiculo in self.veiculos:
            if veiculo.id == id:
                self.veiculos.remove(veiculo)
                print(f"Veículo com ID {id} removido com sucesso.")
                return
        print(f"Erro: Veículo com ID {id} não encontrado.")

    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo cadastrado.")
        for veiculo in self.veiculos:
            veiculo.exibir_detalhes()

    def buscar_veiculo(self, id):
        for veiculo in self.veiculos:
            if veiculo.id == id:
                veiculo.exibir_detalhes()
                return
        print(f"Erro: Veículo com ID {id} não encontrado.")
        
    def atualizar_quilometragem(self, id, nova_km):
        if id in self.veiculos:
            self.veiculos[id].atualizar_qulometragem(nova_km)
        else:
            print(f"Erro: Veículo com ID {id} não encontrado.")
  
           
gerenciador = Gerenciador()          

def exibir_menu():
    print("\n=== Menu de Opções ===")
    print("1. Adicionar veículo")
    print("2. Remover veículo pelo ID")
    print("3. Listar todos os veículos")
    print("4. Buscar veículo pelo ID")
    print("5. Atualizar quilometragem")
    print("6. Sair")
    print("======================")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print("\n--- Adicionar Veículo ---")
            id = int(input("ID do veículo: "))
            modelo = input("Modelo do veículo: ")
            tipo = input("Tipo do veículo (Carro, Moto, Caminhão, etc.): ")
            ano = int(input("Ano de fabricação: "))
            quilometragem = int(input("Quilometragem atual: "))
            veiculo = Veiculo(id, modelo, tipo, ano, quilometragem)
            gerenciador.adicionar_veiculo(veiculo)
        
        elif escolha == "2":
            print("\n--- Remover Veículo ---")
            id = int(input("ID do veículo a ser removido: "))
            gerenciador.remover_veiculo(id)
        
        elif escolha == "3":
            print("\n--- Lista de Veículos Cadastrados ---")
            gerenciador.listar_veiculos()
        
        elif escolha == "4":
            print("\n--- Buscar Veículo pelo ID ---")
            id = int(input("ID do veículo a ser buscado: "))
            gerenciador.buscar_veiculo(id)
        
        elif escolha == "5":
            print("\n--- Atualizar Quilometragem ---")
            id = int(input("ID do veículo: "))
            nova_km = int(input("Nova quilometragem: "))
            gerenciador.atualizar_quilometragem(id, nova_km)
        
        elif escolha == "6":
            print("\nSaindo do sistema. Até logo!")
            break
        
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida.")

# Executa o programa
if __name__ == "__main__":
    main()
