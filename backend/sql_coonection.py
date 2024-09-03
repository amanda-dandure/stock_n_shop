import datetime #importing the datetime module
import mysql.connector

__cnx = None #declaring a global variable named __cnx 

def get_sql_connection():
  print("Opening the MySQL connection")
  global __cnx

  if __cnx is None: #if the __cnx variable is currently None, indicating that a connection has not been established yet
    __cnx = mysql.connector.connect(user='root', password='AAmm!!99', database='ss')

  return __cnx #returns the __cnx variable, which now contains the established database connection object


