from db.connector import get_connection


def main():
    connection = get_connection()

    if not connection:
        print("cannot continue with a db connection")
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
                print("No products found")
    except Exception as e:
        print(e)

    finally:
        connection.close()
        print("db connection is closed")


if __name__ == "__main__":
    main()
