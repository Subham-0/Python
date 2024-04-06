import mysql.connector

mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="",database="mydatabase")

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Kendrapara 123' WHERE address = 'Park Lane 38'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")