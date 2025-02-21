# Solicita ao usuário uma lista de números separados por espaço
entrada = input("Digite uma lista de números separados por espaço: ")

# Converte a entrada para uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Dicionário para contar a ocorrência de cada número
contagem = {}

# Contar as ocorrências de cada número
for numero in numeros:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

# Lista para armazenar números que aparecem mais de uma vez
numeros_repetidos = [numero for numero, ocorrencias in contagem.items() if ocorrencias > 1]

# Exibe os números que aparecem mais de uma vez
if numeros_repetidos:
    print("Números que aparecem mais de uma vez:", numeros_repetidos)
else:
    print("Nenhum número aparece mais de uma vez.")
