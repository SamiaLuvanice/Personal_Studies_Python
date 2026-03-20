import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect('./python_V_bd/title.db')

# 2 - Criando um cursor para executar comandos SQL
cursor = connection.cursor()

# 3 - Lendo dados da tabela
# cursor.execute("SELECT * FROM movies")
# data = cursor.fetchall()
# print(data)

# 4 - Iterando sobre os dados e imprimindo cada filme
# for row in cursor.execute("SELECT * FROM movies"):
#     print(f"{row}")

# 5 - Ordenando os dados pelo score
cursor.execute("SELECT * FROM movies ORDER BY score DESC")
data = cursor.fetchall()
print("Filmes ordenados por nota:")
for row in data:
    print(f"{row}")

# 6 - Fechando a conexão
connection.close()
