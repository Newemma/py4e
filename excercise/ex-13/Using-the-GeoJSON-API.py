import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Irkutsk State University
while True:
    address = input('Enter location: ')
    if len(address) < 1:  break
       # address = 'South Federal University'
    url = serviceurl + urllib.parse.urlencode({'address': address})  # key-value pair using colon.

    parms = dict()#键值对 address:xxx,key:xxx；所以创建一个dictionary
    parms['address'] = address #字典赋值
    if api_key is not False:
        parms['key'] = api_key #使用正确的api-key
    url = serviceurl + urllib.parse.urlencode(parms)#！！parms 包含address and api-key；--encode
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)#context = ctx（short name of context）--is a key-value pair；可以省略？
    data = uh.read().decode()
    #print(data) data在Python中是一串代码，不是原网页
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    #Python中一般使用try-except捕获异常。这样，如果引发异常，程序可对异常进行处理。避免了Traceback（most recent call last）等这样一些不友好的语句出现。

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    #必要的检查和防止报错
    #print(json.dumps(js, indent=4))  #数清楚缩进，第几个缩进，就需要几个[]:
    print('Place id',js['results'][0]['place_id'])#单双引号均可，['']内容直接copy上一行print出来的，手输入容易输错

