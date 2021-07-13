from flask import Flask, request, jsonify
import datetime
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
import psycopg2
import conexion1
import conexion2
import json,hashlib

# definir la instancia
app = Flask(__name__)

@app.route('/login',methods=["POST"])
def añadirUsuarios():
    inf=request.get_json()
    name=inf['username']#guardar variable del username
    pasw=inf['password']#guardar variable de la contraseña
    hashito=hashlib.sha256()
    hashito.update(pasw.encode('utf8'))#codificar la contraseña
    fecha=datetime.datetime.now()
    connect=conexion1.conectar1() #llamar la funcion de conexion con la base de datos test usuarios
    database=connect[0]
    cursor=connect[1]
    sql="INSERT INTO bingo_users VALUES (null,%s,%s,%s,null,null,null,%s,null,%s,%s,%s,%s,null,null,%s,%s,null,null,null,%s,%s,%s)"
    xd=(fecha,0,False,False,name,fecha,77,False,name,hashito.hexdigest(),fecha,7,"A",9,name)
    cursor.execute(sql,xd)#ejecutar query para la guardar el numero usuario
    database.commit()
    return "good"

@app.route('/users',methods=["GET"])
def base():
    connect=conexion2.conectar2() #llamar la funcion de conexion con la base de datos test juego
    database=connect[0]
    cursor=connect[1] 
    cursor.execute("SELECT row_to_json(bingo_param_board) from bingo_param_board LIMIT 20") #pasar registro SQL a formato JSON
    usuario=cursor.fetchall()
    #cursor.close()
    return jsonify(usuario)#mostrar en formato json los registros

@app.route('/figure',methods=['GET'])
def figure():
    connect=conexion2.conectar2() #llamar la funcion de conexion con la base de datos test juego
    database=connect[0]
    cursor=connect[1]  
    cursor.execute("SELECT row_to_json(bingo_param_figure) from bingo_param_figure")  #pasar registro SQL a formato JSON
    usuario=cursor.fetchall()
    #print(usuario)
    resultado = json.dumps(usuario,indent=4)#pasar a string
    resultado2=json.loads(resultado)#pasar a json
    #cursor.close()
    return jsonify(resultado2)

"""@app.route('/usuarios',methods=["GET"])
def basex():
    connect=conexion1.conectar1() #llamar la funcion de conexion con la base de datos test juego
    database=connect[0]
    cursor=connect[1] 
    cursor.execute("SELECT row_to_json(bingo_users) from bingo_users") #pasar registro SQL a formato JSON
    usuario=cursor.fetchall()
    #cursor.close()
    return jsonify(usuario)#mostrar en formato json los registros
"""
@app.route('/val/<int:board_id>',methods=['PUT'])
def edi(board_id):
    connect=conexion2.conectar2() #llamar la funcion de conexion con la base de datos test juego
    database=connect[0]
    cursor=connect[1]  
    cursor.execute("SELECT * from bingo_param_figure")  #pasar registro SQL a formato JSON
    tablas=cursor.fetchall()
    x=json.dumps(tablas)
    tablas2=json.loads(x)
    tablaEnc = [tabla for tabla in tablas if tabla['board_id']==board_id]#buscar la tabla para editar


    return jsonify({"tabla": tablaEnc[0]})
    


@app.route('/arr/<int:id>',methods=['POST'])
def array(id):
    cap=request.get_json()#obtener el array
    for caps in cap['array']:#recorrer el array
        if caps==id:#buscar el dato del la posicion que se agregó
            print(5)

    return cap


if __name__ == '__main__':
    #para que se actualice automaticamente
 app.run(debug=True)

