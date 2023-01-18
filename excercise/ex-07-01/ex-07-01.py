fn = input('Enter filename:')
if len(fn) < 1: fn = 'words.txt'
fh = open(fn)
for line in fh:
    line = line.rstrip()
    print(line.upper())
