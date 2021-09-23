pattern = 'ATAT'
genome = 'GATATATGCATATACTT'
#   input: a pattern and a string (genome)
#   output: the positions at which the pattern appears in the string/genome.

def pattern_match(pattern, genome):
    positions = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions


