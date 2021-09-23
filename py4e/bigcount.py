name = input('Enter file:')
fhand = open(name)
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value
    
print(bigword, bigcount)