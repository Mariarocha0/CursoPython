import random

# Definindo as previsões engraçadas
previsões_engraçadas = (
    "Em breve você encontrará um pato misterioso que mudará sua vida.",
    "Uma nuvem em forma de sorvete aparecerá no seu caminho.",
    "Você vai tropeçar em uma oportunidade incrível (literalmente).",
    "Um dia, seu cabelo terá um ótimo dia e todos notarão.",
    "Alguém vai te confundir com uma celebridade famosa em breve."
)

# Pedindo para o usuário digitar um número de 1 a 5
numero_escolhido = int(input("Digite um número de 1 a 5 para saber sua previsão engraçada: "))

# Verificando se o número está dentro do intervalo válido
if 1 <= numero_escolhido <= 5:
    # Exibindo a previsão correspondente
    previsao = previsões_engraçadas[numero_escolhido - 1]
    print(f"Sua previsão engraçada é: {previsao}")
else:
    print("Por favor, digite um número válido entre 1 e 5.")
