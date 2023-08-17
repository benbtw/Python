import mysql.connector
from mysql.connector import Error
import pandas as pd

pw = ""

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
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

q1 = """
SELECT * FROM account_info;
"""

create_account_table = """
CREATE TABLE account_info (
  user_name varchar(255),
  pass_word varchar(255)
  );
 """

connection = create_db_connection("localhost", "root", pw, "accounts")
#execute_query(connection, create_account_table)

pop_acc = """
INSERT INTO account_info VALUES
("admin", "password");
"""

user_name = "admin"
passwrd = "password"

update = f"UPDATE account_info SET pass_word = '{passwrd}' WHERE user_name = '{user_name}';"

#delete_course = "DELETE FROM course WHERE course_id = 20;" this line is how delete things

execute_query(connection, update)

#execute_query(connection, pop_acc)
results = read_query(connection, q1)

""" below creates the database 
def create_databse(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database create successfully")
    except Error as err:
        print(f"Error: {err}")

create_database_query = "CREATE DATABASE accounts"
create_databse(connection, create_database_query)

connects to database server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
"""