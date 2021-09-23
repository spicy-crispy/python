Genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

# Outputs the position(s) at minimum skew, the point at which #G-#C is minimzed 


# (where reverse half-strand aka leading strand ends and where the forward half-strand aka lagging strand starts)
# this location is known as ori / origin of replication 
def MinimumSkew(Genome):
    skew_array = SkewArray(Genome)
    minpositions = []
    for pos in range(len(Genome)):
        if skew_array[pos] == min(skew_array.values()):
            minpositions.append(pos)
    return minpositions

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
print(MinimumSkew(Genome))