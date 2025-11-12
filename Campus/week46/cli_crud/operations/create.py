from Campus.week46.cli_crud.utils.valdidator import get_valid_input


def add_product():
    """Add a new product to the database"""
    name = get_valid_input("Enter product name: ")
    if not name:
        return

    query = "INSERT INTO products (name) VALUES (%s)"
    from Campus.week46.cli_crud.db.connector import execute_query
    success, cursor = execute_query(query, (name,))

    if success:
        print(f"Product '{name}' added successfully with ID: {cursor.lastrowid}")
