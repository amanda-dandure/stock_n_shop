from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

# Import DAO (Data Access Object) modules for product, order, and UoM management
import products_dao
import orders_dao
import uom_dao

# Create a Flask application instance
app = Flask(__name__)

# Establish a database connection using get_sql_connection function
connection = get_sql_connection()

# ---------- API Endpoints ----------

@app.route('/getUOM', methods=['GET'])
def get_uom():
    """
    API endpoint to retrieve all Unit of Measure (UoM) data.

    Returns:
        JSON response containing a list of UoM dictionaries.
    """

    response = uom_dao.get_uoms(connection)  # Call UoM DAO function to get data
    response = jsonify(response)  # Convert data to JSON format

    # Allow access from any origin for development purposes (consider security later)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    """
    API endpoint to retrieve all product data.

    Returns:
        JSON response containing a list of product dictionaries.
    """

    response = products_dao.get_all_products(connection)  # Call Product DAO function
    response = jsonify(response)  # Convert data to JSON format

    # Allow access from any origin for development purposes (consider security later)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    """
    API endpoint to insert a new product.

    Request Body:
        JSON data containing product details (refer to products_dao.insert_new_product).

    Returns:
        JSON response containing the newly inserted product ID.
    """

    request_payload = json.loads(request.form['data'])  # Parse JSON data from request
    product_id = products_dao.insert_new_product(connection, request_payload)  # Call Product DAO function

    response = jsonify({  # Create JSON response with product ID
        'product_id': product_id
    })

    # Allow access from any origin for development purposes (consider security later)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    """
    API endpoint to retrieve all order data.

    Returns:
        JSON response containing a list of order dictionaries.
    """

    response = orders_dao.get_all_orders(connection)  # Call Order DAO function
    response = jsonify(response)  # Convert data to JSON format

    # Allow access from any origin for development purposes (consider security later)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    """
    API endpoint to insert a new order.

    Request Body:
        JSON data containing order details (refer to orders_dao.insert_order).

    Returns:
        JSON response containing the newly inserted order ID.
    """

    request_payload = json.loads(request.form['data'])  # Parse JSON data from request
    order_id = orders_dao.insert_order(connection, request_payload)  # Call Order DAO function

    response = jsonify({  # Create JSON response with order ID
        'order_id': order_id
    })

    # Allow access from any origin for development purposes (consider security later)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    """
    API endpoint to delete a product.

    Request Body:
        product_id as a string in request.form['product_id'].

    Returns:
        JSON response containing the deleted product ID.
    """

    return_id = products_dao.delete_product(connection, request.form['product_id'])  # Call Product DAO function

    response = jsonify({  # Create JSON response with deleted product ID
        'product_id': return_id
    })

    # Allow access from any origin for development purposes (consider security)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Stock 'N Shop")
    app.run(port=5000)


