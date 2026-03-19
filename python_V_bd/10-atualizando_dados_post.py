from conexao_postgres import conn

cursor_obj = conn.cursor()

sql = """
      UPDATE games
      SET name = %s
      WHERE id = %s
      """

cursor_obj.execute(sql, ("Metroid Games", 6))
conn.commit()
print("Dados atualizados com sucesso!")
conn.close()
