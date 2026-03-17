import sqlite3

# 1 - Criando o BD
connection = sqlite3.connect('title.db')

# 2 - Verifica se houve alteraçãoes na base de dados
print(connection.total_changes)
