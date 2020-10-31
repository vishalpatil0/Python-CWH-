import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")

mycursor=mydb.cursor()

mycursor.execute("show tables")   # show full tables

for db in mycursor:
    print(db)
