from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url: http://py4e-data.dr-chuck.net/comments_1702974.html copy it must be fast!!
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")#??html.parser --- 简单的 HTML 和 XHTML 解析器
#这一步解码了
spans = soup('span')
#print(spans) spans is a list
numbers = []

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))
