import psycopg2

conn = psycopg2.connect(
      database="fliperama",
      user="postgres",
      password="xxxx",
      host="localhost",
      port="5433"
)
