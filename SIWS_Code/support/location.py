import requests
import json
def getloc():
 r = requests.get('http://ipinfo.io/json')
 data = (json.loads(r.text))
 city = data['city']
 loc=data['loc']
 return city+loc 
#return (r.text)