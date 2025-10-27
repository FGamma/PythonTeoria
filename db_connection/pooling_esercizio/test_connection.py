import mysql.connector
from time import time

# Non è l'esecuzione della query che costa tanto ma la connessione --> pooling
N = 100

# Senza pooling
start_time = time()
for i in range(N):
    cnx = mysql.connector.connect(
        host="127.0.0.1", user="root", password="root", database="yelp"
    )

    cursor = cnx.cursor()
    query = """SELECT * FROM business"""
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    cnx.close()
end_time = time()
print(f"Elapsed time without pooling = {end_time-start_time}")

# Con Pooling
start_time = time()
cnx_pool = mysql.connector.pooling.MySQLConnectionPool(
    host="127.0.0.1",
    user="root",
    password="root",
    database="yelp",
    pool_size=3,
    pool_name="mypool",
)
for i in range(N):
    cnx = cnx_pool.get_connection()
    cursor = cnx.cursor()
    query = """SELECT * FROM business"""
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    cnx.close()
end_time = time()
print(f"Elapsed time with pooling = {end_time-start_time}")
