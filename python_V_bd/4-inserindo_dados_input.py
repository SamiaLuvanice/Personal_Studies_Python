import sqlite3

# 1 - Conectando ao BD
connection = sqlite3.connect('./python_V_bd/title.db')

# 2 - Criando um cursor para executar comandos SQL
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
name = input("Digite o nome do filme: ")
year = int(input("Digite o ano de lançamento do filme: "))
score = float(input("Digite a nota do filme: "))

# 4 - Inserindo dados na tabela
cursor.execute("""
               INSERT INTO movies (name, year, score)
               VALUES (?, ?, ?)
                """, (name, year, score))

# 5 - Salvando as alterações
connection.commit()
print("Dados inseridos com sucesso!")

# 6 - Fechando a conexão
connection.close()
