counts = dict()
print('Enter a line of text:')
line = input('')
# Split the input text into separate words
words = line.split()
print('Words:', words)

# Loop through the words and use a dictionary to track the count
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)