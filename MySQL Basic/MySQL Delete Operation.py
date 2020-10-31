import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")

mycursor=mydb.cursor()

mycursor.execute("delete from testing_1 where id=334")

mydb.commit() # you also need to use commit after deletion of data