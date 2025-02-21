def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Solicita ao usuário um número N
N = int(input("Digite um número N: "))

# Gera todos os números primos até N
primos = [num for num in range(2, N + 1) if eh_primo(num)]

# Exibe os números primos
print("Números primos até", N, "são:", primos)
