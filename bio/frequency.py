# Frequent Words Problem: Find the most frequent k-mers in a string.
     # Input: A string Text and an integer k.
     # Output: All most frequent k-mers in text.
str = 'CGATATATCCATAG'   # length is 14
k = 3     # length of the pattern

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
                    frequency[pattern] = frequency[pattern] + 1
     return frequency
     
print(frequency_map(str, k))