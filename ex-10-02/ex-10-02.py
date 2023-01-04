fn = input('Enter filename:')
if len(fn) < 1: fn = 'mbox-short.txt'
fh = open (fn)
hlis = list()
for line in fh:
    if line.startswith('From ') :
        #print(line)
        line = line.split()
        tims = line[5]
        #print(tims)
        hchop = tims.split(':')
        hours = hchop[0]
        hlis.append(hours)
#print(hlis)
counts = dict()
for hour in hlis:
    counts[hour] = counts.get(hour,0)+1
#print(counts)
#!!sorted(),(k,v);sorting/comparing btween tuple but not dictionary.
for k,v in sorted(counts.items()):
#for k,v in sorted([(v,k) for k,v in counts.items()]):
    #for k,v in sorted([counts.items(),reverse=True):
    #!!!'reverse=True' after lists and ','
    print(k,v)
