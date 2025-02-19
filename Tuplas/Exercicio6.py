# Definindo as tuplas de lugares e suas descrições
lugares = (
    ("Floresta sombria", "Um lugar cheio de criaturas mágicas e perigos escondidos"),
    ("Montanhas de fogo", "Território dos dragões ancestrais"),
    ("Cidade submersa", "Ruínas de uma civilização perdida sob as águas")
)

# Solicitando que o usuário insira um local
local_escolhido = input("Insira um local (Floresta sombria, Montanhas de fogo, Cidade submersa): ").lower()

# Inicializando a variável para armazenar a descrição
descricao_encontrada = None

# Usando um loop for para encontrar a descrição do local
for lugar in lugares:
    if lugar[0].lower() == local_escolhido:
        descricao_encontrada = lugar[1]
        break

# Exibindo a descrição ou uma mensagem padrão se o local não for encontrado
if descricao_encontrada:
    print(f"A descrição de '{local_escolhido.title()}' é: {descricao_encontrada}")
else:
    print("Local não reconhecido")
