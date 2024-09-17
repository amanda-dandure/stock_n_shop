from sql_connection import get_sql_connection #establishing a connection to the database

def get_all_products(connection): # retriving all product data
    cursor = connection.cursor() #retriving results
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query) #executing the SQL query stored in the query
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor: #iterating over each row of data returned by the cursor.
        response.append({ #creating a dictionary with the retrieved product data as key-value pairs 
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product): #inserting a new product record into the database
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)") #preventing SQL injection vulnerabilities
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data) #executing the prepared statement (query) using the data tuple
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor() # a channel to execute SQL statements and retrieve results
    query = ("DELETE FROM products where product_id=" + str(product_id)) #a SQL query to delete a product from the products table
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid #checking if the deletion was successful


if __name__ == '__main__': #conditional block ensures that the code below it is only executed when the script is run directly, not when imported as a module
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))
