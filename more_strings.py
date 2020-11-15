greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())


fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa=fruit.find('z')
print(aa)


greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)

nstr = greet.replace('o','x')
print(nstr)

data = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
