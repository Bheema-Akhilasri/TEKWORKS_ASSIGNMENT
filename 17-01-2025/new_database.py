import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="root",
  password="root",
  database="coe"
)

mycursor = mydb.cursor()

sql = "INSERT INTO city (name, address) VALUES (%s, %s)"
val = [
  ('aunty', 'hyd'),
  ('sita', 'aus'),
  ('bro', 'mlg'),
  ('juli', 'wnp'),
  ('jack', 'srpt'),
  ('john', 'nlg'),
  ('jesi', 'hyd'),
  ('jet', 'nlg'),
  ('musk', 'hyd'),
  ('min', 'uk'),
]

mycursor.executemany(sql, val)

mydb.commit()
