counts = dict()
names = ['diluc', 'kazuha', 'diluc', 'benny', 'kazuha']
for item in names :
    counts[item] = counts.get(item, 0) + 1
print(counts)

# get is equal to
#   if item in counts:
#       x = counts[name]
#   else:
#       x = 0