count = 0
print('Before:', count)
# This loop goes through the numbers in the list and counts their position
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    print(count, thing)
print('After:', count)

print('Summing in a loop')

sum = 0
print('Before:', sum)
for item in [9, 41, 12, 3, 74, 15]:
    sum = sum + item
    print(sum, item)
print('After:', sum)
