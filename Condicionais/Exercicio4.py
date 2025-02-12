#define a função 
#intere a palavra mágica
def portal_magico():
    palavra_magica = input("Digite a palavra mágica: ").strip().lower()
    
    if palavra_magica == "vermelho":
        print("O portal emite chamas ardentes!")
    elif palavra_magica == "azul":
        print("O portal brilha como o oceano profundo!")
    elif palavra_magica == "verde":
        print("O portal se entrelaça com a natureza!")
    else:
        print("A cor não é reconhecida... O portal permanece fechado.")

# Executa a função
portal_magico()
