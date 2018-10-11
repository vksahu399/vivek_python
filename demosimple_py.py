#import firebase library
from firebase import firebase

database_url='Your database url wothout last /'

#create instance of firebase connectivity
firebase = firebase.FirebaseApplication(database_url, None)

# my sample database in firebase
#{'ac': '0', 'cooler': '0', 'fan': '1', 'light': '1'}

#get all tha database data in json
data = firebase.get('/', None)

#print all the data
print (data)

# firebase database update .
# firebase.put(data,key,value)

#updating fan status
fan_status = firebase.put('/',"fan","1")
#output of fan status
print ("---",fan_status)
#updating light status
light_status = firebase.put('/',"light","1")
#output of light status
print ("---",light_status)