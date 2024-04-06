import mysql.connector
mydb = mysql.connector.connect(host="localhost",port=3308,user="root",password="")
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE mydatabase")
except:
    mydb.rollback()
mydb.close

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",port=3308,user="root",password="")
# mycursor = mydb.cursor()
# try:
#     mycursor.execute("CREATE DATABASE projectdb")
# except:
#     mydb.rollback()
# mydb.close