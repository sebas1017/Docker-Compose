from flask import Flask
import psycopg2
from psycopg2 import Error
app =  Flask(__name__)

@app.route('/')
def fruits():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="unicorn_user",
                                    password="magical_password",
                                    host="localhost",
                                    port="5432",
                                    database="rainbow_database")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT * FROM fruits;")
        # Fetch result
        record = cursor.fetchall()
        information = {"fruits":[]}
        for fruit in record:
            information["fruits"].append(fruit[1])
        return information
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
