# Input:  Strings Pattern and Text along with an integer d (max # of mismatches)
# Output: A list containing all starting positions where Pattern appears as a substring of Text with at most d mismatches

Text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
Pattern = 'ATTCTGGA'
d = 3
def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            positions.append(i)
    return positions


def HammingDistance(str1, str2):
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count
    else:
        print('strings must match in length')

print(ApproximatePatternMatching(Text, Pattern, d))
