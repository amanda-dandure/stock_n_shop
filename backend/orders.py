from datetime import datetime
from sql_connection import get_sql_connection  # Import for getting SQL connection

def insert_order(connection, order):
    """
    Inserts a new order and its details into the database.

    Args:
        connection: A database connection object.
        order: A dictionary containing customer information and order details.

    Returns:
        The ID of the newly inserted order.
    """

    cursor = connection.cursor()

    # Define the SQL query to insert order data
    order_query = ("INSERT INTO orders "
                   "(customer_name, total, datetime)"
                   "VALUES (%s, %s, %s)")

    # Prepare data for the order insert query
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    # Execute the query and get the last inserted row ID (order ID)
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    # Define the SQL query to insert order details
    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s,   
 %s)")

    # Prepare data list for order details insert (one record per detail)
    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,  # Insert the previously obtained order ID
            int(order_detail_record['product_id']),  # Convert product ID to integer
            float(order_detail_record['quantity']),  # Convert quantity to float
            float(order_detail_record['total_price'])  # Convert total price to float
        ])

    # Execute the query with multiple inserts (executemany) for efficiency
    cursor.executemany(order_details_query, order_details_data)

    # Commit the changes to the database
    connection.commit()

    return order_id

def get_order_details(connection, order_id):
    """
    Retrieves order details for a specific order ID.

    Args:
        connection: A database connection object.
        order_id: The ID of the order to get details for.

    Returns:
        A list of dictionaries containing order detail information.
    """

    cursor = connection.cursor()

    # Initial query attempting to select all columns (replaced later)
    query = "SELECT * from order_details where order_id = %s"

    # Improved query to join with products table and get product information
    query = "SELECT order_details.order_id, order_details.quantity, order_details.total_price, "\
            "products.name, products.price_per_unit FROM order_details LEFT JOIN products on " \
            "order_details.product_id = products.product_id where order_details.order_id   
 = %s"

    # Prepare data for the query (order ID)
    data = (order_id, )

    # Execute the query with the prepared data
    cursor.execute(query, data)

    # List to store retrieved order detail records
    records = []
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        # Create a dictionary for each order detail record
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit   

        })

    # Close the cursor to release resources
    cursor.close()

    return records


def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # Append order details in each order
    for record in response:
        record['order_details'] = get_order_details(connection, record['order_id'])

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(get_order_details(connection,4))
    # print(insert_order(connection, {
    #     'customer_name': 'amandah',
    #     'total': '500',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 50
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 1,
    #             'total_price': 30
    #         }
    #     ]
    # }))
