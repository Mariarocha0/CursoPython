# Solicita ao usuário uma sequência de números separados por espaço
entrada = input("Digite uma sequência de números separados por espaço: ")

# Converte a entrada para uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Encontra o maior e o menor valor na lista
maior_valor = max(numeros)
menor_valor = min(numeros)

# Exibe o maior e o menor valor
print(f'O maior valor é: {maior_valor}')
print(f'O menor valor é: {menor_valor}')
