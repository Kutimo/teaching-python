"""
Product Management System - CLI Menu Application
Combines CRUD operations with a user-friendly menu interface
"""
from Campus.week46.cli_crud.operations.create import add_product
from Campus.week46.cli_crud.operations.delete import delete_product
from Campus.week46.cli_crud.operations.read import view_products
from Campus.week46.cli_crud.operations.update import update_product


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
