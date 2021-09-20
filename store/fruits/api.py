from flask import Flask
from sqlalchemy import create_engine
app =  Flask(__name__)

@app.route('/')
def fruits():
    db_name = 'rainbow_database'
    db_user = 'unicorn_user'
    db_pass = 'magical_password'
    db_host = 'db'
    db_port = '5432'
    # Connecto to the database

    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    db = create_engine(db_string)
    querie = db.execute("SELECT * FROM fruits;")
    print(querie)
    print(type(querie))
    return {"message":"hola mundo"}
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
