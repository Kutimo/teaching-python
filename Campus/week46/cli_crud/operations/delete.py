from Campus.week46.cli_crud.db.connector import execute_query
from Campus.week46.cli_crud.operations.read import view_products
from Campus.week46.cli_crud.utils.valdidator import get_valid_input


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
