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

def execute_query(query, parameters=None, fetch=False, dictionary=False):
    """
    Generic function to execute any database query.
    Handles connection, execution, commit, and error handling.

    Args:
        query: SQL query string
        parameters: Query parameters (tuple or list)
        fetch: If True, returns fetched results
        dictionary: If True, returns results as dictionaries

    Returns:
        For fetch=True: query results or None
        For fetch=False: (success: bool, cursor or error_message)
    """
    connection = get_connection()
    if not connection:
        print("Cannot connect to database")
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
