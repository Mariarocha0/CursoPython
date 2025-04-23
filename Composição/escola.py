class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Professor: {self.nome}, Idade: {self.idade}"


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}"


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor_responsavel = None
        self.alunos_matriculados = []

    def definir_professor(self, professor):
        self.professor_responsavel = professor

    def matricular_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)

    def listar_alunos(self):
        return [str(aluno) for aluno in self.alunos_matriculados]

    def __str__(self):
        prof = self.professor_responsavel.nome if self.professor_responsavel else "Nenhum"
        return f"Curso: {self.nome}, Professor Responsável: {prof}"


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
        self.alunos = []
        self.cursos = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def listar_professores(self):
        return [str(prof) for prof in self.professores]

    def listar_alunos(self):
        return [str(aluno) for aluno in self.alunos]

    def listar_cursos(self):
        return [str(curso) for curso in self.cursos]


# --- PROGRAMA PRINCIPAL ---

escola = Escola("Escola Exemplo")

# Cadastro de professores
print("Cadastro de Professores:")
while True:
    nome = input("Nome do professor (ou 'sair' para parar): ")
    if nome.lower() == "sair":
        break
    idade = input("Idade do professor: ")
    professor = Professor(nome, int(idade))
    escola.adicionar_professor(professor)

# Cadastro de alunos
print("\nCadastro de Alunos:")
while True:
    nome = input("Nome do aluno (ou 'sair' para parar): ")
    if nome.lower() == "sair":
        break
    matricula = input("Matrícula do aluno: ")
    aluno = Aluno(nome, matricula)
    escola.adicionar_aluno(aluno)

# Criando curso e atribuindo o primeiro professor e os alunos
curso = Curso("Matemática")
if escola.professores:
    curso.definir_professor(escola.professores[0])
for aluno in escola.alunos:
    curso.matricular_aluno(aluno)
escola.adicionar_curso(curso)

# Exibindo 
print("\n--- Dados da Escola ---")
print("\nProfessores:")
print("\n".join(escola.listar_professores()))

print("\nAlunos:")
print("\n".join(escola.listar_alunos()))

print("\nCursos:")
print("\n".join(escola.listar_cursos()))

print("\nAlunos do curso de Matemática:")
print("\n".join(curso.listar_alunos()))
