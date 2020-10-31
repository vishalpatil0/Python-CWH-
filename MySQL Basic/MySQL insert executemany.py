import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")

mycursor=mydb.cursor()

# mycursor.execute("create table Testing_1(id integer not null, name varchar(20))")

insertQuery="insert into Testing_1 values(%s,%s)"

data=[(95,"Shubham"),(98,"Shruti")]

mycursor.executemany(insertQuery,data)

mydb.commit()   #we need to use commit() because without commit() you can't put the changes of insert query in database
mydb.close()