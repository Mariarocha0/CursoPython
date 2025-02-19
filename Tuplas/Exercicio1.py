# Definindo as tuplas de cores
cores = (
    ("vermelho", "intenso e apaixonado"),
    ("azul", "calmo e equilibrado"),
    ("amarelo", "radiante e iluminado"),
    ("branco", "tranquilo e apaziguado")
)

# Funções para cada cor
def vermelho():
    return "Você escolheu vermelho! Descrição: " + cores[0][1]

def azul():
    return "Você escolheu azul! Descrição: " + cores[1][1]

def amarelo():
    return "Você escolheu amarelo! Descrição: " + cores[2][1]

def branco():
    return "Você escolheu branco! Descrição: " + cores[3][1]

def cor_nao_reconhecida():
    return "Cor não reconhecida"

# Dicionário de funções
funcoes_cores = {
    "vermelho": vermelho,
    "azul": azul,
    "amarelo": amarelo,
    "branco": branco
}

# Solicitando que o usuário escolha uma cor
cor_escolhida = input("Escolha uma cor: ").lower()

# Chamando a função correspondente ou a função padrão
resultado = funcoes_cores.get(cor_escolhida, cor_nao_reconhecida)()
print(resultado)
