import mysql.connector
from mysql.connector import Error
import pandas as pd

class SQL_CLASS:

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
    
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(f"Error: '{err}'")
        return cursor.fetchone()

    def read_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def check_data(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        check_var = cursor.fetchone()
        if check_var is None:
            print("not in database")
        return check_var