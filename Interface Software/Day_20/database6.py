import mysql.connector

mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="",database="mydatabase")

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)