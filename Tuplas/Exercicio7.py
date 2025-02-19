import random

# Definindo uma tupla com palavras inspiradoras
palavras_inspiradoras = (
    "Coragem", 
    "Criatividade", 
    "Persistência", 
    "Determinação", 
    "Empatia", 
    "Resiliência", 
    "Inovação"
)

# Pedindo para o usuário inserir seu nome
nome = input("Por favor, insira seu nome: ")

# Selecionando uma palavra inspiradora aleatoriamente
lema_aleatorio = random.choice(palavras_inspiradoras)

# Exibindo o lema para o usuário
print(f"{nome.capitalize()}, seu lema de vida é: {lema_aleatorio} leva à grandes realizações!")
