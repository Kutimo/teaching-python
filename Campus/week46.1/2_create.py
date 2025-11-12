from db.connector import get_connection


def create_product(name):
    # Get a connection to the database with our helper function.
    connection = get_connection()

    # Check if the connection was successful
    if not connection:
        print("Could not continue without a db connection")
        return # exit function early if no connection

    try:
        # Create a cursor object to execute sql commands

        with connection.cursor() as cursor:
            query = "INSERT INTO products (name) VALUES (%s)"

            cursor.execute(query, (name,))

            connection.commit()

            print(f"product {name} was created successfully")

    except Exception as e:
        print(f"Insert error: {e} ")
        # reverts change if error happens
        connection.rollback()

    finally:
        connection.close()
        print("connection closed")

def main():
    create_product("pineapple")

if __name__ == "__main__":
    main()


