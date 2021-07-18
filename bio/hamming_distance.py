#   Input: two strings of equal length
#   Output: The Hamming distance between the two strings

str1 = 'CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
str2 = 'ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'

def HammingDistance(str1, str2):
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count
    else:
        print('strings must match in length')

print(HammingDistance(str1, str2))
