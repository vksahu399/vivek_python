import mysql.connector as myc

af=myc.connect(host="localhost",user="root",passwd="vksahu399",database="vivek")

mycursur=af.cursor()

f="insert into Friends(Name,Birthday,Mob_num,Mail)values(%s,%s,%s,%s)"

n=input("enter name")
b=input("enter dob (yyyy-mm-dd)")
m=input("enter mob no.")
ma=input("enter mail")

val=(n,b,m,ma)
mycursur.execute(f,val)
af.commit()
print(mycursur.rowcount,"row inserted")