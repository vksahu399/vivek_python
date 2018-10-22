import urllib.request
import urllib.parse
import json
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('your API key', '9196xxxxxxxx',
    'TXTLCL', 'This is your message')

print (resp)
parsed_json = json.loads(resp)

print(parsed_json['status'])
