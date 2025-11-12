from Campus.week46.cli_crud.db.connector import execute_query


def view_products():
    """Display all products in the database"""
    query = "SELECT * FROM products ORDER BY id"
    results = (
        execute_query(query, fetch=True, dictionary=True))

    if results:
        print("\n" + "=" * 40)
        print("PRODUCTS LIST")
        print("=" * 40)
        for row in results:
            print(f"ID: {row['id']:3d} | Name: {row['name']}")
        print("=" * 40)
    else:
        print("No products found in the database")