fname = input('Enter a file name:')
try:    
    fhand = open(fname)
    for i in fhand:
        print(i.rstrip().upper())
except:
    print('No such file:', fname)
    