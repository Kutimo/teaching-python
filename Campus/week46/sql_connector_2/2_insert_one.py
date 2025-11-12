from Campus.week46.sql_connector_2.db.connector import get_connection


def insert_product(name):
    # Get a connection to the database using our helper function
    connection = get_connection()

    # Check if the connection was successful
    if not connection:
        print("Cannot continue without a database connection.")
        return  # Exit the function early if no connection

    try:
        # Create a cursor object to execute SQL commands
        # Using 'with' ensures the cursor is closed automatically
        with connection.cursor() as cursor:
            # Prepare the SQL INSERT query
            # %s is a placeholder that will be safely replaced with the actual value
            query = "INSERT INTO products (name) VALUES (%s)"

            # Execute the query with the product name
            # (name,) is a tuple - the comma is important even with one value
            cursor.execute(query, (name,))

            # Save the changes to the database
            # Without commit(), the INSERT won't be permanently saved
            connection.commit()

            # Print success message with the auto-generated ID
            # cursor.lastrowid gives us the ID that was automatically created
            print(f"Product '{name}' inserted successfully with ID: {cursor.lastrowid}")

    except Exception as e:
        # If any error occurs during the insert
        print(f"Insert error: {e}")

        # Undo any changes made during this transaction
        # This keeps the database in a consistent state
        connection.rollback()

    finally:
        # This block ALWAYS runs, whether there was an error or not
        # Close the database connection to free up resources
        connection.close()
        print("Connection closed")


def main():
    # Example usage: Insert a product named "Pineapple"
    insert_product("Pineapple")


# This checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Run the main function