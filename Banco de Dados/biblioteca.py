import sqlite3
from datetime import datetime

# Conexão com o banco SQLite
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Criação das tabelas
def criar_tabelas():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nacionalidade TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        id_autor INTEGER,
        ano_publicacao INTEGER,
        disponivel BOOLEAN DEFAULT 1,
        FOREIGN KEY (id_autor) REFERENCES autores(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        id_livro INTEGER NOT NULL,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
        FOREIGN KEY (id_livro) REFERENCES livros(id)
    )""")
    conn.commit()

# Menu principal
def menu():
    while True:
        print("\n📚 MENU BIBLIOTECA")
        print("1. Cadastrar autor")
        print("2. Cadastrar livro")
        print("3. Cadastrar usuário")
        print("4. Realizar empréstimo")
        print("5. Listar livros disponíveis")
        print("6. Listar empréstimos")
        print("7. Realizar devolução")
        print("8. Listar usuários")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_autor()
        elif opcao == "2":
            cadastrar_livro()
        elif opcao == "3":
            cadastrar_usuario()
        elif opcao == "4":
            realizar_emprestimo()
        elif opcao == "5":
            listar_livros()
        elif opcao == "6":
            listar_emprestimos()
        elif opcao == "7":
            realizar_devolucao()
        elif opcao == "8":
            listar_usuarios_completo()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

# Funções de cadastro
def cadastrar_autor():
    nome = input("Nome do autor: ")
    nacionalidade = input("Nacionalidade: ")
    cursor.execute("INSERT INTO autores (nome, nacionalidade) VALUES (?, ?)", (nome, nacionalidade))
    conn.commit()
    print("Autor cadastrado com sucesso!")

def cadastrar_livro():
    titulo = input("Título do livro: ")
    listar_autores()
    id_autor = input("ID do autor: ")
    ano = input("Ano de publicação: ")
    cursor.execute("INSERT INTO livros (titulo, id_autor, ano_publicacao) VALUES (?, ?, ?)", (titulo, id_autor, ano))
    conn.commit()
    print("Livro cadastrado com sucesso!")

def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cursor.execute("INSERT INTO usuarios (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))
    conn.commit()
    print("Usuário cadastrado com sucesso!")

# Empréstimos e devoluções
def realizar_emprestimo():
    listar_usuarios()
    id_usuario = input("ID do usuário: ")
    listar_livros()
    id_livro = input("ID do livro a ser emprestado: ")

    cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
    status = cursor.fetchone()
    if status and status[0] == 1:
        data = datetime.today().date()
        cursor.execute("INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo) VALUES (?, ?, ?)",
                       (id_usuario, id_livro, data))
        cursor.execute("UPDATE livros SET disponivel = 0 WHERE id = ?", (id_livro,))
        conn.commit()
        print("Empréstimo realizado com sucesso!")
    else:
        print("Livro indisponível.")

def realizar_devolucao():
    listar_emprestimos()
    id_livro = input("ID do livro a ser devolvido: ")
    data_hoje = datetime.today().date()
    cursor.execute("""
        UPDATE emprestimos 
        SET data_devolucao = ? 
        WHERE id_livro = ? AND data_devolucao IS NULL
    """, (data_hoje, id_livro))
    cursor.execute("UPDATE livros SET disponivel = 1 WHERE id = ?", (id_livro,))
    conn.commit()
    print("Livro devolvido com sucesso!")

# Listagens
def listar_autores():
    print("\n📖 Autores:")
    cursor.execute("SELECT id, nome FROM autores")
    for autor in cursor.fetchall():
        print(f"{autor[0]} - {autor[1]}")

def listar_usuarios():
    print("\n👤 Usuários:")
    cursor.execute("SELECT id, nome FROM usuarios")
    for usuario in cursor.fetchall():
        print(f"{usuario[0]} - {usuario[1]}")

def listar_usuarios_completo():
    print("\n👤 Lista de Usuários:")
    cursor.execute("SELECT id, nome, email, telefone FROM usuarios")
    for usuario in cursor.fetchall():
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]} | Telefone: {usuario[3]}")

def listar_livros():
    print("\n📘 Livros disponíveis:")
    cursor.execute("SELECT id, titulo FROM livros WHERE disponivel = 1")
    for livro in cursor.fetchall():
        print(f"{livro[0]} - {livro[1]}")

def listar_emprestimos():
    print("\n📄 Empréstimos:")
    cursor.execute("""
        SELECT u.nome, l.titulo, e.data_emprestimo, e.data_devolucao
        FROM emprestimos e
        JOIN usuarios u ON e.id_usuario = u.id
        JOIN livros l ON e.id_livro = l.id
    """)
    for emprestimo in cursor.fetchall():
        devolucao = emprestimo[3] if emprestimo[3] else "Pendente"
        print(f"Usuário: {emprestimo[0]} | Livro: {emprestimo[1]} | Empréstimo: {emprestimo[2]} | Devolução: {devolucao}")

# Execução principal
criar_tabelas()
menu()
conn.close()
