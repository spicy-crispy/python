def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2 - 1]   # extended because circular DNA, 
    #   so must extend genome by length of the window (minus 1) to catch the tail to head fusion nucleotides. 
    #   note: if you dont -1, still get same answer, just redundancy. in this case we want to add 3 nucleotides to genome to make extended genome
    for i in range(n):
        array[i] = pattern_count(extended_genome[i:i+(n//2)], symbol)
    return array

def pattern_count(str, pattern):
    count = 0
    for i in range(len(str)-len(pattern)+1):
        if str[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

genome = "AAAAGGGG"
symbol = "A"
print('{0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3} is correct answer')
print(symbol_array(genome, symbol), "is the result")

#   array starting at i = 0 means window starting from 0 has 4 A's
#   since we selected length/2 as the window (4), that means 4 A's in the [0:4] window, 
#   [1:5] window has 3 A's, etc