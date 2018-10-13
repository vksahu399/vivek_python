import mysql.connector as dbcon
con=dbcon.connect(
    host="localhost",
    user="root",
    passwd="vksahu399",
    database="vivek")

#print(con)

mycursur=con.cursor()
#q="select * from Students"
q="select Name,Roll_num from Students"
mycursur.execute(q)
result= mycursur.fetchall() # data fetch from table

#result= mycursur.fetchone()

#print(result)

for x in result:
    print(x)