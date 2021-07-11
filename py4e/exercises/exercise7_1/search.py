fname = input('Enter the file name:')
total = 0
count = 0


try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - you have been punk\'d!')
    else:
        fhand = open(fname)
        for line in fhand:
            line = line.rstrip()
            if line.find('X-DSPAM-Confidence:') == -1:
                continue
            pos_at_colon = line.find(':')
            value = line[pos_at_colon+2:]
            total = total + float(value)
            count = count + 1
            average = total/count
        print('Average spam confidence:', average)

except:
    print('invalid')

