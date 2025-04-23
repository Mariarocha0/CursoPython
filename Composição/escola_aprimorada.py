class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} (Idade: {self.idade})"


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"{self.nome} (Matrícula: {self.matricula})"


class Curso:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def matricular_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def gerar_relatorio(self):
        print(f"\nRelatório do Curso: {self.nome}")
        print(f"Professor: {self.professor.nome}")
        if not self.alunos:
            print("Nenhum aluno matriculado.")
            return
        for aluno in self.alunos:
            media = aluno.calcular_media()
            status = "Aprovado" if media >= 7.0 else "Reprovado"
            print(f"- {aluno.nome} | Média: {media:.2f} | {status}")

    def __str__(self):
        return f"{self.nome} (Prof: {self.professor.nome})"


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
        self.alunos = []
        self.cursos = []

    def encontrar_professor(self, nome):
        for prof in self.professores:
            if prof.nome == nome:
                return prof
        return None

    def encontrar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                return aluno
        return None

    def encontrar_curso(self, nome):
        for curso in self.cursos:
            if curso.nome == nome:
                return curso
        return None


# ======= MENU INTERATIVO =======
escola = Escola("Escola Interativa")

def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Adicionar um novo curso")
        print("2. Adicionar um professor")
        print("3. Adicionar um aluno")
        print("4. Matricular aluno em um curso")
        print("5. Adicionar nota a um aluno")
        print("6. Gerar relatório do curso")
        print("7. Listar todos os cursos")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_curso = input("Nome do curso: ")
            nome_prof = input("Nome do professor responsável: ")
            professor = escola.encontrar_professor(nome_prof)
            if not professor:
                print("Professor não encontrado. Adicione-o primeiro.")
                continue
            curso = Curso(nome_curso, professor)
            escola.cursos.append(curso)
            print("Curso adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Nome do professor: ")
            idade = int(input("Idade: "))
            escola.professores.append(Professor(nome, idade))
            print("Professor adicionado.")

        elif opcao == "3":
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula: ")
            escola.alunos.append(Aluno(nome, matricula))
            print("Aluno adicionado.")

        elif opcao == "4":
            nome_aluno = input("Nome do aluno: ")
            nome_curso = input("Curso para matrícula: ")
            aluno = escola.encontrar_aluno(nome_aluno)
            curso = escola.encontrar_curso(nome_curso)
            if aluno and curso:
                curso.matricular_aluno(aluno)
                print("Aluno matriculado com sucesso.")
            else:
                print("Aluno ou curso não encontrado.")

        elif opcao == "5":
            nome_aluno = input("Nome do aluno: ")
            aluno = escola.encontrar_aluno(nome_aluno)
            if aluno:
                nota = float(input("Nota a ser adicionada: "))
                aluno.adicionar_nota(nota)
                print("Nota adicionada.")
            else:
                print("Aluno não encontrado.")

        elif opcao == "6":
            nome_curso = input("Nome do curso: ")
            curso = escola.encontrar_curso(nome_curso)
            if curso:
                curso.gerar_relatorio()
            else:
                print("Curso não encontrado.")

        elif opcao == "7":
            print("\nCursos cadastrados:")
            for curso in escola.cursos:
                print(f"- {curso}")

        elif opcao == "8":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")


# Iniciar o sistema
menu()
