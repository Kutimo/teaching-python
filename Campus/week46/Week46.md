## Week 46

## SQL

```sql 
CREATE SCHEMA IF NOT EXISTS oliver_db;
USE oliver_db;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          name VARCHAR(255)
);

INSERT INTO products (name) VALUES
                                ('Apple'),
                                ('Banana'),
                                ('Orange'),
                                ('Grapes'),
                                ('Mango');

```

## sql connector

current dir
|
|--db
| |- __init__.py
| |- connector.py
|
|-- 1_select.py

```python
import mysql.connector
from mysql.connector import Error


def get_connection():
    """Create and return your MySQL connection."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gokstad",
            database="oliver_db",
            charset='utf8'
        )

        if connection.is_connected():
            print("Connected to MySQL")
            return connection

    except Error as e:
        print(f"MySQL connection error: {e}")
        return None

```

```python

from db.connector import get_connection


def main():
    connection = get_connection()

    if not connection:
        print("Cannot continue without a database connection.")
        return

    try:
        # Use dictionary=True for readable output
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM products;")
            results = cursor.fetchall()

            if results:
                print("Products found:")
                for row in results:
                    print(
                        row)  # e.g., {'id': 1, 'name': 'Shoes', 'price': 99.99}
            else:
                print("No products found in the table.")

    except Exception as e:
        print(f"Query error: {e}")

    finally:
        connection.close()
        print("Connection closed")


if __name__ == "__main__":
    main()

```

Task 1: Insert a single product

Write a Python function insert_product(name) that inserts one product into
the products table.

Requirements:

1. Get a database connection using get_connection()
2. Create a cursor and write an INSERT query: "INSERT INTO products (name)
   VALUES (%s)"
3. Execute the query: cursor.execute(query, (name,))
    - Note: (name,) is a tuple — the comma is required!
4. Commit the changes: connection.commit()
5. Use try/except/finally to handle errors and close the connection
    - In except: use connection.rollback() to undo changes
    - In finally: close the connection

Example usage:
insert_product("Pineapple")

Expected output:
Product 'Pineapple' inserted successfully with ID: 6
Connection closed

Hint: Use cursor.lastrowid to get the auto-generated ID after inserting.

``` python
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

```

Task 2: Insert several products
Write a Python function that inserts several products at once.

Example list: ["Kiwi", "Peach", "Strawberry"].

Use a loop or executemany to insert them.

Print a message for each product added.

```python
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
```

## Cli Crud menu
```
├── db/
│ ├── __init__.py
│ └── connector.py # Database connection & execute_query
│
├── operations/
│ ├── __init__.py
│ ├── create.py # Insert operations
│ ├── read.py # Select operations
│ ├── update.py # Update operations
│ └── delete.py # Delete operations
│
├── utils/
│ ├── __init__.py
│ └── validators.py
```

Connector:
```python
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
```

utils: 
```python
def get_valid_input(prompt, input_type='str', allow_empty=False):
    """
    Get and validate user input.

    Args:
        prompt: Input prompt message
        input_type: Expected type ('str' or 'int')
        allow_empty: Allow empty strings

    Returns:
        Valid input or None if invalid
    """
    try:
        value = input(prompt).strip()

        if input_type == 'str':
            if not allow_empty and not value:
                print("Input cannot be empty!")
                return None
            return value

        elif input_type == 'int':
            return int(value)

    except ValueError:
        print("Invalid input! Please enter a valid number")
        return None

```


create:
```python
from Campus.week46.cli_crud.utils.valdidator import get_valid_input


def create_product():
    """Add a new product to the database"""
    name = get_valid_input("Enter product name: ")
    if not name:
        return

    query = "INSERT INTO products (name) VALUES (%s)"
    from Campus.week46.cli_crud.db.connector import execute_query
    success, cursor = execute_query(query, (name,))

    if success:
        print(f"Product '{name}' added successfully with ID: {cursor.lastrowid}")

```

Read: 
```python
from Campus.week46.cli_crud.db.connector import execute_query


def read_products():
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
```

Update:
```python
from Campus.week46.cli_crud.db.connector import execute_query
from Campus.week46.cli_crud.operations.read import view_products
from Campus.week46.cli_crud.utils.valdidator import get_valid_input


def update_product():
    """Update an existing product's name"""
    view_products()

    product_id = get_valid_input("\nEnter product ID to update: ", input_type='int')
    if product_id is None:
        return

    new_name = get_valid_input("Enter new product name: ")
    if not new_name:
        return

    query = "UPDATE products SET name=%s WHERE id=%s"
    success, cursor = execute_query(query, (new_name, product_id))

    if success:
        if cursor.rowcount > 0:
            print(f"Product ID {product_id} updated to '{new_name}'")
        else:
            print(f"No product found with ID {product_id}")
```

