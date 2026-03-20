from conexao_postgres import conn

cursor_obj = conn.cursor()

sql = """
      DELETE FROM games
      WHERE id = %s
      """

cursor_obj.execute(sql, (1,))
conn.commit()
print("Dados excluídos com sucesso!")
conn.close()
