from crud_cli.operations.create import create_product
from crud_cli.operations.read import read_products

def display_menu():
    print("Product management system")
    print("-" * 35)
    print("1. Add product")
    print("2. View all products")
    print("5. Exit")


def main():

    while True:
        display_menu()
        choice =input("\n Enter your choice: (1-5): ").strip()

        match choice:
            case "1":
                create_product()
            case "2":
                read_products()
            case "5":
                print("Exiting...")
                break
            case _:
                print("invalid choice! please enter a number between 1 and 5")

        if choice != "5":
            input("Press enter to continue...")


if __name__ == "__main__":
    main()