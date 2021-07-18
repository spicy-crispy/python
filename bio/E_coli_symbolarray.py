with open('E_coli.txt') as file:
    e_coli = file.read()

def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2 - 1]  
    array[0] = pattern_count(genome[0:n//2], symbol)

    for i in range(1, n):  
        array[i] = array[i-1]
    
        if extended_genome[i-1] == symbol: 
            array[i] = array[i]-1   
        if extended_genome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def pattern_count(str, pattern):
    count = 0
    for i in range(len(str)-len(pattern)+1):
        if str[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

array = symbol_array(e_coli, "C")

import matplotlib.pyplot as plt
plt.plot(*zip(*sorted(array.items())))
plt.xlabel("genome position")
plt.ylabel("count of C in half-genome starting at given position")
plt.show()