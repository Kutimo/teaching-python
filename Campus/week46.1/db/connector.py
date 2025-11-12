import mysql.connector
from mysql.connector import Error


""" Create and return a Mysql connection"""
def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gokstad",
            database="oliver_db",
            charset="utf8"
        )
        if connection.is_connected():
            print("connected to db")
            return connection

    except Error as e:
        print(f"Error while connecting to db: {e}")
        return None
