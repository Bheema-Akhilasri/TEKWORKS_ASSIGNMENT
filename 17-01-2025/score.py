import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='coe'
)
mycursor=mydb.cursor()
sql='select sname , marks from stu where marks between 90 and 100'
mycursor.execute(sql)
res=mycursor.fetchall()
for x in res:
    print(x)
