from crud_cli.db.connector import execute_query


def read_products():

    query = "SELECT * FROM products ORDER BY id"
    results = (execute_query(query, fetch=True, dictionary=True))

    if results:
        print("\n" + "-" * 35)
        print("Products list:")
        print("-" * 35)
        for row in results:
            print(f"ID: {row['id']:3d} | Name: {row['name']}")
        print("-" * 35)
    else:
        print("no products found in the database")