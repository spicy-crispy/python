Text = 'TTTAGAGCCTTCAGAGG'
Pattern = 'GAGG'
d = 2
def ApproximatePatternCount(Text, Pattern, d):
    patterncount = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            patterncount += 1
    return patterncount

def HammingDistance(str1, str2):
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count
    else:
        print('strings must match in length')

print(ApproximatePatternCount(Text, Pattern, d))