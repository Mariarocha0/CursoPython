# Listas de nomes antigos e adjetivos poderosos
nomes_antigos = ("Capitão", "Doutor", "Mestre", "Senhor")
adjetivos_poderosos = ("Relâmpago", "Sombrio", "Invencível", "Voador")

# Solicitando que o usuário escolha os números
primeiro_nome = int(input("Escolha um número de 1 a 4 para escolher o primeiro nome do seu herói: ")) - 1
segundo_nome = int(input("Escolha um número de 1 a 4 para escolher o segundo nome do seu herói: ")) - 1

# Obtendo o nome e o adjetivo correspondentes
nome_herói = nomes_antigos[primeiro_nome]
adjetivo_herói = adjetivos_poderosos[segundo_nome]

# Exibindo o nome completo do herói
print(f"Seu herói se chama {nome_herói} {adjetivo_herói}!")
