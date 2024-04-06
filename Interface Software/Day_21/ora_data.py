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
    # cur.execute("create table servicesdata (name varchar(255), address varchar(255))")
    # cur.execute("create table servicesdata (name varchar(255), address varchar(255))")
    # print("ok")
    sql = "INSERT INTO servicesdata (name, address) VALUES (:1, :2)"
    # val = ("John", "Highway 21")

    val = [("Subham", "Park Lane 38"),("Sourav", "Highway 25"),]
    
    # cur.execute(sql, val)
    
    cur.executemany(sql, val)

    conn.commit()

    print(cur.rowcount, "record inserted.")
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