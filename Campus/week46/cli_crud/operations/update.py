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
