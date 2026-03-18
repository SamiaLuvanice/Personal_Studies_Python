import sqlite3

connection = sqlite3.connect('./python_V_bd/title.db')

cursor = connection.cursor()

# Solicitando dados do usuário
id = int(input('Digite o ID do filme que deseja remover: '))

# Removendo Dados
cursor.execute("""DELETE FROM movies
                  WHERE id = ?
                """, (id,))

# Salvando as alterações
connection.commit()
print('Dados removidos com sucesso!')

# Fechando a conexão
connection.close()
