import mysql.connector as dbcon
con=dbcon.connect(
    host="localhost",
    user="root",
    passwd="vksahu399",
    database="vivek")

#print(con)

mycursur=con.cursor()
q="insert into Students(Roll_num,Name,class)values(%s,%s,%s)"

r=input("enter roll no.")
n=input("enter name")
c=input("enter class")


val=(int(r),n,int(c))
mycursur.execute(q,val)
con.commit()
print(mycursur.rowcount,"row inserted")