Delete:
```python
from Campus.week46.cli_crud.db.connector import execute_query
from Campus.week46.cli_crud.operations.read import view_products
from Campus.week46.cli_crud.utils.valdidator import get_valid_input


def delete_product():
    """Delete a product from the database"""
    view_products()

    product_id = get_valid_input("\nEnter product ID to delete: ",
                                 input_type='int')
    if product_id is None:
        return

    confirm = get_valid_input(
        f"Are you sure you want to delete product ID {product_id}? (Y/n): "
    ).lower()

    if confirm != 'y':
        print("Deletion cancelled")
        return

    query = "DELETE FROM products WHERE id=%s"
    success, cursor = execute_query(query, (product_id,))

    if success:
        if cursor.rowcount > 0:
            print(f"Product ID {product_id} deleted successfully")
        else:
            print(f"No product found with ID {product_id}")

``` python
"""
Product Management System - CLI Menu Application
Combines CRUD operations with a user-friendly menu interface
"""
def display_menu():
    """Display the main menu"""
    print("\n" + "-" * 30)
    print("   PRODUCT MANAGEMENT SYSTEM")
    print("-" * 30)
    print("1. Add Product")
    print("2. View All Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    print("-" * 30)


def main():
    """Main application loop"""
    print("\nWelcome to Product Management System!")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        match choice:
            case '1':
                create_product()
            case '2':
                read_products()
            case '3':
                update_product()
            case '4':
                delete_product()
            case '5':
                print("\nThank you for using Product Management System!")
                print("Goodbye!\n")
                break
            case _:
                print("Invalid choice! Please enter a number between 1 and 5")

        if choice != '5':
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

```

Task playlist cli menu:  

Database Table: playlist (id, song_title, artist_name, genre)

Requirements:

C (Create): Add a new song (title, artist, genre) to the playlist.

R (Read All): Display the complete playlist.

U (Update): Change the Genre of a song by its ID.

D (Delete): Delete a song from the playlist by its ID.

```python
import mysql.connector
import sys

# Make sure to install the connector: pip install mysql-connector-python

# ==============================================================================
# 🛠️ 1. CONFIGURATION (MYSQL CREDENTIALS)
# ==============================================================================

# IMPORTANT: Students MUST update these details to match their local MySQL setup.
DB_CONFIG = {
    'host': '127.0.0.1',  # e.g., 'localhost' or '127.0.0.1'
    'user': 'root',  # Change this to your MySQL username
    'password': 'gokstad',  # Change this to your MySQL password
    'database': 'oliver_db'  # Change this to the name of your database
}


def get_db_connection():
    """Returns a connection object to the MySQL database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print("\n" + "=" * 50)
        print("❌ ERROR: Database Connection Failed.")
        print(f"Details: {err}")
        print("Please check your DB_CONFIG (host, user, password, database) and ensure MySQL is running.")
        print("=" * 50 + "\n")
        # Exit the application if the connection fails
        sys.exit(1)


def create_table():
    """Connects to the database and creates the playlist table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # MySQL syntax for creating the table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlist (
                id INT AUTO_INCREMENT PRIMARY KEY,
                song_title VARCHAR(255) NOT NULL,
                artist_name VARCHAR(255) NOT NULL,
                genre VARCHAR(255)
            )
        """)
        conn.commit()
        # print("Database table initialized successfully.") # Optional confirmation
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()
        conn.close()


# ==============================================================================
# 🎶 2. CRUD OPERATIONS (FUNCTIONS)
# ==============================================================================

# C (Create): Add Song
def add_song(title, artist, genre):
    """Adds a new song to the playlist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use %s as the placeholder for MySQL
    query = "INSERT INTO playlist (song_title, artist_name, genre) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (title, artist, genre))
        conn.commit()
        print(f"\n✅ Added: '{title}' by {artist}.")
    except mysql.connector.Error as err:
        print(f"Error adding song: {err}")
    finally:
        cursor.close()
        conn.close()


