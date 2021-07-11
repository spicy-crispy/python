x = 5
if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
else :
    print('Not bigger than 2')
print('Done with 2')

# Nested indentation example below:
for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')  # only prints Bigger than 2 if i > 2 
    print('Done with i', i) # in same block as print(i) so always prints done with i after each iteration
print('All Done')