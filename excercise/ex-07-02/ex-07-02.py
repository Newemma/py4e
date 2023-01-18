fn = input('Enter the filename:')
if len(fn) < 1: fn = 'mbox-short.txt'
fh = open(fn)
all = 0
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find('0')
        value = float(line[pos:])
        all = all + value
        count = count+1
if count >0:
    print ('Average spam confidence:',all/count)
