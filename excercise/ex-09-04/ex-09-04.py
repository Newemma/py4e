fname = input('Enter filename:')
if len(fname) < 1 : # make a convenience
    fname = 'mbox-short.txt'
fh = open(fname)
ls = list()# make a space list before for in
for line in fh:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    senders = words[1]
    ls.append(senders)# list senders
counts = dict()# make a dict contains key-value repair [histogram]
for sender in ls:
    counts[sender] = counts.get(sender,0)+1#!!!make histogram [a trick]
    # = if sender not in counts: counts[sender] = 1
    # else: counts[sender] = counts[sender]+1
largest = -1# negative number is a good choice in this plcae.
theword = None
for k,v in counts.items():#!!.items()
    if v > largest:
        largest = v
        theword = k
print(theword,largest)
    #the other:
    #largest = None
    #theword = None
    #if largest is None or counts.get(sender) > largest:
        #theword = sender
        #largest = counts.get(sender)
#print(bigsender,bigcount)
