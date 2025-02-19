# Listas de nomes antigos e adjetivos poderosos
nomes_antigos = ("Fafnir", "Smaug", "Balerion", "Drago")
adjetivos_poderosos = ("O terrível", "O devastador", "O guardião das chamas")

# Solicitando que o usuário escolha os números
primeiro_nome = int(input("Escolha um número de 1 a 4 para escolher o primeiro nome do seu dragão: ")) - 1
segundo_nome = int(input("Escolha um número de 1 a 3 para escolher o segundo nome do seu dragão: ")) - 1

# Obtendo o nome e o adjetivo correspondentes
nome_dragao = nomes_antigos[primeiro_nome]
adjetivo_dragao = adjetivos_poderosos[segundo_nome]

# Exibindo o nome completo do dragão
print(f"Seu dragão se chama {nome_dragao} {adjetivo_dragao}!")
