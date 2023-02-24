import mysql.connector
connection = mysql.connector.connect(host='localhost', database='grocery_store', user='root', password='password')
if connection.is_connected(): print("Connection Successfully")