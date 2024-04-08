import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="PAGAL",
  password="NallaPassword@123",
  database="sqlalchemy"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE students2 (name VARCHAR(255), phone INTEGER)")

mycursor.execute("INSERT INTO users VALUES(200 , 'pagal')")

tempcursor = mycursor
print(mycursor)
print(type(mycursor))
tempcursor.execute("SELECT * FROM users")

for x in tempcursor:
  print(x)
  print(type(x))

mydb.commit()

mycursor.close()