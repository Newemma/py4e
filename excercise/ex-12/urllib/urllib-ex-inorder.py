#111
import urllib.request, urllib.parse, urllib.error
fh = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
# encode accomplishment

counts = dict()
for line in fh:
    words = line.decode().split()#decode!
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)
for v,k in sorted( [(k,v) for v,k in sorted(counts.items())],reverse = True):
    print(k,v,end='  ')
