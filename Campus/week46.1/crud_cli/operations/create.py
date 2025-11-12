from crud_cli.db.connector import execute_query
from crud_cli.utils.validators import get_valid_input


def create_product():
    name = get_valid_input("Enter product name: ")
    if not name:
        return

    query = "INSERT INTO products (name) VALUES (%s)"
    success, cursor = execute_query(query, (name,))

    if success:
        print(f" product {name} created, successfully! with ID: {cursor.lastrowid}")