import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))#双括号,一个元祖
#connect 是客户端;bind 是服务端
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
#print语句默认打印一行,末尾加换行符;end=' '表示末尾加空格('',之间加几个空格就空几格,与前面代码逗号隔开)
#eg:>>> print(‘a’)a>>> print(‘a’,end=’ ')a >>> print(‘a’,end=‘1234’)a1234>>>

mysock.close()#括号
# always 'my'sock
