import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='coe'
)
mycursor=mydb.cursor()
sql='select * from city'
mycursor.execute(sql)
res=mycursor.fetchall()
for x in res:
    print(x)
