import mysql.connector as myc

df = myc.connect(host="localhost",user="root",passwd="vksahu399",database="vivek")

mycursor = df.cursor()

#input from user

d_id=int(input("Enter Id Numer for Delete : "))



id =(d_id,)

#show data before delete
s_q="SELECT * FROM Friends where id=%s"

mycursor.execute(s_q,id)

myresult = mycursor.fetchone()

#print(myresult[1])

choice=input("Do you want to delete  :{} ? (y/n) :".format(myresult[1]))



if choice=='y' or choice=='Y':
    q ="DELETE FROM Friends WHERE id=%s"
    mycursor.execute(q,id)
    df.commit()
    print(mycursor.rowcount, "record deleted")

else:
    print ("try again")



