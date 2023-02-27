import csv
import mysql.connector

db_connection = mysql.connector.connect(host="localhost", port=3306, user="root", password="geethapavan",auth_plugin='mysql_native_password',database="PErsonalFinance")
db = db_connection.cursor()

with open("activity.csv", newline='') as input_file:
    data_content = csv.DictReader(input_file)
    print(data_content)

    for each in data_content:
        query = "insert into  Transactions (Description,Amount) values (\""+each["Description"]+"\","+each["Amount"]+")"
        print(query)
        db.execute(query)
        db_connection.commit()


# results = db.fetchall()
# print(results)


