import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")

mycursor=mydb.cursor()

# mycursor.execute("select name from testing_1 where id=334   ")

# for db in mycursor:
#     print(db)


#########Fetchone################

mycursor.execute("select * from testing_1")

myresult=mycursor.fetchall()

for db in myresult:
    print(db)