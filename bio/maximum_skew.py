Genome = 'CATTCCAGTACTTCGATGATGGCGTGAAGA'
def MaximumSkew(Genome):
    skew_array = SkewArray(Genome)
    maxpositions = []
    for pos in range(len(Genome)):
        if skew_array[pos] == max(skew_array.values()):
            maxpositions.append(pos)
    return maxpositions

def SkewArray(Genome):
    Skew = {}
    n = len(Genome)
    Skew[0] = 0
    for i in range(n):
        if Genome[i] == "C":
           Skew[i+1] = Skew[i] - 1
        elif Genome[i] == "G":
            Skew[i+1] = Skew[i] + 1
        else:
            Skew[i+1] = Skew[i]
    return Skew

print(SkewArray(Genome))
print(MaximumSkew(Genome))