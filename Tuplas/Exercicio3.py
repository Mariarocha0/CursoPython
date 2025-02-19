instrumentos = ("guitarra", "rock"), ("violino", "música clássica"), ("sanfona", "forró")

# Definindo as tuplas de instrumentos e seus gêneros musicais
instrumentos = (
    ("guitarra", "rock"),
    ("violino", "música clássica"),
    ("sanfona", "forró")
)

# Solicitando que o usuário insira um instrumento
instrumento_escolhido = input("Insira um instrumento (guitarra, violino, sanfona): ").lower()

# Usando match-case para determinar o gênero musical
match instrumento_escolhido:
    case "guitarra":
        print("O gênero musical é:", instrumentos[0][1])
    case "violino":
        print("O gênero musical é:", instrumentos[1][1])
    case "sanfona":
        print("O gênero musical é:", instrumentos[2][1])
    case _:
        print("Instrumento não reconhecido")

