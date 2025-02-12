def recomendar_cafe(temperatura):
    if temperatura < 15:
        return "Café expresso bem quente"
    elif 15 <= temperatura <= 25:
        return "Cappuccino"
    else:
        return "Café gelado"

# Exemplo de uso
temperatura = 20
recomendacao = recomendar_cafe(temperatura)
print(f"Com a temperatura de {temperatura}°C, o robô recomenda: {recomendacao}.")
