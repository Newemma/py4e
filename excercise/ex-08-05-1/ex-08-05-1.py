fname = input('Enter filename: ')
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    sen = line.split()
    # if line =='':continue
    # if len(sen) < 0: continue
    # if line.startswith('From '):
    if len(sen) < 3 or sen[0] !='From':continue
    count = count+1
    print(sen[1])
print('There were',count,'lines in the file with From as the first word')
# print helps debug
# Gurdian in a compound statement. Gurdian comes before.
# continue means skip
