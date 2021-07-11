pattern = 'CCAGATC'

def reverse(pattern):
    reverse = []
    pattern.split() # convert the string pattern into a list ['AAAACCCGGT']
    for char in pattern:  
        reverse.insert(0, char) # add to an empty list each iterable character to the front
        rev = ''.join(reverse)  # join list items together using no space
    return rev

#   or through string concatenation in the beginning
def Reverse(pattern):
    rev = ''
    for i in pattern:
        rev = i + rev
    return rev


def complement(pattern):
    complement = ''
    for char in range(len(pattern)):
        if pattern[char] == 'A':
            complement += 'T'
        elif pattern[char] == 'T':
            complement += 'A'
        elif pattern[char] == 'G':
             complement += 'C'
        elif pattern[char] == 'C':
            complement += 'G'
    return complement

#   or using .replace method

def Complement(pattern):
    pattern = pattern.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    return pattern

def reverse_complement(pattern):
    return reverse(complement(pattern))

print('The reverse complement of ' + pattern + ' is ' + reverse_complement(pattern))
