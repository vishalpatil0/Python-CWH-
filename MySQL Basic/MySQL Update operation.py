import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")

mycursor=mydb.cursor()

update_1="update Testing_1 set name='vishu' where id=121"

mycursor.execute(update_1)

mydb.commit()

mycursor.close()
mydb.close()