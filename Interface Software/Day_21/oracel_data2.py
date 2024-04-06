import cx_Oracle

# connection string in the format
# <username>/<password>@<dbHostAddress>:<dbPort>/<dbServiceName>
connStr = 'gift/gift@localhost:1521/xe'


conn = cx_Oracle.connect(connStr)

try:
    # create a connection object
    conn = cx_Oracle.connect(connStr)

    # get a cursor object from the connection
    cur = conn.cursor()

    # do something with the database
    cur.execute("SELECT * FROM servicesdata")

    myresult = cur.fetchall()

    for x in myresult:
        print(x)
except Exception as err:
    print('Error while connecting to the db')
    print(err)
finally:
    if(conn):
        # close the cursor object to avoid memory leaks
        cur.close()

        # close the connection object also
        conn.close()
print("execution complete!")