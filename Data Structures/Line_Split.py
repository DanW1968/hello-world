fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip() #get rid of new lines
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
