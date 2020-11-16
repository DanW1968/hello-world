fhand = open("c:/Src1/hello-world/mbox-short.txt")
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)



fname = input('Enter the file name : ')
fhand = open(fname)
count = 0
for line in fhand : 
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)
