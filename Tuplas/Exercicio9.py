# Definindo as tuplas de traços de personalidade e suas descrições
tracos_personalidade = (
    ("Líder", "Rei ou Rainha de um império poderoso"),
    ("Estrategista", "Mestre das sombras que manipula tudo nos bastidores"),
    ("Aventureiro", "Explorador destemido que busca tesouros escondidos")
)

# Solicitando que o usuário escreva sua personalidade
personalidade_escolhida = input("Escreva sua personalidade (Líder, Estrategista, Aventureiro): ").capitalize()

# Inicializando a variável para armazenar a descrição
descricao_personalidade = None

# Usando um loop for para encontrar a descrição da personalidade
for traco in tracos_personalidade:
    if traco[0].lower() == personalidade_escolhida.lower():
        descricao_personalidade = traco[1]
        break

# Exibindo a descrição ou uma mensagem padrão se a personalidade não for encontrada
if descricao_personalidade:
    print(f"Sua personalidade é: {personalidade_escolhida}. {descricao_personalidade}")
else:
    print("Personalidade não reconhecida")
