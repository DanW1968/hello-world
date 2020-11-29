for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

z = ['Joesph', 'Glenn', 'Sally']
for x in z :
    print('Happy New Year', x)
print('Done')

friends = ['Joesph', 'Glenn', 'Sally']
print(friends[1])

lotto = [2, 12, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
