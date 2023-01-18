# /Users/nana/Desktop/py4e/ex-13-01/ex-13-01.py
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
#xml一般指可扩展标记语言。 可扩展标记语言，标准通用标记语言的子集，简称XML
#书写复杂,一定写对,反复对照确认
#HTML 是超文本标记语言,而 XML 是可扩展标记语言。
#功能状态不同。HTML 用于显示数据,它是静态的;而 XML 用于传输数据,XML中的标记用来描述数据的性质和结构,它是动态的。
# can't use from bs4 import BeautifulSoup:
##It looks like you're parsing an XML document using an HTML parser.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

loc = input('Enter location:')
#URL http://py4e-data.dr-chuck.net/comments_42.xml Sample
#http://py4e-data.dr-chuck.net/comments_1702976.xml real
while len(loc)<1:
    loc ='http://py4e-data.dr-chuck.net/comments_42.xml'
html = urllib.request.urlopen(loc).read()
#filehand html and read it
print('Retrieving',loc)

xml = html.decode()
#此步decode解码是为了在计算机显示网页内容;
#??如果描述性质和结构就可解决问题,无需解码,直接使用ET将xml字符串转坏为element对象
#进结构的目录需要解码
x = len(xml)
print('Retrieved',x,'characters')

tree = ET.fromstring(xml)
#!!!acess web data must先解码,获得xml格式,再用ET将xml字符串转换成Element对象
#ET.fromstring() 可以在解析xml格式时，将字符串转换为Element对象，解析树的根节点。
tags = tree.findall('.//count')
#print('tags:',tags) tags is a list
#counts = tree.findall('.//count')
#1.Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details.
#2.You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
#tree = ET.fromstring(xml)
#comments = tree.findall('comments/comment')--进结构的目录
#for item in comments:
    #nums = int(item.find('count').text)
    #sum += nums

print('Count:',len(tags))
#?? Why double slash
#regular expression \ means \ is exactually /
#\:转义符，将特殊字符进行转义，忽略其特殊意义a\.b匹配a.b，但不能匹配ajb，.被转义为特殊意义\\\
sum = 0
# 1.sum object is not literal; first inall=0,inall += x(literal);inall is a varible nat a sum function,print it
# 2.make a list and use a sum function.
for tag in tags:
    sum += int(tag.text)

print(sum)
#Sample Execution
