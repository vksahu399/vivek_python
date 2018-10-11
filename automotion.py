#import firebase library
from firebase import firebase

database_url='https://python-1abb9.firebaseio.com'

#create instance of firebase connectivity
firebase = firebase.FirebaseApplication(database_url, None)

# my sample database in firebasepython
#{'ac': '0', 'cooler': '0', 'fan': '1', 'light': '1'}

#get all tha database data in json
data = firebase.get('/', None)

#print all the data
print (data)
fan_status = firebase.put('/',"age","18")
#output of fan status
print ("---",fan_status)