counts = dict()
print('Enter a line of test :')
line = input('')

words = line.split()

print('Words:', words)

print('Counting....')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)
