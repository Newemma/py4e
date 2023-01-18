fn = input('Enter the filename:')
if len(fn) < 1: fn = 'mbox-short.txt'
fh = open(fn)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        count = count+1
        sen = line.split()
        print(sen[1])
print('There were',count,'lines in the file with From as the first word')
