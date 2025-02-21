# Solicita ao usuário uma sequência de números separados por espaço
entrada = input("Digite uma sequência de números separados por espaço: ")

# Converte a entrada para uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Filtra os números pares
pares = [numero for numero in numeros if numero % 2 == 0]

# Exibe os números pares
print("Números pares:", pares)
