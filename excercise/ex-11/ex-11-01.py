fn = input('Enter name:')
if len(fn)<1: fn = 'regex_sum_1702972.txt'
import re
list = []
fh = open(fn)
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x)>0:
        for y in x:
            tx = int(y)
            list.append(tx)
    xx = sum(list)
print(xx)
