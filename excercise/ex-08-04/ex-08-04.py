fn = input('Enter the filename:')
if len(fn) < 1: fn = 'romeo.txt'
fh = open(fn)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if not word in lst:
            lst.append(word)
lst.sort()
print(lst)
#print(lst.sort()) WRONG just step one by oncourse ?
#build a new space list
