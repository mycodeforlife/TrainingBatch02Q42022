import csv
from time import strftime

import mysql.connector

mydb = mysql.connector.connect(host="localhost", port=3306, user="root", password="indira",database="first")
db = mydb.cursor()


with open("smlsmple.csv", newline='') as input_file:
    data_content = csv.DictReader(input_file)
    for each in data_content:
        query = "insert into transactions (Description,Amount,date) values (\""+each["Description"]+"\","+each["Amount"]+","+each["date"]+")"
        print(query)

        db.execute(query)
        mydb.commit()


#results=db.fetchall()

#print(results)



