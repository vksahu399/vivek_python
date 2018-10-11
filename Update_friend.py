import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="vksahu399",
  database="vivek"
)

mycursor = mydb.cursor()

sql = "UPDATE Friends SET 1 = %s WHERE 1 = %s"
val = ("vivek", "vivek sahu")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")