# Frequent Words Problem: Find the most frequent k-mers in a string.
     # Input: A string Text and an integer k.
     # Output: All most frequent k-mers in text.
str = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
k = 3     # length of the pattern


# returns a dictionary with patterns as keys that set their frequency counts to the value 
def frequency_map(str, k):
     frequency = {}
     for i in range(len(str)-k+1):
          # defines all the possible patterns of k-mer in the string, str
          pattern = str[i:i+k]
          # assigns the default value of 0 to each key (which is each possible k-mer pattern) to zero
          frequency[pattern] = 0
          # the below code is adapted from pattern_count function earlier, which with a defined pattern tells you how many times that pattern appears
          # using another iteration loop, iterate through the string with all possible 3-mer patterns and seeing if they match the 'iteration slider'
          for i in range(len(str)-len(pattern)+1):
               if str[i:i+len(pattern)] == pattern:
                    # set the value of the frequency key: count by 1 if the 'slider' pattern is equal to the possible pattern
                    frequency[pattern] = frequency[pattern] + 1
     return frequency
     
def frequent_patterns(str, k):
     seq = []
     frequency = frequency_map(str, k)
     # finds the highest value that occurs in the frequency counts
     max_count = max(frequency.values())
     for key in frequency:
          # going through the list of counts, if the value in the frequency dictionary earlier is equal to the highest count
          if frequency[key] == max_count:
               # add that key to the list
               seq.append(key)
     return seq

print(frequency_map(str,k))
print(frequent_patterns(str, k))
