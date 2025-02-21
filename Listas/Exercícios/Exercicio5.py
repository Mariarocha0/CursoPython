def classificar_nota(nota):
    if nota >= 9:
        return 'Ótimo'
    elif nota >= 7:
        return 'Bom'
    elif nota >= 5:
        return 'Regular'
    else:
        return 'Ruim'

# Solicita ao usuário uma lista de notas separadas por espaço
notas = list(map(int, input("Digite uma lista de notas separadas por espaço: ").split()))

# Classifica cada nota conforme a tabela fornecida
classificacoes = [classificar_nota(nota) for nota in notas]

# Exibe os resultados
for nota, classificacao in zip(notas, classificacoes):
    print(f'Nota: {nota} - Classificação: {classificacao}')
