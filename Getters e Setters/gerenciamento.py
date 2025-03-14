from Filmes import Filmes

# Dicionário para armazenar os filmes cadastrados
filmes_cadastrados = {}

# Função para adicionar um novo filme
def adicionar_filme(titulo, genero, ano_lancamento, avaliacao):
    if titulo not in filmes_cadastrados:
        filme = Filmes(titulo, genero, ano_lancamento, avaliacao)
        filmes_cadastrados[titulo] = filme
        return f'Filme "{titulo}" adicionado com sucesso!'
    return f'Filme "{titulo}" já está cadastrado.'

# Função para remover um filme pelo título
def remover_filme(titulo):
    if titulo in filmes_cadastrados:
        del filmes_cadastrados[titulo]
        return f'Filme "{titulo}" removido com sucesso!'
    return f'Filme "{titulo}" não encontrado.'

# Função para buscar um filme pelo título
def buscar_filme(titulo):
    if titulo in filmes_cadastrados:
        return filmes_cadastrados[titulo].exibir_detalhes()
    return f'Filme "{titulo}" não encontrado.'

# Função para editar um filme
def editar_filme(titulo, novo_titulo=None, novo_genero=None, novo_ano_lancamento=None, nova_avaliacao=None):
    if titulo in filmes_cadastrados:
        filme = filmes_cadastrados[titulo]
        if novo_titulo:
            del filmes_cadastrados[titulo]
            filme.set_titulo(novo_titulo)
            filmes_cadastrados[novo_titulo] = filme
        if novo_genero:
            filme.set_genero(novo_genero)
        if novo_ano_lancamento:
            filme.set_ano_lancamento(novo_ano_lancamento)
        if nova_avaliacao is not None:
            filme.set_avaliacao(nova_avaliacao)
        return f'Filme "{titulo}" atualizado com sucesso!'
    return f'Filme "{titulo}" não encontrado.'

# Função para listar todos os filmes cadastrados
def listar_filmes():
    if filmes_cadastrados:
        detalhes = "Lista de filmes cadastrados:\n"
        for filme in filmes_cadastrados.values():
            detalhes += filme.exibir_detalhes() + "\n\n"
        return detalhes
    return "Nenhum filme cadastrado."
