import mysql.connector
print(1)
#Create the connection object
myconn = mysql.connector.connect(host="localhost", port=3308, user="root", passwd="", database="gift")
print(myconn)
# #creating the cursor object
cur = myconn.cursor()
try:
    cur.execute("select * from studentgift")
    result = cur.fetchall()
    for c in result:
        print(c)
except:
    myconn.rollback()