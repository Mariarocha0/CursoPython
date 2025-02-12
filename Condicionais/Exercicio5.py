def detectar_personagem(nome):
    primeira_letra = nome[0].upper()
    
    if primeira_letra in ["A", "E", "I", "O", "U"]:
        return "Herói"
    elif primeira_letra in ["Z", "Y", "X"]:
        return "Vilão"
    else:
        return "Classificação desconhecida. Preciso de mais dados."

# Exemplo de uso
nome_personagem = input("Digite o nome do personagem: ")
classificacao = detectar_personagem(nome_personagem)
print(f"O personagem {nome_personagem} é um: {classificacao}.")
