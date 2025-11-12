"""
Product Management System - CLI Menu Application
Combines CRUD operations with a user-friendly menu interface
DRY (Don't Repeat Yourself) version
"""

from db.connector import get_connection, execute_query


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


def add_product():
    """Add a new product to the database"""
    name = get_valid_input("Enter product name: ")
    if not name:
        return

    query = "INSERT INTO products (name) VALUES (%s)"
    success, cursor = execute_query(query, (name,))

    if success:
        print(f"Product '{name}' added successfully with ID: {cursor.lastrowid}")


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


def delete_product():
    """Delete a product from the database"""
    view_products()

    product_id = get_valid_input("\nEnter product ID to delete: ", input_type='int')
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
                add_product()
            case '2':
                view_products()
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