class Filmes:
    def __init__(self, titulo, genero, ano_lancamento, avaliacao):
        # Atributos privados
        self.__titulo = titulo
        self.__genero = genero
        self.__ano_lancamento = ano_lancamento
        self.__avaliacao = avaliacao

    # Getters e setters para acessar e modificar os atributos
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_ano_lancamento(self):
        return self.__ano_lancamento

    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def get_avaliacao(self):
        return self.__avaliacao

    def set_avaliacao(self, avaliacao):
        if 0 <= avaliacao <= 10:
            self.__avaliacao = avaliacao
        else:
            raise ValueError("A avaliação deve estar entre 0 e 10.")

    # Método para exibir detalhes do filme
    def exibir_detalhes(self):
        return (f"Título: {self.__titulo}\n"
                f"Gênero: {self.__genero}\n"
                f"Ano de Lançamento: {self.__ano_lancamento}\n"
                f"Avaliação: {self.__avaliacao}/10")
