def determinar_nivel_mago(experiencia):
    if experiencia < 1000:
        return "Aprendiz"
    elif 1000 <= experiencia <= 5000:
        return "Mago Intermediário"
    elif 5001 <= experiencia <= 10000:
        return "Mago Avançado"
    else:
        return "Mestre Supremo da Magia"

# Exemplo de uso
experiencia = 7500
nivel = determinar_nivel_mago(experiencia)
print(f"O mago com {experiencia} pontos de experiência é um {nivel}.")