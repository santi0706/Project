import psycopg2
#definir la conexion de la base de datos test juego
def conectar2():
    conn = psycopg2.connect(
        host = "198.12.66.10",
        database = "test_juego",
        user = "testjava",
        password = "j4v42020*",
        port = "5432"
        )
    print("Conexion exitosa a la base de datos test_juego")
    cur=conn.cursor()
    return [conn,cur]