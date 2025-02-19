# Definindo as tuplas de ingredientes mágicos e seus efeitos
ingredientes_magicos = (
    ("Asas de fada", "Permite voar por um curto período"),
    ("Lágrima de dragão", "Concede força sobre-humana"),
    ("Pó de estrela", "Dá o poder da invisibilidade")
)

# Função para obter o efeito de um ingrediente
def obter_efeito(ingrediente):
    for item in ingredientes_magicos:
        if item[0].lower() == ingrediente.lower():
            return item[1]
    return "Ingrediente não encontrado"

# Pedindo para o usuário escolher dois ingredientes
print("Escolha dois ingredientes mágicos entre: Asas de fada, Lágrima de dragão, Pó de estrela")
ingrediente1 = input("Digite o primeiro ingrediente: ")
ingrediente2 = input("Digite o segundo ingrediente: ")

# Obtendo os efeitos dos ingredientes escolhidos
efeito1 = obter_efeito(ingrediente1)
efeito2 = obter_efeito(ingrediente2)

# Exibindo os efeitos combinados
if efeito1 != "Ingrediente não encontrado" and efeito2 != "Ingrediente não encontrado":
    print(f"Você escolheu: {ingrediente1} e {ingrediente2}.")
    print(f"Efeitos combinados: {efeito1} e {efeito2}.")
else:
    print("Um ou ambos os ingredientes não foram encontrados.")
