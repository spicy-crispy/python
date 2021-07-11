found = None
print('Before', found)
for num in [9, 41, 12, 3, 74, 15]:
    if num == 3:
        found = True
    else: 
        found = False
    print(found, num)
print('After', found)