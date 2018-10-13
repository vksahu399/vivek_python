import mysql.connector as dbcon
con=dbcon.connect(
    host="localhost",
    user="root",
    passwd="vksahu399",
    database="vivek")

#print(con)

mycursur=con.cursor()
q="insert into Students(Roll_num,Name,class)values(%s,%s,%s)"
val=(512,"Ragini",10)
mycursur.execute(q,val)
con.commit()
print(mycursur.rowcount,"row inserted")
