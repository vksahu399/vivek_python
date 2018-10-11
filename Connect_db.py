import mysql.connector as dbcon
con=dbcon.connect(
    host="localhost",
    user="root",
    passwd="vksahu399",
    database="vivek")

print(con)
