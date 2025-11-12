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


def execute_query(query, parameters=None, fetch=False, dictionary=False):
    # Generic function to execute any database query
    # Handles connections, execution (to run a sql query), commit (send the changes to the database) and error handling.

    connection = get_connection()
    if not connection:
        print("Cannot connect to db")
        return None if fetch else (False, "Connection failed")

    try:
        with connection.cursor(dictionary=dictionary) as cursor:
            cursor.execute(query, parameters or ())

            if fetch:
                results = cursor.fetchall()
                return results
            else:
                connection.commit()
                return True, cursor

    except Exception as e:
        print(f"Database error: {e}")
        if not fetch:
            connection.rollback()
        return None if fetch else (False, str(e))

    finally:
        connection.close()