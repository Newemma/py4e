from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url is http://py4e-data.dr-chuck.net/known_by_Kelice.html
url = input("Enter URL: ")
count = int(input("Enter count: "))#int()
position = int(input("Enter position: "))


names = [] #make a space list

while count > 0:
    print ("retrieving: {0}".format(url))
# {0}它是格式方法的一个指示符，您希望它被格式的第一个（索引零）参数替换。
#例如("2 + 2 = {0}".format(4)）
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup('a')
    name = anchors[position-1].string#astract string\names-using method:.string
    names.append(name)
    url = anchors[position-1]['href']#astract href-using ['href']
    count -= 1#equal to count = count-1

print (names[-1])#print the last 1\\print(name[-3]):倒数第三个
