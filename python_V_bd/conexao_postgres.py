import psycopg2

conn = psycopg2.connect(
      database="fliperama",
      user="postgres",
      password="1797",
      host="localhost",
      port="5433"
)
