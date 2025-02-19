# Definindo as tuplas de significados
significados = (
    ("cavalo", "liberdade e força"),
    ("mar", "mudanças emocionais"),
    ("relógio", "ansiedade com o tempo")
)

# Solicitando que o usuário insira um símbolo
simbolo = input("Insira um símbolo que você sonhou (cavalo, mar, relógio): ").lower()

# Inicializando a variável para armazenar o significado
significado_encontrado = None

# Usando um loop for para encontrar o significado do símbolo
for item in significados:
    if item[0] == simbolo:
        significado_encontrado = item[1]
        break

# Exibindo o significado ou uma mensagem padrão se o símbolo não for encontrado
if significado_encontrado:
    print(f"O significado de '{simbolo}' é: {significado_encontrado}")
else:
    print("Símbolo não reconhecido")

