import mysql.connector
from mysql.connector import Error
import pandas as pd
from flask import Flask, request, render_template, session, redirect

"""
This is the backend of my API it just send one SQL request to the database and respond the data to the user

"""

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query, params=None, fetch=False):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if fetch:
            result = cursor.fetchall()
            return result
        else:
            connection.commit()
            print("Query successful")
    except Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


app = Flask(__name__)

@app.route('/<choice>', methods=['GET'])
def index(choice):
    query = "SELECT * FROM moviesinfos WHERE name = %s"
    params = (choice,)

    print("query = ", query)
    connection = create_db_connection('127.0.0.1', 'MovieAPIReader', '' ,'movies')

    result = execute_query(connection, query, params=params, fetch=True)


    return result

if __name__ == '__main__':
    app.run("127.0.0.1",port=3434)