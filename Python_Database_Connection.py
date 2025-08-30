import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="elderly_ai",
    user="postgres",
    password="yourpassword"
)
cur = conn.cursor()
