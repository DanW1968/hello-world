fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand : 
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        #idiom : retrieve/create/update counter
        di[w] = di.get(w,0)+1
       # print(w,'new', di[w])

print(di)

#find most common word



