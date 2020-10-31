import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")

mycursor=mydb.cursor()

mycursor.execute("drop table testing_1")

#Note: You don't need to use mydb.commit() after drop command
