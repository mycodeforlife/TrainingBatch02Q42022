import csv
import mysql.connector

db_connection = mysql.connector.connect(host="localhost", port=3306, user="root", password="password",
                                        auth_plugin='mysql_native_password', database="grocery_store")
db = db_connection.cursor()

# below logic is to read the csv file and to upload it into the transaction table
with open("samplebankstatement1.csv", newline='') as input_file:
    data_content = csv.DictReader(input_file)
    print(data_content)
for each in data_content:
    query = "insert into  Transactions_list(Transaction_Date,Trans_Description,Amount) values (\""+each["*Date"]+"\",\""+each["Description"]+"\","+each["*Amount"]+")"
    print(query)
    db.execute(query)
    db_connection.commit()
cd
#Select unique merchants from transaction table

query = "SELECT DISTINCT Description FROM Transactions_list ORDER BY Trans_Description"
#print(query)
db.execute(query)
results = db.fetchall()
print(results)
results

# insert fetched merchant details into merchant table
for each in results:
    print(each)
    query = "insert into  Merchant_list (Merchant_Name) values (%s)"
    db.execute(query, each)
    db_connection.commit()

# results = db.fetchall()
# print(results)
