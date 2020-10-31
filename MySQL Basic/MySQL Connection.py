import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="vishu",database="learning")
""" if you don't mention database name here ^  then you can use it as follow:
    mydb=mysql.connector.connect(host="localhost",user="root",password="vishu")
    mycursor.execute("use learning")
"""
if(mydb):
    print("Connection is successfull")
else:
    print("Connection unsuccessfull")