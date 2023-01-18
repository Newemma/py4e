import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#http://py4e-data.dr-chuck.net/comments_1702977.json
#html = input('Enter location:')
print('Enter location: http://py4e-data.dr-chuck.net/comments_42.json')
html = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Retrieving',html)
jsonline = urllib.request.urlopen(html).read().decode()
print('Retrieved',len(jsonline),'characters')
print(jsonline)
info = json.loads(jsonline)
print(info)
print('=======================================')
for item in info:
    print('num',item[0]['count'])
    #print('nums',item['name'])
#Count: 50
#Sum: 2...
