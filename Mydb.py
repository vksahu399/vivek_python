import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="vksahu399",
  database="vivek"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Friends")

myresult = mycursor.fetchall()
print("ID Name  ")
print("-----------------------------------")
for x in myresult:
  print(x[0],x[1],x[2],x[3],x[4])
  print("--------------------------------")