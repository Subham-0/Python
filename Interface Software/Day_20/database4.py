import mysql.connector

mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="",database="mydatabase")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)