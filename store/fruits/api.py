from flask import Flask
from sqlalchemy import create_engine
app =  Flask(__name__)

@app.route('/')
def fruits():
    db_name = 'rainbow_database'
    db_user = 'unicorn_user'
    db_pass = 'magical_password'
    db_host = 'database' # este es el servicio database declarado en el docker-compose
    db_port = '5433'
    # conexion a la base de datos POSTGRESQL
    try:
        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        db = create_engine(db_string)
        querie_fruits = db.execute("SELECT * FROM fruits;").fetchall()
        #aqui tomo los resultados de la tabla fruits y los transformo en la estructura json {"fruits":[]}
        information = {"fruits":[]}
        for fruit in querie_fruits:
            information["fruits"].append(fruit[1])
        #finalmente retorno la informacion de las frutas extraidas de la base de datos
        return information
    except:
	    return {"status":"error en conexion con la base de datos"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
