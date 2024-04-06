import mysql.connector

mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="",database="mydatabase")

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)