import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor para executar comandos SQL
cursor = connection.cursor()

# 3 - Criando a tabela
cursor.execute("""
               CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    year INTEGER,
                    score REAL NOT NULL
                )
                """)

# 4 - Fechando a conexão
print("Tabela criada com sucesso!")
connection.close()
