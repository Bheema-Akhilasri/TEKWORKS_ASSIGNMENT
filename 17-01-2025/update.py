import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='coe'
)
mycursor=mydb.cursor()
sql="UPDATE city SET address = 'wnp' WHERE name = 'sita'"
mycursor.execute(sql)
mydb.commit()
