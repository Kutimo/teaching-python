from db.connector import get_connection

def main():
    connection = get_connection()

    if not connection:
        print("Cannot continue without a database connection.")
        return

    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM products;")
            results = cursor.fetchall()

            if results:
                print("Products found:")
                for row in results:
                    print(row)
            else:
                print("No products found in the table.")

    except Exception as e:
        print(f"Query error: {e}")

    finally:
        connection.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
