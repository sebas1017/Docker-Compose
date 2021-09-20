from flask import Flask
from sqlalchemy import create_engine
app =  Flask(__name__)

@app.route('/')
def fruits():
    db_name = 'rainbow_database'
    db_user = 'unicorn_user'
    db_pass = 'magical_password'
    db_host = 'database'
    db_port = '5432'
    # Connecto to the database
    try:
        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        db = create_engine(db_string)
        querie_fruits = db.execute("SELECT * FROM fruits;").fetchall()
        information = {"fruits":[]}
        for fruit in querie_fruits:
            information["fruits"].append(fruit[1])
        return information
    except:
	return {"status":"error in database connection"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
