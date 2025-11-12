import mysql.connector
from mysql.connector import Error

def get_connection():
    """Create and return a MySQL connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gokstad",
            database="oliver_db",
            charset = 'utf8'
        )

        if connection.is_connected():
            print("Connected to MySQL")
            return connection

    except Error as e:
        print(f"MySQL connection error: {e}")
        return None
