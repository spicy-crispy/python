def pattern_count(str, pattern):
    count = 0
    # for example, if the pattern was 3 letters long and the text was 6, 6-3 = 3, but since range is non-exclusive of the final number, you add 1
    # so range(4) would include 0 to 3
    for i in range(len(str)-len(pattern)+1):
        # next part checks if the pattern on the "slider" that slides over by i is equal to the pattern, if so, it counts it
        if str[i:i+len(pattern)] == pattern:
            count = count + 1
    return count


# here's an example:
str = 'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC'
pattern = 'TGATCA'
result = pattern_count(str,pattern)
print('Number of times', pattern, 'appears:', result)