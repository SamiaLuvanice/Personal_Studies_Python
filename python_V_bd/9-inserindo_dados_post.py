from conexao_postgres import conn

cursor_obj = conn.cursor()

games = [
  ('Super Mario Bros', 1985, 9.0),
  ('The Legend of Zelda', 1986, 9.5),
  ('Metroid', 1986, 8.5)
]

for game in games:
    cursor_obj.execute("""
                       INSERT INTO games (name, year, score)
                       VALUES (%s, %s, %s)
                       """, game)

conn.commit()
print("Dados inseridos com sucesso!")
cursor_obj.close()
conn.close()
