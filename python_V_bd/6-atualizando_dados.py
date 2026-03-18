import sqlite3

connection = sqlite3.connect('./python_V_bd/title.db')

cursor = connection.cursor()

# Solicitando dados do usuário
id = int(input('Digite o ID do filme que deseja atualizar: '))
name = input('Digite o novo nome do filme: ')

# Atualizando Dados
cursor.execute("""UPDATE movies SET name = ?
                  WHERE id = ?
                """, (name, id))

# Salvando as alterações
connection.commit()
print('Dados atualizados com sucesso!')

# Fechando a conexão
connection.close()
