import mysql.connector

mydb = mysql.connector.connect(host="localhost",port="3308",user="root",passwd="",database="mydatabase")

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
val = [("Harish", "Khorda"),("Bikash", "Jajpur"),]
# mycursor.executema(sql, val)
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")