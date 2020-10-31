import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")

# if(mydb):
#     print("Connection is successfull")
# else:
#     print("Connection unsuccessfull")

mycursor=mydb.cursor()

# mycursor.execute("show databases")
#
# for db in mycursor:
#     print(db)

# mycursor.execute("use learning")   #instead of this command you can use mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")


# mycursor.execute("create table Testing_1(id integer not null, name varchar(20))")
#
# mycursor.execute("show full tables")
#
# for db in mycursor:
#     print(db)

# insertQuery="insert into Testing_1 values(%s,%s)"
#
# data=[(121,"vishal"),(321,"namu")]
#
# mycursor.executemany(insertQuery,data)
#
# mydb.commit()  # you need to use commit after executemany() method