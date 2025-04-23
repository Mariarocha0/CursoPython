import json
import os

# ======== CLASSES BASE E DERIVADAS ========

class Veiculo:
    def __init__(self, id, marca, modelo, ano, placa):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": "Veiculo",
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "placa": self.placa
        }

class Carro(Veiculo):
    def __init__(self, id, marca, modelo, ano, placa, portas):
        super().__init__(id, marca, modelo, ano, placa)
        self.portas = portas

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "Carro"
        data["portas"] = self.portas
        return data

class Moto(Veiculo):
    def __init__(self, id, marca, modelo, ano, placa, cilindradas):
        super().__init__(id, marca, modelo, ano, placa)
        self.cilindradas = cilindradas

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "Moto"
        data["cilindradas"] = self.cilindradas
        return data

# ======== FUNÇÕES DE MANIPULAÇÃO DE ARQUIVOS ========

ARQUIVO = "veiculos.json"

def carregar_veiculos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_veiculos(veiculos):
    with open(ARQUIVO, "w") as f:
        json.dump(veiculos, f, indent=4)

# ======== MENU INTERATIVO ========

def cadastrar_veiculo():
    veiculos = carregar_veiculos()
    id = len(veiculos) + 1
    tipo = input("Tipo de veículo (carro/moto): ").strip().lower()

    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    placa = input("Placa: ")

    if tipo == "carro":
        portas = int(input("Quantidade de portas: "))
        carro = Carro(id, marca, modelo, ano, placa, portas)
        veiculos.append(carro.to_dict())
    elif tipo == "moto":
        cilindradas = input("Cilindradas: ")
        moto = Moto(id, marca, modelo, ano, placa, cilindradas)
        veiculos.append(moto.to_dict())
    else:
        print("Tipo inválido. Use 'carro' ou 'moto'.")
        return

    salvar_veiculos(veiculos)
    print("✅ Veículo cadastrado com sucesso!")

def listar_veiculos():
    veiculos = carregar_veiculos()
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return
    print("\n=== Lista de Veículos ===")
    for v in veiculos:
        print(f"ID: {v['id']} | Tipo: {v['tipo']} | {v['marca']} {v['modelo']} ({v['ano']}) - Placa: {v['placa']}")

def buscar_veiculo():
    veiculos = carregar_veiculos()
    id = input("Digite o ID do veículo: ")
    for v in veiculos:
        if str(v["id"]) == id:
            print("\n=== Veículo Encontrado ===")
            for chave, valor in v.items():
                print(f"{chave.capitalize()}: {valor}")
            return
    print("❌ Veículo não encontrado.")

def menu():
    while True:
        print("\n===== Sistema de Locadora de Veículos =====")
        print("1. Cadastrar Veículo")
        print("2. Listar Todos os Veículos")
        print("3. Buscar Veículo por ID")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_veiculo()
        elif opcao == "2":
            listar_veiculos()
        elif opcao == "3":
            buscar_veiculo()
        elif opcao == "4":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# ======== INICIAR O SISTEMA ========
menu()
