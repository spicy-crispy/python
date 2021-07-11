fname = input('Enter file:')
fhand = open(fname)
new_list = []

# for each line in the file (iterate through the lines, gives each line as a list after the split)
for line in fhand:
    text = line.strip().split()
    # after getting the lists split by comma, iterate through the items in that new list (text) and add each word into an empty list
    for word in text:
        # if the word is not in the list, add it (avoids duplicates)
        if word not in new_list:
            new_list.append(word)

sorted_list = sorted(new_list)
print(sorted_list)