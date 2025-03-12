class Veiculo:
    def __init__(self, id, modelo, tipo, ano, quilometragem):
        self.id = id
        self.modelo = modelo
        self.tipo = tipo
        self.ano = ano
        self.quilometragem = quilometragem

    def exibir_detalhes(self):
        print(f"ID: {self.id}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo: {self.tipo}")
        print(f"Ano: {self.ano}")
        print(f"Quilometragem: {self.quilometragem} km")
    
    def atualizar_quilometragem(self, nova_km):
        if nova_km >= self.quilometragem:
            self.quilometragem = nova_km
        else:
            print("Erro: A nova quilometragem não pode ser menor que a atual.")
           