# R (Read All): Display Playlist
def view_playlist():
    """Retrieves and prints all songs in the playlist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT id, song_title, artist_name, genre FROM playlist')
        songs = cursor.fetchall()

        if not songs:
            print("\n▶️ The playlist is empty.")
            return

        print("\n--- 🎧 Current Playlist 🎧 ---")
        print(f"{'ID':<4} | {'Song Title':<30} | {'Artist Name':<20} | {'Genre':<15}")
        print("-" * 75)

        for song in songs:
            # Data from MySQL needs to be formatted for printing
            print(f"{song[0]:<4} | {song[1]:<30} | {song[2]:<20} | {song[3]:<15}")
        print("-" * 75)

    except mysql.connector.Error as err:
        print(f"Error viewing playlist: {err}")
    finally:
        cursor.close()
        conn.close()


# U (Update): Change Genre
def update_song_genre(song_id, new_genre):
    """Updates the genre of a song based on its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE playlist SET genre = %s WHERE id = %s"
    try:
        cursor.execute(query, (new_genre, song_id))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"\n✅ Song ID {song_id} updated. New Genre: {new_genre}.")
        else:
            print(f"\n⚠️ Error: No song found with ID {song_id}.")

    except mysql.connector.Error as err:
        print(f"Error updating song: {err}")
    finally:
        cursor.close()
        conn.close()


# D (Delete): Delete Song
def delete_song(song_id):
    """Deletes a song from the playlist based on its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM playlist WHERE id = %s"
    try:
        cursor.execute(query, (song_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"\n🗑️ Song ID {song_id} deleted successfully.")
        else:
            print(f"\n⚠️ Error: No song found with ID {song_id} to delete.")

    except mysql.connector.Error as err:
        print(f"Error deleting song: {err}")
    finally:
        cursor.close()
        conn.close()


# ==============================================================================
# 💻 3. CLI INTERFACE (MAIN LOOP)
# ==============================================================================
def main():
    """The main command-line interface loop."""
    # Step 1: Ensure the database connection works and the table exists
    create_table()

    while True:
        print("\n--- Playlist Manager CLI (MySQL) ---")
        print("1. Add a new song (Create)")
        print("2. View the full playlist (Read All)")
        print("3. Update a song's genre (Update)")
        print("4. Delete a song (Delete)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            genre = input("Enter genre: ")
            add_song(title, artist, genre)

        elif choice == '2':
            view_playlist()

        elif choice == '3':
            view_playlist()  # Show list to help user choose ID
            try:
                song_id = int(input("Enter the ID of the song to update: "))
                new_genre = input("Enter the new genre: ")
                update_song_genre(song_id, new_genre)
            except ValueError:
                print("\n❌ Invalid input. Please enter a valid number for the ID.")

        elif choice == '4':
            view_playlist()  # Show list to help user choose ID
            try:
                song_id = int(input("Enter the ID of the song to delete: "))
                delete_song(song_id)
            except ValueError:
                print("\n❌ Invalid input. Please enter a valid number for the ID.")

        elif choice == '5':
            print("\n👋 Exiting Playlist Manager. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please select a number from 1 to 5.")


# ==============================================================================
# 🚀 4. ENTRY POINT
# ==============================================================================
if __name__ == '__main__':
    main()
```


## Flask

### Creating a virtual environment for python:

```bash
mkdir week46
cd week 46
```

Windows:  
![alt text](images/create_venv_win.png)  
Mac and linux:  
![alt text](images/create_venv_mac_&_linux.png)

then activate:

Linux and mac:  
![alt text](images/activate_linux_&_mac.png)

Windows:  
![alt text](images/activate_win.png)

Then install flask:

```bash
pip install Flask
```

## Old syntax of running a simple webserver:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    returns a short message on "localhost/"
    """
    return " hello Worlds! "


if __name__ == "__main__":
    app.run(debug=True)
```

Then:

```bash
py hello_world.py
```

## New syntax as of flask 2.2:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    returns a short message on "localhost/"
    """
    return " hello Worlds! "

```

Then:

```bash
flask --app app --debug run
```

```python
from flask import Flask, render_template
import random as rnd

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    returns a short message on "localhost/"
    """
    return " hello World! "


names = ["John", "jane", "doe"]


@app.route('/rnd')
def get_random_number():
    rnd_name = rnd.choice(names)
    return f"hello {rnd_name}"


@app.route('/html')
def get_html_file():
    return render_template("index.html")

```

my notes:

fix connection error docker with mysql
start docker container
docker exec -it ga-mysql-2025 mysql -u root -p
gokstad
