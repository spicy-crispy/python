#    "forward half strand" that they use is the lagging strand and the "reverse half strand" is the leading strand.

def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2 - 1]  

    # for the first window, the first genome half, find counts of the symbol G, C, A, or T
    array[0] = pattern_count(genome[0:n//2], symbol)

    for i in range(1, n):   #  the range will be length of entire genome - 1
        # start by setting the current array value equal to the previous array value in the loop
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        # so basically if the symbol existed in the character before the current sliding window, you would decrease count by 1 because after moving window it's no longer there in the current new window
        # if the symbol is at the end of the current sliding window, then you would add count by  1 since it appeared
        if extended_genome[i-1] == symbol:  # if the symbol was present in the first char position previous to sliding the window, subtract 1 from the
            array[i] = array[i]-1   #   if the last character in the window is equal to the symbol, add count by 1
        if extended_genome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def pattern_count(str, pattern):
    count = 0
    for i in range(len(str)-len(pattern)+1):
        if str[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

genome = 'AAAAGGGG'
symbol = 'A'
print(symbol_array(genome, symbol))

#   some notes that will help
#   extended_genome = 'AAAAGGGGAAA'
#   your windows will be i = 0; AAAA    array[0] = 4 (4 counts of A)
#                        i = 1; AAAG    array[1] = 3
#                        i = 2; AAGG    array[2] = 2
#                        i = 3: AGGG    array[1] = 1
#                        i = 4; GGGG    array[4] = 0
#                        i = 5; GGGA    array[5] = 1
#                        i = 6; GGAA    array[6] = 2
#                        i = 7: GAAA    array[7] = 3
#
#   array[0] = pattern_count(genome[0:n//2], symbol) -> n = genome length which is 8 and divide by half is 4. 
#   genome[0:4] is 'AAAA' and the symbol A counts for 4 times here

#   array[0] = 4

#   now the loop:

#   for i in range(1, n):   the range will be length of entire genome - 1 = 7
        # start by setting the current array value equal to the previous array value in the loop
#       array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
#       if extended_genome[i-1] == symbol:  # if the symbol was present in the first char position previous to sliding the window, subtract 1 from the
#           array[i] = array[i]-1   #   if the last character in the window is equal to the symbol, add count by 1
#       if extended_genome[i+(n//2)-1] == symbol:
#           array[i] = array[i]+1

#   i = 1: array[1] = array[0] = 4
#   extended_genome[0] == A -> True 
#   so array[1] = 4 - 1 = 3

#   i = 2: array[2] = array[1] = 3
#   extended_genome[1] == A -> True 
#   so array[2] = 3 - 1 = 2

#   i = 3: array[3] = array [2] = 2
#   extended_genome[2] == A -> True
#   so array[3] = 2 - 1 = 1

#   i = 4: array[4] = array[3] = 1
#   extended_genome[3] == A => True
#   so array[4] = 1 - 1 = 0

#   i = 5: array[5] = array[4] = 0
#   extended_genome[4] == A => False (No A at the position before this sliding window)
#   extended_genome[5 + (4) - 1] which is extended_genome[8] == A => True (Found A at the last position of this current sliding window)
#   array[5] = 0 + 1

#   and etc

