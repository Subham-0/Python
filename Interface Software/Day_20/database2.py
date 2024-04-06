import mysql.connector
mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="",database="mydatabase")
mycursor = mydb.cursor()
print("connection successfull")

mycursor.execute("create table customers (name varchar(255), address varchar(255))")
print("ok")


   

#Insert
"""after creating the connection object and then we are inserting a record by default insert setment are    not commited so we have to write a commit method (my connection.commit)
In java it is autometically commited
it is the part of the acid propertity where commit is  the compulsy"""