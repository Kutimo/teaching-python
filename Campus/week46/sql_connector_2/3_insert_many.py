from db.connector import get_connection


def insert_multiple_products_loop(product_names):
    connection = get_connection()

    if not connection:
        print("Cannot continue without a database connection.")
        return

    try:
        with connection.cursor() as cursor:
            product_query = "INSERT INTO products (name) VALUES (%s)"

            for name in product_names:
                cursor.execute(product_query, (name,))

            connection.commit()
            print(f"{len(product_names)} products inserted successfully")

    except Exception as e:
        print(f"Insert error: {e}")
        connection.rollback()

    finally:
        connection.close()
        print("Connection closed")


def main():
    # Example: Insert multiple products
    products = ["Pineapple", "Watermelon", "Strawberry", "Kiwi"]
    insert_multiple_products_loop(products)


if __name__ == "__main__":
    main()
