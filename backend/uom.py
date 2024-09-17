def get_uoms(connection):
    """
    Retrieves all units of measure (UoMs) from the database.

    Args:
        connection: A database connection object.

    Returns:
        A list of dictionaries containing UoM data.
    """

    cursor = connection.cursor()  # Create a database cursor
    query = ("select * from uom")  # SQL query to select all UoMs
    cursor.execute(query)  # Execute the query

    response = []  # List to store UoM data
    for (uom_id, uom_name) in cursor:  # Iterate over query results
        response.append({  # Create a dictionary for each UoM
            'uom_id': uom_id,
            'uom_name': uom_name
        })

    return response  # Return the list of UoMs

if __name__ == '__main__':
    from sql_connection import get_sql_connection  # Import for database connection

    connection = get_sql_connection()  # Establish a database connection
    print(get_uoms(connection))  # Call the function to retrieve and print UoMs
