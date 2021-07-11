str = 'X-DSPAM-Confidence: 0.8475'
colonpos = str.find(':')
print('The position of the colon is', colonpos)
num = str[colonpos+2:]
floating_num = float(num)
print(floating_num)
print(type(floating_num))