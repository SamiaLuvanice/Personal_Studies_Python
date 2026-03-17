import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor para executar comandos SQL
cursor = connection.cursor()

# 3 - Inserindo dados na tabela
cursor.execute("""
               INSERT INTO movies (name, year, score)
               VALUES ('The Secret Agent', 2025, 9.5)
                """)

cursor.execute("""
               INSERT INTO movies (name, year, score)
               VALUES ('I am Still Here', 2025, 10)
                """)

# 4 - Salvando as alterações
connection.commit()
print("Dados inseridos com sucesso!")

# 5 - Fechando a conexão
connection.close()
