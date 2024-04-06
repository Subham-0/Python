import cx_Oracle
import datetime as dt
import pandas as pd




connStr = 'gift/gift@localhost:1521/xe'

conn = cx_Oracle.connect(connStr)
cur = conn.cursor()

# sqlTxt = 'INSERT INTO students (st_name, dob,student_id) VALUES (\'xyz\', to_date(\'01-01-2003\'),3243)'

#use sql placeholder    
# sqlTxt = 'INSERT INTO students (st_name, dob,student_id) VALUES (:1, :2, :3)'
# cur.execute(sqlTxt,('xyz', dt.date(2023,1,1),34 ))

#this way in the parameter substitusion you can use the real data type instead of string into the sql statement  and this also save from sql injection attack


#if we want to add 100 rows then it is so difficult write every insert then execute every insert

dataTuples =[
    ('subham dash', dt.date(2002, 1, 1),2205298187),
    ('sourav pradhan', dt.date(2001, 10, 12), 2205298102)
    ]
# sqlTxt = 'INSERT INTO students (st_name, dob,student_id) VALUES (:1, :2, :3)'
# cur.executemany(sqlTxt,dataTuples)
# rowCount = cur.rowcount
# print("number of inserted rows =", rowCount)

# sqlTxt = 'INSERT INTO students (st_name, dob,student_id) VALUES (:1, :2, :3)'
# cur.executemany(sqlTxt,dataTuples)

# sqlTxt = 'DELETE from students where (st_name=:1 and dob=:2 )and student_id=:3'
# cur.executemany(sqlTxt,dataTuples)
# rowCount = cur.rowcount
# print("number of deleted rows =", rowCount)

# conn.commit()

sqltxt = 'select st_name,dob,student_id from students where st_name=:1 order by st_name,student_id'
cur.execute(sqltxt,('subham dash',))
# cur.executemany(sqltxt, dataTuples)

records = cur.fetchall()
print(records)

df = pd.DataFrame.from_records(records,columns=["st_name","dob","student_id"])
print(df)






cur.close()
conn.close()