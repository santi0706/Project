import psycopg2
#definir la conexion a la base de datos test usuarios
def conectar1():
    conn = psycopg2.connect(
        host = "198.12.66.10",
        database = "test_usuarios",
        user = "testjava",
        password = "j4v42020*",
        port = "5432"
        )
    print("Conexion exitosa a la base de datos test_usuarios")
    cur=conn.cursor()
    return [conn,cur]