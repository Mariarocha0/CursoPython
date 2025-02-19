# Criando a tupla
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Tentativa de alterar o valor do primeiro elemento
try:
    numeros[0] = 100
except TypeError as e:
    print("Erro:", e)

# Exibindo o primeiro e o último número
primeiro_numero = numeros[0]
ultimo_numero = numeros[-1]

print("Primeiro número:", primeiro_numero)
print("Último número:", ultimo_numero)
