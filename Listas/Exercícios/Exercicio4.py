# Solicita ao usuário uma lista de palavras separadas por espaço
palavras = input("Digite uma lista de palavras separadas por espaço: ").split()

# Solicita ao usuário uma letra
letra = input("Digite uma letra: ").lower()

# Filtra as palavras que começam com a letra fornecida
palavras_filtradas = [palavra for palavra in palavras if palavra.lower().startswith(letra)]

# Exibe as palavras filtradas
print("Palavras que começam com a letra '{}' são: {}".format(letra, palavras_filtradas))
