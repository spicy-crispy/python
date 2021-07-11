# Prints each line of a file
count = 0
samplefile = open('sample.txt')
for i in samplefile:
    count = count + 1
    print(i)
print('Line Count:', count)
